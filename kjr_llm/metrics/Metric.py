"""
This module defines the `Metric` class, which is a base class for creating custom metrics that can be used to evaluate the performance of language models or RAG applications.
The class provides methods to generate feedback based on different providers such as OpenAI and LiteLLM (llama3).
"""

from trulens_eval.feedback.provider import OpenAI, LiteLLM
from trulens_eval import Feedback

class Metric:
    """
    A base class for defining custom metrics to evaluate language models or RAG applications.
    """
    # Private attributes to hold instances of the OpenAI and LiteLLM providers.
    _provider_openai = None
    _provider_llama3 = None
    _provider_deepseek = None

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Metric class.

        :param args: Variable length argument list.
        :param kwargs: Arbitrary keyword arguments.
        """
        self.args = args
        self.kwargs = kwargs

        self._feedback = None
        self._feedback_fn = None

    def __feedback(self, provider):
        """
        Generates a feedback object using the specified provider.

        :param provider: The feedback provider to use.
        :return: A Feedback object.
        """
        feedback_metric = getattr(provider, self.feedback_name)
        return Feedback(feedback_metric, *self.args, **self.kwargs)

    def _feedback_with_selector(self, feedback):
        """
        Applies a feedback selector to the feedback object. This method is intended to be overridden in subclasses.

        :param feedback: The feedback object to apply the selector to.
        :return: The feedback object with the selector applied.
        """
        raise NotImplementedError()
        # Example implementation:
        # return (
        #     feedback
        #     .on_input_output()
        # )

    @property
    def feedback_name(self):
        """
        The name of the feedback metric. This property should be overridden in subclasses.
        """
        raise NotImplementedError()

    @property
    def openai(self):
        """
        Generates a feedback object using the OpenAI provider.

        :return: A Feedback object with the OpenAI provider.
        """
        feedback = self.__feedback(self.provider_openai)
        return self._feedback_with_selector(feedback)

    @property
    def llama3(self):
        """
        Generates a feedback object using the LiteLLM (llama3) provider.

        :return: A Feedback object with the LiteLLM (llama3) provider.
        """
        feedback = self.__feedback(self.provider_llama3)
        return self._feedback_with_selector(feedback)
    
    @property
    def deepseek(self):
        """
        Generates a feedback object using the LiteLLM (deepseek) provider.

        :return: A Feedback object with the LiteLLM (deepseek) provider.
        """
        feedback = self.__feedback(self.provider_deepseek)
        return self._feedback_with_selector(feedback)

    @property
    def provider_openai(self):
        """
        Gets or initializes the OpenAI provider.

        :return: The OpenAI provider.
        """
        if self._provider_openai is None:
            self._provider_openai = OpenAI()
        return self._provider_openai

    @property
    def provider_llama3(self):
        """
        Gets or initializes the LiteLLM (llama3) provider.

        :return: The LiteLLM (llama3) provider.
        """
        if self._provider_llama3 is None:
            self._provider_llama3 = LiteLLM()
            self._provider_llama3.model_engine = "ollama/llama3"
            self._provider_llama3.completion_args = {
                "api_base": "http://localhost:11434"
            }
        return self._provider_llama3
    
    @property
    def provider_deepseek(self):
        """
        Gets or initializes the LiteLLM (deepseek) provider.

        :return: The LiteLLM (deepseek) provider.
        """
        if self._provider_deepseek is None:
            self._provider_deepseek = LiteLLM()
            self._provider_deepseek.model_engine = "deepseek/deepseek-chat"
        return self._provider_deepseek