from ..TestSet import TestSet
from ...prompts.lib import SelfHarmPromptSet
from ...metrics import SelfHarm as SelfHarmMetric

_feedbacks = [SelfHarmMetric()]

SelfHarm = TestSet(SelfHarmPromptSet, _feedbacks, name="Self Harm")