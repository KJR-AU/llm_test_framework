from llm_test_framework.kjr_llm.metrics import Metric
from trulens_eval import Feedback
from typing import List

class GroundTruthAgreement(Metric):
    
    def __init__(self, golden_set: List[dict], *args, agreement_measure = "", **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.golden_set = golden_set
        self.agreement_measure = agreement_measure

    @property
    def feedback_name(self):
        return "ground_truth_agreement"

    @property
    def ground_truth_agreement(self):
        return GroundTruthAgreement(self.golden_set)

    def __feedback(self, provider):
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