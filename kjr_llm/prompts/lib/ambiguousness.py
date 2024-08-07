from pathlib import Path

from ..prompt_set import PromptSet

current_file_dir = Path(__file__).resolve().parent

prompt_definition_path = current_file_dir / "data" / "ambiguousness.json"

AmbiguousnessPromptSet = PromptSet.from_json_file(prompt_definition_path)
