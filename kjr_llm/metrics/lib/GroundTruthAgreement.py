# Import the base Metric class from the parent package and other class, variable and types.
from ..Metric import Metric
from trulens_eval import Feedback
from typing import List
from trulens_eval.feedback import GroundTruthAgreement as GTA

# Define a class named GroundTruthAgreement that inherits from the Metric class.
class GroundTruthAgreement(Metric):
    
    def __init__(self, golden_set: List[dict], *args, ground_truth_measure = "agreement_measure", **kwargs) -> None:
        # Call the constructor of the parent Metric class with the name "Ground Truth".
        super().__init__(name="Ground Truth", *args, **kwargs)
        # Store the golden set of ground truth data.
        self.golden_set = golden_set
        # Store the name of the measure used to evaluate the agreement.
        self.ground_truth_measure = ground_truth_measure

    # Property method to return the name of the feedback metric.
    @property
    def feedback_name(self):
        return self.ground_truth_measure

    # Property method to compute the agreement between the golden set and the predictions.
    @property
    def ground_truth_agreement(self):
        return GTA(ground_truth=self.golden_set)

    def __feedback(self, provider):
        """
        Generates a feedback object using the specified provider.

        :param provider: The feedback provider to use.
        :return: A Feedback object.
        """
        ground_truth_agreement = self.ground_truth_agreement
        ground_truth_agreement.provider = provider
        agreement_measure = getattr(ground_truth_agreement, self.feedback_name)
        return Feedback(agreement_measure, *self.args, **self.kwargs)

    def _feedback_with_selector(self, feedback):
        """
        Applies a feedback selector to the feedback object. This method is intended to be overridden in subclasses.

        :param feedback: The feedback object to apply the selector to.
        :return: The feedback object with the selector applied.
        """
        return feedback.on_input_output()
    
    @property
    def openai(self):
        """
        Generates a feedback object using the OpenAI provider.

        :return: A Feedback object with the OpenAI provider.
        """
        feedback = self.__feedback(self.provider_openai)
        return self._feedback_with_selector(feedback)

    @property
    def llama3(self):
        """
        Generates a feedback object using the LiteLLM (llama3) provider.

        :return: A Feedback object with the LiteLLM (llama3) provider.
        """
        feedback = self.__feedback(self.provider_llama3)
        return self._feedback_with_selector(feedback)
    
    
