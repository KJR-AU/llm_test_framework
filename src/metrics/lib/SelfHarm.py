from .Metric import Metric
from .MetricNotAvailableError import MetricNotAvailableError


class SelfHarm(Metric):
    
    def __init__(self):
        super().__init__(name="Self Harm")

    @property
    def feedback_name(self):
        return "moderation_selfharm"

    @property
    def llama3(self):
        raise MetricNotAvailableError()