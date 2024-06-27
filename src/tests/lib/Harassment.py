"""
This module defines the `Harassment` test set, which is a specific instance of the `TestSet` class used to evaluate the presence of harassment and threatening content in responses from a language model or a RAG application.
"""

from ..TestSet import TestSet
from ...prompts.lib import HarassmentPromptSet
from ...metrics import (
    Harassment as HarassmentMetric,
    HarassmentThreatening as HarassmentThreateningMetric
)

# Define the feedback metrics for the Harassment test set
_feedbacks = [HarassmentMetric(), HarassmentThreateningMetric()]

# Create an instance of TestSet for evaluating harassment
Harassment = TestSet(HarassmentPromptSet, _feedbacks, name="Harassment")