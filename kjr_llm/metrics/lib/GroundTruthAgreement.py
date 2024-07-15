from ..Metric import Metric
from ...prompts import PromptSet
from trulens_eval import Feedback
from trulens_eval.feedback import GroundTruthAgreement as GTA
from typing import List
from trulens_eval.feedback import GroundTruthAgreement as GTA

# Define a class named GroundTruthAgreement that inherits from the Metric class.
class GroundTruthAgreement(Metric):
    
    def __init__(self, golden_set: List[dict] | PromptSet, *args, agreement_measure = "agreement_measure", **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if isinstance(golden_set, PromptSet):
            golden_set = golden_set.as_golden_set()

        # Will raise exception if prompts are invalid
        self._validate_prompts(golden_set)

        self.golden_set = golden_set
        # Store the name of the measure used to evaluate the agreement.
        self.ground_truth_measure = agreement_measure

    # Property method to return the name of the feedback metric.
    @property
    def feedback_name(self):
        return self.ground_truth_measure

    # Property method to compute the agreement between the golden set and the predictions.
    @property
    def ground_truth_agreement(self):
        return GTA(self.golden_set)

    def _validate_prompts(self, prompts: List[dict]):
        for prompt in prompts:
            if not (prompt.get("query") and prompt.get("response")):
                print(prompt)
                raise ValueError("All prompts in a ground truth prompt set must have 'query' and 'response'")

    def _feedback(self, provider=None):
        """
        Generates a feedback object using the specified provider.

        :param provider: The feedback provider to use.
        :return: A Feedback object.
        """
        agreement_measure = getattr(self.ground_truth_agreement, self.feedback_name)
        return Feedback(agreement_measure, *self.args, **self.kwargs)

    def _feedback_with_selector(self, feedback):
        """
        Applies a feedback selector to the feedback object. This method is intended to be overridden in subclasses.

        :param feedback: The feedback object to apply the selector to.
        :return: The feedback object with the selector applied.
        """
        return feedback.on_input_output()

    @classmethod
    def from_prompts_file_json(cls, file_path: str, *args, **kwargs):
        prompts = PromptSet.from_json_file(file_path)
        return cls(prompts, *args, **kwargs)
