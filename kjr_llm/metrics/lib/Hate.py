# Import the base Metric class from the parent package.
from ..Metric import Metric

# Import the custom exception MetricNotAvailableError from the parent package.
from ..MetricNotAvailableError import MetricNotAvailableError

# Define a class named Hate that inherits from the Metric class.
class Hate(Metric):
    
    # Constructor method to initialize the Hate object.
    def __init__(self):
        # Call the constructor of the parent Metric class with the name "Hate" and specify that higher values are not better.
        super().__init__(name="Hate", higher_is_better=False)

    # Method to apply a selector to the feedback.
    def _feedback_with_selector(self, feedback):
        # Apply the feedback selector to the output and return the result.
        return (
            feedback
            .on_output()  # Select feedback based on the output.
        )

    # Property method to return the name of the feedback metric.
    @property
    def feedback_name(self):
        return "moderation_hate"

    # Property method to handle the llama3 feedback.
    @property
    def llama3(self):
        # Raise a MetricNotAvailableError because the llama3 feedback is not available for this metric.
        raise MetricNotAvailableError()