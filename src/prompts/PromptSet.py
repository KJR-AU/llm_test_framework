import json
from typing import List
from .Prompt import Prompt

class PromptSet:

    def __len__(self):
        return len(self.inputs)

    def __iter__(self):
        return self.inputs.__iter__()

    def __init__(self, inputs: List[Prompt]):
        self._inputs = inputs

    @property
    def inputs(self):
        return self._inputs

    @classmethod
    def from_json_file(cls, file_name: str):
        with open(file_name) as f:
            obj = json.load(f)
        return cls.from_json(obj)
        
    @classmethod
    def from_json(cls, json: dict):
        inputs = [Prompt.from_json(input_json) for input_json in json]
        return cls(inputs)