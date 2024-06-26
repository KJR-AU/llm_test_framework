from ..TestSet import TestSet
from ...prompts.lib import HarassmentPromptSet
from ...metrics import (
    Harassment as HarassmentMetric,
    HarassmentThreatening as HarassmentThreateningMetric
)

_feedbacks = [HarassmentMetric(), HarassmentThreateningMetric()]

Harassment = TestSet(HarassmentPromptSet, _feedbacks, name="Harassment")