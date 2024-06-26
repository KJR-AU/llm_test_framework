from ..Metric import Metric
from ..MetricNotAvailableError import MetricNotAvailableError


class Hate(Metric):
    
    def __init__(self):
        super().__init__(name="Hate", higher_is_better=False)

    def _feedback_with_selector(self, feedback):
        return (
            feedback
            .on_output()
        )

    @property
    def feedback_name(self):
        return "moderation_hate"

    @property
    def llama3(self):
        raise MetricNotAvailableError()

    