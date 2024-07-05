"""
This Python script defines a class `PromptSet` that manages a collection of `Prompt` objects.
The class provides methods to initialize a `PromptSet` from a JSON file or a JSON object,
and it allows iteration over the `Prompt` objects within the set.

Dependencies:
- `json` module for parsing JSON data.
- `typing` module for type hints.
- `Prompt` class from the `Prompt` module in the same directory.

Class Methods:
- `from_json_file(cls, file_name: str)`: A class method that initializes a `PromptSet` from a JSON file.
- `from_json(cls, json: dict)`: A class method that initializes a `PromptSet` from a JSON object.

Instance Methods:
- `__len__(self)`: Returns the number of `Prompt` objects in the `PromptSet`.
- `__iter__(self)`: Returns an iterator over the `Prompt` objects in the `PromptSet`.

Properties:
- `inputs`: A property that returns the list of `Prompt` objects in the `PromptSet`.

"""

import json
from typing import List
from .Prompt import Prompt

class PromptSet:
    """
    A class representing a set of prompts.

    Attributes:
        _inputs (List[Prompt]): A list of Prompt objects.
    """

    def __len__(self):
        """
        Returns the number of prompts in the set.

        Returns:
            int: The number of prompts.
        """
        return len(self.inputs)

    def __iter__(self):
        """
        Returns an iterator over the prompts in the set.

        Returns:
            iterator: An iterator over the prompts.
        """
        return self.inputs.__iter__()

    def __init__(self, inputs: List[Prompt]):
        """
        Initializes a new instance of the PromptSet class.

        Args:
            inputs (List[Prompt]): A list of Prompt objects.
        """
        self._inputs = inputs

    @property
    def inputs(self):
        """
        Getter for the list of prompts.

        Returns:
            List[Prompt]: The list of prompts.
        """
        return self._inputs

    @classmethod
    def from_json_file(cls, file_name: str):
        """
        Creates a new instance of the PromptSet class from a JSON file.

        Args:
            file_name (str): The path to the JSON file.

        Returns:
            PromptSet: A new instance of the PromptSet class.
        """
        with open(file_name) as f: # Open the file and assign it to a file object f
            obj = json.load(f) # Load JSON data from the file into a Python object
        return cls.from_json(obj) # Call from_json class method to create PromptSet instance

    @classmethod
    def from_json(cls, json: List[dict]):
        """
        Creates a new instance of the PromptSet class from a JSON dictionary.

        Args:
            json (dict): A dictionary containing the prompts.

        Returns:
            PromptSet: A new instance of the PromptSet class.
        """
        inputs = [Prompt.from_json(input_json) for input_json in json] # Convert each JSON object to Prompt object
        return cls(inputs) # Create a new instance of PromptSet with the list of Prompt objects
