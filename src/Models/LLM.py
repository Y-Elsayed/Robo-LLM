from transformers import AutoModelForCausalLM, AutoTokenizer
from accelerate import Accelerator
import torch

# Load model and tokenizer once, then reuse them for multiple prompts
class LLMModel:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.accelerator = Accelerator()
        
        # Load the model and tokenizer once
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype="auto",
            device_map="auto"
        )
        
        # Set pad_token_id to eos_token_id to avoid padding issues
        self.model.config.pad_token_id = self.model.config.eos_token_id
        
        # Use accelerator to manage device placement
        self.model = self.accelerator.prepare(self.model)
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

    def generate(self, prompt: str) -> str:
        # Prepare the prompt and generate response
        inputs = self.tokenizer(
            prompt, return_tensors="pt", truncation=True, max_length=512
        ).to(self.model.device)

        # Generate response from the model with increased max_new_tokens
        generated_ids = self.model.generate(
            **inputs,
            max_new_tokens=500,  # Increase the number of tokens
            num_return_sequences=1,
            temperature=0.7,  # Control randomness
            top_p=0.95,  # Use nucleus sampling
            no_repeat_ngram_size=2,  # Avoid repeating the same n-grams
            do_sample=True  # Enable sampling
        )

        # Decode the generated output
        response = self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        return response
