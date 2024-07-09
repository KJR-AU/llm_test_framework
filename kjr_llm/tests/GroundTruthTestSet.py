from .TestSet import TestSet
from ..metrics import GroundTruthAgreement
from ..prompts import PromptSet

class GroundTruthTestSet(TestSet):
    """
    This class extends the `TestSet` class and integrates the `GroundTruthAgreement` metric
    to evaluate the GroundTruth of responses based on provided prompts and context.
    """
    
    def __init__(self, prompts: PromptSet, name: str | None = None, agreement_measure: str = "agreement_measure"):
        """
        Constructor method to initialize an instance of GroundTruthTestSet with the given prompts, context path, and optional name and provider.

        Args:
            prompts (PromptSet): The set of prompts to be used for evaluation.
            name (str | None, optional): The name of the test set. Defaults to None.
            agreement_measure (str, optional): The name of the agreement measure
                                        used by the ground truth agreement metric.
        """
        feedback = GroundTruthAgreement(prompts, agreement_measure=agreement_measure)
        feedback_fn = feedback._feedback_with_selector(feedback._feedback())
        # Call the constructor of the parent class (TestSet) with the prompts, feedback, and optional name and provider
        super().__init__(prompts, [feedback_fn], name=name, default_provider=None)

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