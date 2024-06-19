import uuid
from trulens_eval import TruChain, TruLlama, Feedback
from ..targets import Target, LangChainTarget, LlamaIndexTarget
from ..prompts.PromptSet import PromptSet
from typing import List
from .UnknownTargetException import UnknownTargetException

# Class to represent a test set for evaluating targets
class TestSet:

    # Constructor for the TestSet class
    def __init__(self, prompts: PromptSet, feedbacks: List[Feedback], name: str = ""):
        """
        Initializes a TestSet instance.

        Args:
            prompts (PromptSet): A set of prompts to be used in the evaluation.
            feedbacks (List[Feedback]): A list of feedback functions to be used in the evaluation.
            name (str, optional): The name of the test set. Defaults to an empty string.
        """
        # Store the prompts, feedbacks, and name as instance variables
        self.prompts: PromptSet = prompts
        self.feedbacks: List[Feedback] = feedbacks
        self.name = name

    # Method to evaluate a target using the test set's prompts and feedbacks
    def evaluate(self, target: Target, app_id: str | None = None, reset_database: bool = False):
        """
        Evaluates the target using the prompts and feedbacks defined in the TestSet.

        Args:
            target (Target): The target to be evaluated, which can be either a LangChainTarget or LlamaIndexTarget.
            app_id (str | None, optional): The application ID to be used for recording. If None, a new UUID will be generated. Defaults to None.
            reset_database (bool, optional): Whether to reset the database before evaluation. Defaults to False.

        Raises:
            UnknownTargetException: If the target is not an instance of LangChainTarget or LlamaIndexTarget.

        Returns:
            recording: The recording object containing the evaluation results.
        """
        
        # Reset the database if reset_database is True
        if reset_database:
            self.reset_database()

        # Generate a new UUID if app_id is None
        if app_id is None:
            app_id = uuid.uuid4().hex
        
        # Check if the target is either a LangChainTarget or LlamaIndexTarget, otherwise raise an exception
        if not isinstance(target, (LangChainTarget, LlamaIndexTarget)):
            raise UnknownTargetException()

        # Define a dictionary to map target types to their corresponding recorder classes
        recorders = {
            LangChainTarget: TruChain,
            LlamaIndexTarget: TruLlama
        }
        
        # Get the appropriate recorder class based on the type of the target
        recorder_class = recorders.get(type(target))
        
        # Create an instance of the recorder class, passing the target's chain, app_id, and feedbacks
        recorder = recorder_class(target.chain, app_id=app_id, feedbacks=self.feedbacks)

        # Use the recorder in a context manager to record the evaluation process
        with recorder as recording:
            # Iterate over each prompt in the prompts set
            for prompt in self.prompts:
                # Invoke the target with the prompt's input and get the response
                response = target.invoke(prompt.input)
        
        # Return the recording object containing the evaluation results
        return recording