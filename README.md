# ROBO-LLM Framework

The ROBO-LLM Framework is a pipeline for using Large Language Models (LLMs) to control robotic systems through voice commands. This framework enables seamless interaction with robots by translating natural language inputs into executable robotic control scripts.

## Overview

The framework works as follows:

1. **Voice Command**: The user provides a voice input to the system.

2. **Speech-to-Text Module**: The voice command is converted into raw text using a speech-to-text module.

3. **Input Refinement**:
   - The raw text input is sent to an LLM for refinement.
   - The LLM rewrites the input into a structured format based on a context prompt.
   - The context prompt contains details about:
     - The robotic system being controlled.
     - The type of environment the robot operates in.
     - The available functions of the robot (e.g., `move(x)` for movement).

4. **Control Script Generation**:
   - The refined input is sent to another LLM that generates a control script.
   - The script is written in a format that the robotic control system can execute.

5. **Robotic System Execution**:
   - The generated control script is sent to the robotic system.
   - The robot performs the desired actions based on the script.

## Key Features
- **Context-Aware Refinement**: Ensures commands are tailored to the specific capabilities and environment of the robot.
- **Abstracted Functionality**: Simplifies the interaction by abstracting robotic functions into high-level commands.
- **End-to-End Automation**: Automates the entire process from user command to robotic execution.

## Use Case Example
Imagine a robotic arm in a warehouse that can pick and place objects. Using ROBO-LLM:

1. The user says, "Move the box to the top shelf."
2. The speech-to-text module converts this to: `Move the box to the top shelf.`
3. The Input Refinement LLM processes this input, rewriting it as a structured command like: `pick(box); move(top_shelf); place(box).`
4. The Control Script Generation LLM generates the low-level script required for the robotic arm, such as: 'arm.pick("box"); arm.moveTo("top_shelf"); arm.place("box");'

5. The robotic system executes these instructions.

## Diagram
Refer to the diagram below for a visual representation of the framework:

![image](https://github.com/user-attachments/assets/88534ce6-7a7a-4a64-a7f5-6f62930cca98)


## How to Use
1. Set up the speech-to-text module.
2. Define the context prompt with robot capabilities and environment details.
3. Integrate the LLMs for Input Refinement and Control Script Generation.
4. Connect the robotic system to the framework.

## Future Enhancements
- Improved LLM fine-tuning for domain-specific applications.
- Support for additional languages in speech-to-text conversion.
- Integration with more types of robots and environments.

