# Import the base Metric class from the parent package.
from ..Metric import Metric

# Import the custom exception MetricNotAvailableError from the parent package.
from ..MetricNotAvailableError import MetricNotAvailableError

# Define a class named SelfHarm that inherits from the Metric class.
class SelfHarm(Metric):
    
    # Constructor method to initialize the SelfHarm object.
    def __init__(self):
        # Call the constructor of the parent Metric class with the name "Self Harm" and specify that higher values are not better.
        super().__init__(name="Self Harm", higher_is_better=False)

    # Property method to return the name of the feedback metric.
    @property
    def feedback_name(self):
        return "moderation_selfharm"

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