from ...metrics import SelfHarm as SelfHarmMetric
from ...prompts.lib import SelfHarmPromptSet
from ..test_set import TestSet

# Define the feedback metrics for the SelfHarm test set
_feedbacks = [SelfHarmMetric()]

# Create an instance of TestSet for evaluating self-harm content
SelfHarm = TestSet(SelfHarmPromptSet, _feedbacks, name="Self Harm")
