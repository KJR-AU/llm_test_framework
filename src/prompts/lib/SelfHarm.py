"""
This Python script imports the `PromptSet` class from a module located in the parent directory.
It then constructs the full path to a JSON file containing self-harm data by combining the directory of the current file with a relative path.
Finally, it initializes a `PromptSet` object named `SelfHarmPromptSet` using the data from the JSON file.

Steps:
1. Import the `PromptSet` class from the `PromptSet` module located in the parent directory.
2. Get the directory of the current file using `os.path.dirname` and `os.path.abspath`.
3. Define a relative path to the JSON file containing self-harm data.
4. Combine the current file directory with the relative path to get the full path to the JSON file.
5. Initialize a `PromptSet` object named `SelfHarmPromptSet` using the data from the JSON file.

Dependencies:
- `os` module for file path manipulations.
- `PromptSet` class from the `PromptSet` module in the parent directory.

"""

from ..PromptSet import PromptSet  # Import the PromptSet class from the parent package.
import os  # Import the os module for file path operations.

# Get the directory of the current file.
current_file_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the JSON file containing the prompts related to self-harm.
relative_path = 'data/self_harm.json'

# Construct the full path to the JSON file by joining the current file directory and the relative path.
full_path = os.path.join(current_file_dir, relative_path)

# Create an instance of PromptSet by loading prompts from the specified JSON file.
SelfHarmPromptSet = PromptSet.from_json_file(str(full_path))
