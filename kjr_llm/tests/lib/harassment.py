from ...metrics import Harassment as HarassmentMetric
from ...metrics import HarassmentThreatening as HarassmentThreateningMetric
from ...prompts.lib import HarassmentPromptSet
from ..test_set import TestSet

# Define the feedback metrics for the Harassment test set
_feedbacks = [HarassmentMetric(), HarassmentThreateningMetric()]

# Create an instance of TestSet for evaluating harassment
Harassment = TestSet(HarassmentPromptSet, _feedbacks, name="Harassment")
