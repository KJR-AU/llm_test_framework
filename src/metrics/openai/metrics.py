from trulens_eval import Feedback
from trulens_eval.feedback.provider import OpenAI, LiteLLM

provider = OpenAI()

import numpy as np

def ContextRelevance(context):
    return (
        Feedback(provider.context_relevance_with_cot_reasons)
        .on_input()
        .on(context)  # Refers to context defined from `select_context`
        .aggregate(np.mean)
    )

print(vars(provider))


Relevance = (
    Feedback(provider.relevance)
    .on_input_output()
)

Hate = (
    Feedback(
        provider.moderation_hate,
        name="Hate",
        higher_is_better=False
    ).on_output()
)

SelfHarm = (
    Feedback(
        provider.moderation_selfharm,
        name="Self Harm",
        higher_is_better=False
    ).on_output()
)

Violence = (
    Feedback(
        provider.moderation_violence,
        name="Violent",
        higher_is_better=False
    ).on_output()
)

Harassment = (
    Feedback(
        provider.moderation_harassment, 
        name="Harassment", 
        higher_is_better=False
    ).on_output()
)

HarassmentThreatening = (
    Feedback(
        provider.moderation_harassment_threatening, 
        name="Harassment Threatening", 
        higher_is_better=False
    ).on_output()
)

Maliciousness = (
    Feedback(
        provider.maliciousness_with_cot_reasons,
        name="Maliciousness",
        higher_is_better=False,
    ).on_output()
)

Insensitivity = (
    Feedback(
        provider.insensitivity_with_cot_reasons,
        name="Insensitivity",
        higher_is_better=False,
    ).on_output()
)

Criminality = (
    Feedback(
        provider.criminality_with_cot_reasons,
        name="Criminality",
        higher_is_better=False,
    ).on_output()
)

ViolenceGraphic = (
    Feedback(
        provider.moderation_violencegraphic,
        name="Violent/Graphic",
        higher_is_better=False,
    ).on_output()
)

Controversiality = (
    Feedback(
        provider.controversiality_with_cot_reasons,
        name="Controversiality",
        higher_is_better=False,
    ).on_output()
)