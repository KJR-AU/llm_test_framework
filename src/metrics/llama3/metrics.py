from trulens_eval import Feedback  # Import the Feedback class from the trulens_eval module.
from trulens_eval.feedback.provider import LiteLLM  # Import the LiteLLM class from the trulens_eval.feedback.provider module.

# Initialize a LiteLLM provider instance.
provider = LiteLLM()

# Set the model engine to "ollama/llama3".
provider.model_engine = "ollama/llama3"

# Configure the completion arguments for the provider, specifying the API base URL.
provider.completion_args = {
    "api_base": "http://localhost:11434"
}

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

# Define a Feedback instance for evaluating relevance based on input and output.
Relevance = (
    Feedback(provider.relevance, name="Relevance")
    .on_input_output()
)

# Define Feedback instances for various attributes, each configured to evaluate the output and named accordingly.
Maliciousness = (
    Feedback(
        provider.maliciousness_with_cot_reasons,
        name="Maliciousness", # Name is set to Maliciousness
        higher_is_better=False, # Score is high when it is very malicious.
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

Coherence = (
    Feedback(
        provider.coherence,
        name="Coherence"
    ).on_output()
)

CoherenceWithCotReasons = (
    Feedback(
        provider.coherence_with_cot_reasons,
        name="Coherence with cot reasons"
    ).on_output()
)

