from ..PromptSet import PromptSet
import os

current_file_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = 'data/violence.json'
full_path = os.path.join(current_file_dir, relative_path)
ViolencePromptSet = PromptSet.from_json_file(str(full_path))