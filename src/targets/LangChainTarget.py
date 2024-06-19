from .Target import Target

class LangChainTarget(Target):
    """
    A class representing a target that uses a language chain to process input.

    This class extends the `Target` base class and provides functionality to invoke a language chain with optional additional options.

    Attributes:
        _chain (object): The language chain object used to process input.
        _options (dict): A dictionary of additional options to be included in the input when invoking the chain.
        _prompt_key (str): The key used to store the prompt in the input dictionary.
    
        Methods:
        __init__: Initializes a new instance of the LangChainTarget class.
        chain: Property to get the LangChain object.
        invoke: Invokes the LangChain with a given prompt.
    """
    
    def __init__(self, chain, options: dict = {}, prompt_key: str = "input"):
        """
        Initializes a new instance of the LangChainTarget class.

        Args:
            chain (object): The language chain object to be used for processing input.
            options (dict, optional): A dictionary of additional options to be included in the input when invoking the chain. Defaults to an empty dictionary.
            prompt_key (str, optional): The key used to store the prompt in the input dictionary. Defaults to "input".
        """
        self._chain = chain
        self._options = options
        self._prompt_key = prompt_key

    @property
    def chain(self):
        """
        Getter for the language chain object.

        Returns:
            object: The language chain object.
        """
        return self._chain

    def invoke(self, prompt: str):
        """
        Invokes the language chain with the given prompt and optional additional options.

        Args:
            prompt (str): The input prompt to be processed by the language chain.

        Returns:
            object: The result of invoking the language chain.
        """
        if not self._options:
            return self._chain.invoke(prompt)
        else:
            input_dict = {
                **self._options,
                self._prompt_key: prompt
            }
            return self._chain.invoke(input_dict)