# Import the base Metric class from the parent package.
from ..Metric import Metric

# Import the custom exception MetricNotAvailableError from the parent package.
from ...exceptions import MetricNotAvailableError

# Define a class named HarassmentThreatening that inherits from the Metric class.
class HarassmentThreatening(Metric):
    
    # Constructor method to initialize the HarassmentThreatening object.
    def __init__(self):
        # Call the constructor of the parent Metric class with the name "Harassment Threatening" and specify that higher values are not better.
        super().__init__(name="Harassment Threatening", higher_is_better=False)

    # Property method to return the name of the feedback metric.
    @property
    def feedback_name(self):
        return "moderation_harassment_threatening"

    # Property method to handle the llama3 feedback.
    @property
    def llama3(self):
        # Raise a MetricNotAvailableError because the llama3 feedback is not available for this metric.
        raise MetricNotAvailableError()

    # Method to apply a selector to the feedback.
    def _feedback_with_selector(self, feedback):
        # Apply the feedback selector to the output and return the result.
        return (
            feedback
            .on_output()  # Select feedback based on the output.
        )