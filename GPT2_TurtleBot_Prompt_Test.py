import src.Models.LLM as llm


prompt = """Imagine we are controlling a robot. The robot has the following functions available to control its movement:
move_forward(x, v): #Moves the robot forward by 'x' points at velocity 'v'.
turn(direction, w): #Turns the robot in the specified direction ('right' or 'left') with angular velocity 'w'.
To control it, you need to generate a script that utilizes these functions in abstract matter to control it. 
You are asked to control the robot to move it in a square.
"""

model = llm.LLMModel("gpt2")
response = model.generate_code(prompt)

