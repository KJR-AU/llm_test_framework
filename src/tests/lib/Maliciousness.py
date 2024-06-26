from ..TestSet import TestSet
from ...prompts.lib import MaliciousnessPromptSet
from ...metrics import Maliciousness as MaliciousnessMetric

_feedbacks = [MaliciousnessMetric()]

Maliciousness = TestSet(MaliciousnessPromptSet, _feedbacks, name="Maliciousness")