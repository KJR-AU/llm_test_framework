from ..PromptSet import PromptSet  # Import the PromptSet class from the parent package.
import os  # Import the os module for file path operations.

# Get the directory of the current file.
current_file_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the JSON file containing the prompts related to insensitivity.
relative_path = 'data/insensitivity.json'

# Construct the full path to the JSON file by joining the current file directory and the relative path.
full_path = os.path.join(current_file_dir, relative_path)

# Create an instance of PromptSet by loading prompts from the specified JSON file.
InsensitivityPromptSet = PromptSet.from_json_file(str(full_path))