from ...metrics import Hate as HateMetric
from ...prompts.lib import HatePromptSet
from ..test_set import TestSet

# Define the feedback metrics for the Hate test set
_feedbacks = [HateMetric()]

# Create an instance of TestSet for evaluating hate speech
Hate = TestSet(HatePromptSet, _feedbacks, name="Hate")
