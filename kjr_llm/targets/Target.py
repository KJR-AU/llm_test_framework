


class Target:
    def __init__(self, chain, options: dict = {}, prompt_key: str = "input"):
        self._chain = chain
        self._options = options
        self._prompt_key = prompt_key
    
    def invoke(self, prompt: str):
        pass