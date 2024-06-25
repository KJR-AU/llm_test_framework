from .Metric import Metric
from .MetricNotAvailableError import MetricNotAvailableError


class ViolenceGraphic(Metric):
    
    def __init__(self):
        super().__init__(name="Violence Graphic")

    @property
    def feedback_name(self):
        return "moderation_violencegraphic"

    @property
    def llama3(self):
        raise MetricNotAvailableError()

    def __feedback_with_selector(self, feedback):
        return (
            feedback
            .on_output()
        )