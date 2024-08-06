from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable
from langchain.chains.base import Chain


class Target:
    """
    A base class representing a target that can invoke a chain with a given prompt and optional additional options.

    Attributes:
        _chain (object): The chain object used to process input.
        _options (dict): A dictionary of additional options to be included in the input when invoking the chain.
        _prompt_key (str): The key used to store the prompt in the input dictionary.
    """

    def __init__(
        self,
        target_app: Chain,
        options: dict[str, Any] | None = None,
        prompt_key: str = "input",
        invoke_method: str = "invoke",
    ):
        """
        Initializes a new instance of the Target class.

        Args:
            chain (object): The chain object to be used for processing input.
            options (dict, optional): A dictionary of additional options to be included in the input
            when invoking the chain. Defaults to an empty dictionary.
            prompt_key (str, optional): The key used to store the prompt in the input dictionary. Defaults to "input".
        """
        self._target_app = target_app
        self._options = options if options is not None else {}
        self._prompt_key = prompt_key
        self._invoke_method = invoke_method

    @property
    def app(self) -> Chain:
        """
        Property that returns the chain object.

        Returns:
            object: The chain object.
        """
        return self._target_app

    def invoke(self, prompt: str) -> dict[str, Any] | str:
        """
        Invokes the chain with the given prompt and optional additional options.

        This method should be overridden by subclasses to provide specific implementation.

        Args:
            prompt (str): The input prompt to be processed by the chain.
        """
        invoke_method: Callable[[Any], dict[str, Any]] = (
            getattr(self._target_app, self._invoke_method) if self._invoke_method is not None else self._target_app
        )
        if not self._options:
            return invoke_method(prompt)
        input_dict = {**self._options, self._prompt_key: prompt}
        return invoke_method(input_dict)
