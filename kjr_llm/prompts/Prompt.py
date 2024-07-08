"""
This Python script defines a class `Prompt` that represents a single prompt with an input and an optional expected output.
The class provides methods to initialize a `Prompt` from a JSON object and to access its properties.

Dependencies:
- None

Class Methods:
- `from_json(cls, json: dict)`: A class method that initializes a `Prompt` from a JSON object.

Instance Methods:
- `__repr__(self)`: Returns a string representation of the `Prompt` object.
- `__init__(self, input: str, expected_output: str = None)`: Initializes a `Prompt` object with the given input and optional expected output.

Properties:
- `input`: A property that returns the input of the `Prompt`.
- `expected_output`: A property that returns the expected output of the `Prompt`.
- `has_expected_output`: A property that returns a boolean indicating whether the `Prompt` has an expected output.

"""

class Prompt:
    """
    A class representing a prompt with an input string and an optional expected output string.

    Attributes:
        _input (str): The input string for the prompt.
        _expected_output (str): The expected output string for the prompt.
    """

    def __repr__(self) -> str:
        """
        Returns a string representation of the Prompt object.

        Returns:
            str: A string in the format "Input("input_string", expected_output=expected_output_string)".
        """
        return f"Input(\"{self.input}\", expected_output={self.expected_output})"

    def __init__(self, input: str, expected_output: str = None) -> None:
        """
        Initializes a new instance of the Prompt class.

        Args:
            input (str): The input string for the prompt.
            expected_output (str, optional): The expected output string for the prompt. Defaults to None.
        """
        self._input = input
        self._expected_output = expected_output

    def as_dict(self):
        out = {
            "input": self._input
        }
        if self.has_expected_output:
            out['expected_output'] = self.expected_output
        return out

    @property
    def input(self):
        """
        Getter for the input string.

        Returns:
            str: The input string.
        """
        return self._input

    @property
    def expected_output(self):
        """
        Getter for the expected output string.

        Returns:
            str: The expected output string.
        """
        return self._expected_output

    @property
    def has_expected_output(self):
        """
        Checks if the prompt has an expected output string.

        Returns:
            bool: True if the expected output string is not None, False otherwise.
        """
        return self._expected_output is not None

    @classmethod
    def from_json(cls, json: dict):
        """
        Creates a new instance of the Prompt class from a JSON dictionary.

        Args:
            json (dict): A dictionary containing the input and optionally the expected output.

        Returns:
            Prompt: A new instance of the Prompt class.
        """
        return cls(json['input'], expected_output=json.get('expected_output'))
