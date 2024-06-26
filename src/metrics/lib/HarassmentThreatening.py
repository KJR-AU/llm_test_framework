from ..Metric import Metric
from ..MetricNotAvailableError import MetricNotAvailableError


class HarassmentThreatening(Metric):
    
    def __init__(self):
        super().__init__(name="Harassment Threatening", higher_is_better=False)

    @property
    def feedback_name(self):
        return "moderation_harassment_threatening"

    @property
    def llama3(self):
        raise MetricNotAvailableError()

    def _feedback_with_selector(self, feedback):
        return (
            feedback
            .on_output()
        )