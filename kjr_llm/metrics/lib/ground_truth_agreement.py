from typing import Self

from trulens.core.feedback.feedback import Feedback
from trulens.feedback.groundtruth import GroundTruthAgreement as GroundTruthAgreementTrulens

from ...prompts import PromptSet
from ..metric import Metric


class GroundTruthAgreement(Metric):
    def __init__(
        self, golden_set: list[dict[str, str]] | PromptSet, agreement_measure: str = "agreement_measure"
    ) -> None:
        super().__init__()

        if isinstance(golden_set, PromptSet):
            golden_set_json = golden_set.as_golden_set()
            golden_set = golden_set_json

        self._validate_prompts(golden_set_json)

        self.golden_set = golden_set
        self.ground_truth_measure = agreement_measure

    @property
    def feedback_name(self) -> str:
        return self.ground_truth_measure

    @property
    def ground_truth_agreement(self) -> GroundTruthAgreementTrulens:
        return GroundTruthAgreementTrulens(self.golden_set)

    def _validate_prompts(self, prompts: list[dict[str, str | None]]) -> None:
        for prompt in prompts:
            if not (prompt.get("query") and prompt.get("expected_response")):
                print(prompt)
                error_message: str = "All prompts in a ground truth prompt set must have 'query' and 'expected_response'"
                raise ValueError(error_message)

    def _feedback(self, provider: object) -> Feedback:
        """
        Generates a feedback object using the specified provider.

        :param provider: The feedback provider to use.
        :return: A Feedback object.
        """
        agreement_measure = getattr(self.ground_truth_agreement, self.feedback_name)
        return Feedback(agreement_measure, *self.args, **self.kwargs)

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        """
        Applies a feedback selector to the feedback object. This method is intended to be overridden in subclasses.

        :param feedback: The feedback object to apply the selector to.
        :return: The feedback object with the selector applied.
        """
        return feedback.on_input_output()

    @classmethod
    def from_prompts_file_json(cls, file_path: str, agreement_measure: str = "agreement_measure") -> Self:
        prompts = PromptSet.from_json_file(file_path)
        return cls(prompts, agreement_measure=agreement_measure)
