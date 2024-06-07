from .Target import Target


class LlamaIndexTarget(Target):
    
    def __init__(self, chain, options: dict = {}, prompt_key: str = "input"):
        super().__init__(chain, options=options, prompt_key=prompt_key)

    @property
    def chain(self):
        return self._chain

    def invoke(self, prompt: str):
        if not self._options:
            return self._chain.invoke(prompt)
        else:
            input_dict = {
                **self._options,
                self._prompt_key: prompt
            }
            return self._chain.invoke(input_dict)