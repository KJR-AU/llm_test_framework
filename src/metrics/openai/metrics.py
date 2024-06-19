from trulens_eval import Feedback  # Import the Feedback class from the trulens_eval module.
from trulens_eval.feedback.provider import OpenAI, LiteLLM  # Import the OpenAI and LiteLLM classes from the trulens_eval.feedback.provider module.

provider = OpenAI()  # Initialize an instance of the OpenAI provider.
# can also change model by setting model engine: OpenAI(model_engine="gpt-3.5-turbo")

import numpy as np  # Import the numpy library for numerical operations.

def ContextRelevance(context):
    """
    Define a function to evaluate the relevance of the context using the provider's context_relevance_with_cot_reasons method.
    
    Args:
        context: The context to be evaluated.
    
    Returns:
        A Feedback instance configured to evaluate context relevance and aggregate the results using the mean.
    """
    return (
        Feedback(provider.context_relevance_with_cot_reasons, name="Context Relevance")
        .on_input()
        .on(context)  # Apply the feedback function to the provided context.
        .aggregate(np.mean)  # Aggregate the results using the mean.
    )

print(vars(provider))  # Print the attributes of the provider instance.

# Define Feedback instances for various attributes, each configured to evaluate either input-output or output and named accordingly.
Relevance = (
    Feedback(provider.relevance, name="Relevance")
    .on_input_output()
)

Hate = (
    Feedback(
        provider.moderation_hate,
        name="Hate", # Name is set to Hate
        higher_is_better=False, # Score is high when it has high hate.
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