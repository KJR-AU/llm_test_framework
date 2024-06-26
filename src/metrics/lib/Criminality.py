from ..Metric import Metric
from ..MetricNotAvailableError import MetricNotAvailableError


class Criminality(Metric):
    
    def __init__(self):
        super().__init__(name="Criminality", higher_is_better=False)

    @property
    def feedback_name(self):
        return "criminality_with_cot_reasons"

    def _feedback_with_selector(self, feedback):
        return (
            feedback
            .on_output()
        )