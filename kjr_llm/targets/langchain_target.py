from typing import Any

from langchain.chains.base import Chain

from .target import Target


class LangChainTarget(Target):
    """
    A class representing a target that uses a language chain to process input.

    Attributes:
        _chain (object): The language chain object used to process input.
        _options (dict): A dictionary of additional options to be included in the input when invoking the chain.
        _prompt_key (str): The key used to store the prompt in the input dictionary.

        Methods:
        __init__: Initializes a new instance of the LangChainTarget class.
        chain: Property to get the LangChain object.
        invoke: Invokes the LangChain with a given prompt.
    """

    def __init__(self, chain: Chain, options: dict[str, Any] | None = None, prompt_key: str = "input"):
        """
        Initializes a new instance of the LangChainTarget class.

        Args:
            chain (object): The language chain object to be used for processing input.
            options (dict, optional): A dictionary of additional options to be included in the
                                      input when invoking the chain. Defaults to an empty dictionary.
            prompt_key (str, optional): The key used to store the prompt in the input dictionary.
                                        Defaults to "input".
        """
        # Call the parent class's __init__ method to initialize the instance
        super().__init__(chain, options=options, prompt_key=prompt_key, invoke_method="invoke")

    @property
    def chain(self) -> Chain:
        """
        Getter for the language chain object.

        Returns:
            object: The language chain object.
        """
        # Return the private _chain attribute
        return self._target_app
