

class Prompt:
    
    def __repr__(self) -> str:
        return f"Input(\"{self.input}\", expected_output={self.expected_output})"

    def __init__(self, input: str, expected_output: str = None) -> None:
        self._input = input
        self._expected_output = expected_output

    @property
    def input(self):
        return self._input
    
    @property
    def expected_output(self):
        return self._expected_output
    
    @property
    def has_expected_output(self):
        return self._expected_output is not None

    @classmethod
    def from_json(cls, json: dict):
        return cls(json['input'], expected_output=json.get('expected-output'))