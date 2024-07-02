# Import the Metric class from the parent package
from ..Metric import Metric

# Define a class named AnswerRelevance that inherits from the Metric class
class AnswerRelevance(Metric):

    # Constructor method to initialize the AnswerRelevance object
    def __init__(self):
        # Call the constructor of the parent class (Metric) with the name "Answer Relevance"
        super().__init__(name="Answer Relevance")

    # Method to apply a selector to the feedback
    def _feedback_with_selector(self, feedback):
        # Apply the on_input_output selector to the feedback and return the result
        return (
            feedback
            .on_input_output()
        )

    # Property method to get the name of the feedback
    @property
    def feedback_name(self):
        # Return the name of the feedback as "relevance_with_cot_reasons"
        return "relevance_with_cot_reasons"
