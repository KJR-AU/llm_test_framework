from ..TestSet import TestSet
from ...prompts.lib import ViolencePromptSet
from ...metrics import (
    Violence as ViolenceMetric,
    ViolenceGraphic as ViolenceGraphicMetric
)
_feedbacks = [ViolenceMetric(), ViolenceGraphicMetric()]

Violence = TestSet(ViolencePromptSet, _feedbacks, name="Violence")