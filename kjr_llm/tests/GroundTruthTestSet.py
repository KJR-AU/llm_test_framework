# Import the TestSet class from the TestSet module within the current package
from .TestSet import TestSet

# Import the Groundedness class from the metrics module within the parent package
from ..metrics import GroundTruthAgreement

# Import the PromptSet class from the prompts module within the parent package
from ..prompts import PromptSet

# Define a class named GroundTruthTestSet that inherits from TestSet
class GroundTruthTestSet(TestSet):

    """
    This class extends the `TestSet` class and integrates the `GroundTruthTestSet` metric
    to evaluate the GroundTruthTestSet of responses based on provided prompts and golden set prompt.
    """
    
    def __init__(self, prompts: PromptSet, golden_set, name: str | None = None, provider: str | None = None):
        """
        Constructor method to initialize an instance of GroundTruthTestSet with the given prompts, golden set, and optional name and provider.

        Args:
            prompts (PromptSet): The set of prompts to be used for evaluation.
            golden_set: The golden set data used for evaluating ground truth agreement.
            name (str | None, optional): The name of the test set. Defaults to None.
            provider (str | None, optional): The provider of the test set. Defaults to None.
        """
        # Create an instance of GroundTruthAgreement using the provided golden_set
        feedback = GroundTruthAgreement(golden_set)
        # Call the constructor of the parent class (TestSet) with the prompts, feedback, and optional name and provider
        super().__init__(prompts, [feedback], name=name, provider=provider)

    @classmethod
    def from_file(cls, file_path, *args, **kwargs):
        """
        Class method to create a GroundTruthTestSet instance from a JSON file containing prompts.

        Args:
            file_path: The path to the JSON file containing the prompts.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            GroundTruthTestSet: An instance of GroundTruthTestSet initialized with the prompts from the file.
        """
        # Load a PromptSet from a JSON file located at file_path
        prompt_set = PromptSet.from_json_file(file_path)
        # Return a new instance of GroundTruthTestSet using the loaded prompt_set and other arguments
        return cls(prompt_set, *args, **kwargs)