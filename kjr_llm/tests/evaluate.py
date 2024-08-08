import uuid

from trulens_eval import Feedback, Tru, TruChain, TruLlama

from ..exceptions.unknown_target_error import UnknownTargetError
from ..prompts.prompt_set import PromptSet
from ..targets import LangChainTarget, LlamaIndexTarget, Target


def evaluate(
    target: Target,
    prompts: PromptSet,
    feedbacks: list[Feedback],
    app_id: str | None = None,
    reset_database: bool = True,
) -> None:
    """
    Evaluates a given target using a set of prompts and feedbacks, and optionally resets the database.

    Args:
        target (Target): The target to be evaluated, which can be either a LangChainTarget or LlamaIndexTarget.
        prompts (PromptSet): A set of prompts to be used for evaluation.
        feedbacks (List[Feedback]): A list of feedbacks to be used for evaluation.
        app_id (str | None, optional): The application ID. If None, a new UUID will be generated. Defaults to None.
        reset_database (bool, optional): Whether to reset the database before evaluation. Defaults to True.

    Raises:
        UnknownTargetException: If the target is not an instance of LangChainTarget or LlamaIndexTarget.
    """
    # If no app_id is provided, generate a new UUID and convert it to a hexadecimal string
    if app_id is None:
        app_id = uuid.uuid4().hex

    # Check if the target is either a LangChainTarget or LlamaIndexTarget, otherwise raise an exception
    if not isinstance(target, LangChainTarget | LlamaIndexTarget):
        raise UnknownTargetError()

    # Initialize the Tru object, which is used for managing the evaluation process
    tru = Tru()
    # Reset Tru object database
    tru.reset_database()

    # Define a dictionary to map target types to their corresponding recorder classes
    recorders = {LangChainTarget: TruChain, LlamaIndexTarget: TruLlama}

    # Get the appropriate recorder class based on the type of the target
    recorder_class: type | None = recorders.get(type(target))

    # Create an instance of the recorder class, passing the target's chain, app_id, and feedbacks
    if recorder_class is None:
        raise Exception()
    recorder: TruChain | TruLlama = recorder_class(target.app, app_id=app_id, feedbacks=feedbacks)

    # Use the recorder in a context manager to record the evaluation process
    with recorder as _:
        # Iterate over each prompt in the prompts set
        for prompt in prompts:
            # Invoke the target with the prompt's input and get the response
            _ = target.invoke(prompt.input)

    # Run the dashboard to visualize the evaluation results
    tru.run_dashboard()
