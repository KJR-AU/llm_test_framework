from ..TestSet import TestSet
from ...prompts.lib import HatePromptSet
from ...metrics import Hate as HateMetric

_feedbacks = [HateMetric()]

Hate = TestSet(HatePromptSet, _feedbacks, name="Hate")