from .Target import Target


class LlamaIndexTarget(Target):
    """
    A class representing a target that uses a LlamaIndex chain to process input.

    This class extends the `Target` base class and provides functionality to invoke a LlamaIndex chain with optional additional options.

    Attributes:
        _target_app (object): The LlamaIndex chain object used to process input.
        _options (dict): A dictionary of additional options to be included in 
                         the input when invoking the chain.
        _prompt_key (str): The key used to store the prompt in the input dictionary.
        _invoke_method (str): The name of the method used to invoke the target.
    """
    
    def __init__(self, app, options: dict = {}, prompt_key: str = "input"):
        """
        Initializes a new instance of the LlamaIndexTarget class.

        Args:
            app (object): The LlamaIndex query engine to be used for processing 
                          input.
            options (dict, optional): A dictionary of additional options to be 
                                      included in the input when invoking the chain. 
                                      Defaults to an empty dictionary.
            prompt_key (str, optional): The key used to store the prompt in the input 
                                        dictionary. Defaults to "input".
        """
        # Call the parent class's __init__ method to initialize the instance
        super().__init__(app, options=options, prompt_key=prompt_key,
                            invoke_method="query")

    @property
    def index(self):
        """
        Getter for the LlamaIndex index object.

        Returns:
            object: The LlamaIndex index object.
        """
        # Return the private _chain attribute
        return self._target_app