from ..PromptSet import PromptSet
import os

current_file_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = 'data/criminality.json'
full_path = os.path.join(current_file_dir, relative_path)
CriminalityPromptSet = PromptSet.from_json_file(str(full_path))