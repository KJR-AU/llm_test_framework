class Target:
    """
    A base class representing a target that can invoke a chain with a given prompt and optional additional options.

    Attributes:
        _chain (object): The chain object used to process input.
        _options (dict): A dictionary of additional options to be included in the input when invoking the chain.
        _prompt_key (str): The key used to store the prompt in the input dictionary.
    """

    def __init__(self, chain, options: dict = {}, prompt_key: str = "input"):
        """
        Initializes a new instance of the Target class.

        Args:
            chain (object): The chain object to be used for processing input.
            options (dict, optional): A dictionary of additional options to be included in the input when invoking the chain. Defaults to an empty dictionary.
            prompt_key (str, optional): The key used to store the prompt in the input dictionary. Defaults to "input".
        """
        self._chain = chain
        self._options = options
        self._prompt_key = prompt_key
    
    def invoke(self, prompt: str):
        """
        Invokes the chain with the given prompt and optional additional options.

        This method should be overridden by subclasses to provide specific implementation.

        Args:
            prompt (str): The input prompt to be processed by the chain.
        """
        pass