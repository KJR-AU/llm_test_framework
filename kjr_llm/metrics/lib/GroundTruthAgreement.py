from ..Metric import Metric
from ...prompts import PromptSet
from trulens_eval import Feedback
from trulens_eval.feedback import GroundTruthAgreement as GTA
from typing import List

class GroundTruthAgreement(Metric):
    
    def __init__(self, golden_set: List[dict] | PromptSet, *args, agreement_measure = "agreement_measure", **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if isinstance(golden_set, PromptSet):
            golden_set = golden_set.as_golden_set()

        # Will raise exception if prompts are invalid
        self._validate_prompts(golden_set)

        self.golden_set = golden_set
        self.agreement_measure = agreement_measure

    @property
    def feedback_name(self):
        return "ground_truth_agreement"

    @property
    def ground_truth_agreement(self):
        return GTA(self.golden_set)

    def _validate_prompts(self, prompts: List[dict]):
        for prompt in prompts:
            if not (prompt.get("query") and prompt.get("response")):
                print(prompt)
                raise ValueError("All prompts in a ground truth prompt set must have 'query' and 'response'")

    def _feedback(self):
        """
        Generates a feedback object using the specified provider.

        :param provider: The feedback provider to use.
        :return: A Feedback object.
        """
        agreement_measure = getattr(self.ground_truth_agreement, self.agreement_measure)
        return Feedback(agreement_measure, *self.args, **self.kwargs)

    def _feedback_with_selector(self, feedback):
        """
        Applies a feedback selector to the feedback object. This method is intended to be overridden in subclasses.

        :param feedback: The feedback object to apply the selector to.
        :return: The feedback object with the selector applied.
        """
        return feedback.on_input_output()