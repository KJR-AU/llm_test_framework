# Import the TestSet class from the TestSet module within the current package
# Import the Groundedness class from the metrics module within the parent package
from pathlib import Path
from typing import Self

from trulens_eval.utils.serial import Lens

from ..metrics import Groundedness
from ..metrics.metric import Metric

# Import the PromptSet class from the prompts module within the parent package
from ..prompts import PromptSet
from ..provider import FeedbackProvider
from .test_set import TestSet


# Define a class named GroundednessTestSet that inherits from TestSet
class GroundednessTestSet(TestSet):
    """
    This class extends the `TestSet` class and integrates the `Groundedness` metric
    to evaluate the groundedness of responses based on provided prompts and context.
    """

    def __init__(
        self, prompts: PromptSet, context_path: Lens, name: str = "", provider: FeedbackProvider | None = None
    ):
        """
        Args:
            prompts (PromptSet): The set of prompts to be used for evaluation.
            context_path: The path to the context data used for evaluating groundedness.
            name (str | None, optional): The name of the test set. Defaults to None.
            provider (str | None, optional): The provider of the test set. Defaults to None.
        """
        # Create an instance of Groundedness using the provided context_path
        feedback = Groundedness(context_path)
        # Call the constructor of the parent class (TestSet) with the prompts, feedback, and optional name and provider
        super().__init__(prompts, [feedback], name=name, default_provider=provider)

    @classmethod
    def from_file(
        cls, file_path: str | Path, feedbacks: list[Metric], name: str = "", provider: FeedbackProvider | None = None
    ) -> Self:
        """
        Class method to create a GroundednessTestSet instance from a JSON file containing prompts.

        Args:
            file_path: The path to the JSON file containing the prompts.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            GroundednessTestSet: An instance of GroundednessTestSet initialized with the prompts from the file.
        """
        # Load a PromptSet from a JSON file located at file_path
        prompt_set = PromptSet.from_json_file(file_path)
        # Return a new instance of GroundednessTestSet using the loaded prompt_set and other arguments
        return cls(prompt_set, feedbacks, name=name, provider=provider)
