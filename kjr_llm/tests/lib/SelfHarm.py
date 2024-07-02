"""
This module defines the `SelfHarm` test set, which is a specific instance of the `TestSet` class used to evaluate the presence of self-harm content in responses from a language model or a RAG application.
"""

from ..TestSet import TestSet
from ...prompts.lib import SelfHarmPromptSet
from ...metrics import SelfHarm as SelfHarmMetric

# Define the feedback metrics for the SelfHarm test set
_feedbacks = [SelfHarmMetric()]

# Create an instance of TestSet for evaluating self-harm content
SelfHarm = TestSet(SelfHarmPromptSet, _feedbacks, name="Self Harm")