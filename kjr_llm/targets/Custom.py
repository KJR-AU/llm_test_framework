"""
This module defines a custom target class that extends a base `Target` class.
The `CustomTarget` class is designed to interact with a chain object, which is used to process and query data.

Classes:
    CustomTarget: A custom implementation of the `Target` class that allows for additional options and a specific prompt key.

Imports:
    from .Target import Target: Imports the base `Target` class from the same package.
"""

from .Target import Target

class CustomTarget(Target):
    """
    A custom implementation of the `Target` class that allows for additional options and a specific prompt key.

    Attributes:
        _chain (object): The chain object used for querying data.
        _options (dict): Additional options to be included in the query.
        _prompt_key (str): The key to use for the prompt in the input dictionary.

    Methods:
        __init__(self, chain, options: dict = {}, prompt_key: str = "input"): Initializes the CustomTarget instance.
        chain(self): Property that returns the chain object.
        invoke(self, prompt: str): Invokes the chain's query method with the provided prompt and options.
    """
    
    def __init__(self, chain, options: dict = {}, prompt_key: str = "input"):
        """
        Initializes the CustomTarget instance.

        Args:
            chain (object): The chain object used for querying data.
            options (dict, optional): Additional options to be included in the query. Defaults to an empty dictionary.
            prompt_key (str, optional): The key to use for the prompt in the input dictionary. Defaults to "input".
        """
        # Call the parent class's __init__ method to initialize the instance
        self._chain = chain
        self._options = options
        self._prompt_key = prompt_key

    @property
    def chain(self):
        """
        Property that returns the chain object.

        Returns:
            object: The chain object.
        """
        # Return the private _chain attribute
        return self._chain

    def invoke(self, prompt: str):
        """
        Invokes the chain's query method with the provided prompt and options.

        Args:
            prompt (str): The prompt to be used in the query.

        Returns:
            object: The result of the chain's query method.
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