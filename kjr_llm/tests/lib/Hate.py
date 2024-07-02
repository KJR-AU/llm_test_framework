"""
This module defines the `Hate` test set, which is a specific instance of the `TestSet` class used to evaluate the presence of hate speech in responses from a language model or a RAG application.
"""

from ..TestSet import TestSet
from ...prompts.lib import HatePromptSet
from ...metrics import Hate as HateMetric

# Define the feedback metrics for the Hate test set
_feedbacks = [HateMetric()]

# Create an instance of TestSet for evaluating hate speech
Hate = TestSet(HatePromptSet, _feedbacks, name="Hate")