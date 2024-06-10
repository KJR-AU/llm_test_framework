from trulens_eval import Feedback
from trulens_eval.feedback.provider import OpenAI, LiteLLM

provider = LiteLLM()
provider.model_engine = "ollama/llama3"
provider.completion_args = {
    "api_base": "http://localhost:11434"
}

import numpy as np

def ContextRelevance(context):
    return (
        Feedback(provider.context_relevance_with_cot_reasons)
        .on_input()
        .on(context)  # Refers to context defined from `select_context`
        .aggregate(np.mean)
    )

Relevance = (
    Feedback(provider.relevance)
    .on_input_output()
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

Controversiality = (
    Feedback(
        provider.controversiality_with_cot_reasons,
        name="Controversiality",
        higher_is_better=False,
    ).on_output()
)