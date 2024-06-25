from .Metric import Metric
from .MetricNotAvailableError import MetricNotAvailableError


class Hate(Metric):
    
    def __init__(self):
        super().__init__(name="Hate")

    @property
    def feedback_name(self):
        return "moderation_hate"

    @property
    def llama3(self):
        raise MetricNotAvailableError()