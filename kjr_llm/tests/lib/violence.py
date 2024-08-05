from ...metrics import Violence as ViolenceMetric
from ...metrics import ViolenceGraphic as ViolenceGraphicMetric
from ...prompts.lib import ViolencePromptSet
from ..test_set import TestSet

# Define the feedback metrics for the Violence test set
_feedbacks = [ViolenceMetric(), ViolenceGraphicMetric()]

# Create an instance of TestSet for evaluating violence content
Violence = TestSet(ViolencePromptSet, _feedbacks, name="Violence")
