"""
This module defines the `Violence` test set, which is a specific instance of the `TestSet` class used to evaluate the presence of violence and graphic violence content in responses from a language model or a RAG application.
"""

from ..TestSet import TestSet
from ...prompts.lib import ViolencePromptSet
from ...metrics import (
    Violence as ViolenceMetric,
    ViolenceGraphic as ViolenceGraphicMetric
)

# Define the feedback metrics for the Violence test set
_feedbacks = [ViolenceMetric(), ViolenceGraphicMetric()]

# Create an instance of TestSet for evaluating violence content
Violence = TestSet(ViolencePromptSet, _feedbacks, name="Violence")