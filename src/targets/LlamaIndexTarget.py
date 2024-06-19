from .Target import Target


class LlamaIndexTarget(Target):
    """
    A class representing a target that uses a LlamaIndex chain to process input.

    This class extends the `Target` base class and provides functionality to invoke a LlamaIndex chain with optional additional options.

    Attributes:
        _chain (object): The LlamaIndex chain object used to process input.
        _options (dict): A dictionary of additional options to be included in the input when invoking the chain.
        _prompt_key (str): The key used to store the prompt in the input dictionary.
    """
    
    def __init__(self, chain, options: dict = {}, prompt_key: str = "input"):
        """
        Initializes a new instance of the LlamaIndexTarget class.

        Args:
            chain (object): The LlamaIndex chain object to be used for processing input.
            options (dict, optional): A dictionary of additional options to be included in the input when invoking the chain. Defaults to an empty dictionary.
            prompt_key (str, optional): The key used to store the prompt in the input dictionary. Defaults to "input".
        """
        # Call the parent class's __init__ method to initialize the instance
        super().__init__(chain, options=options, prompt_key=prompt_key)

    @property
    def chain(self):
        """
        Getter for the LlamaIndex chain object.

        Returns:
            object: The LlamaIndex chain object.
        """
        # Return the private _chain attribute
        return self._chain

    def invoke(self, prompt: str):
        """
        Invokes the LlamaIndex chain with the given prompt and optional additional options.

        Args:
            prompt (str): The input prompt to be processed by the LlamaIndex chain.

        Returns:
            object: The result of invoking the LlamaIndex chain.
        """
        # Check if there are no additional options
        if not self._options:
            # Invoke the chain with the prompt directly
            return self._chain.invoke(prompt)
        else:
            # Create a dictionary combining the options and the prompt
            input_dict = {
                **self._options,
                self._prompt_key: prompt
            }
            # Invoke the chain with the combined input dictionary
            return self._chain.invoke(input_dict)