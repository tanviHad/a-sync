from langchain.llms import OpenAI
from tqdm import tqdm
import os

# Initialize the OpenAI language model with a specified token limit
llm = OpenAI(max_tokens=2048)

# Directories for saving the scripts
async_directory = 'LLMcode/asynchronous/'
sync_directory = 'LLMcode/synchronous/'

# Ensure both directories exist
os.makedirs(async_directory, exist_ok=True)
os.makedirs(sync_directory, exist_ok=True)

# Define prompts for asynchronous and synchronous scripts
async_prompt = "Write a Python program that creates an asynchronous function to print (Python Exercises!) with a two second delay"
sync_prompt = "Write a Python program Replace each special symbol with # in the following string. Given:str1 = '/*Jon is @developer & musician!!' "

# Start index for filenames
start_index = 1
start_indexs = 11

# Generate asynchronous scripts
for i in tqdm(range(start_index, 2)):  # Adjust the range as needed
    output = llm.predict(async_prompt)
    output = output.replace("```python", "").replace("```py", "").replace("```", "").strip()
    file_path = os.path.join(async_directory, f"asyn{i}.py")
    with open(file_path, "w") as f:
        f.write(output)

# Generate synchronous scripts
for i in tqdm(range(start_indexs, 12)):  # Adjust the range as needed
    output = llm.predict(sync_prompt)
    output = output.replace("```python", "").replace("```py", "").replace("```", "").strip()
    file_path = os.path.join(sync_directory, f"syn{i}.py")
    with open(file_path, "w") as f:
        f.write(output)

# Inform the user that the scripts have been generated
print(f"Generated Python scripts have been saved in '{async_directory}' and '{sync_directory}'")
