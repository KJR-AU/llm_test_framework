from trulens_eval.feedback.provider import OpenAI, LiteLLM
from trulens_eval import Feedback

class Metric:

    _provider_openai = None
    _provider_llama3 = None

    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs

        self._feedback = None
        self._feedback_fn = None

    def __feedback(self, provider):
        feedback_metric = getattr(provider, self.feedback_name)
        return Feedback(feedback_metric, *self.args, **self.kwargs)


    def _feedback_with_selector(self, feedback):
        raise NotImplementedError()
        # return (
        #     feedback
        #     .on_input_output()
        # )
    
    @property
    def feedback_name(self):
        raise NotImplementedError()

    @property
    def openai(self):
        feedback = self.__feedback(self.provider_openai)
        return self._feedback_with_selector(feedback)

    @property
    def llama3(self):
        feedback = self.__feedback(self.provider_llama3)
        return self._feedback_with_selector(feedback)

    @property
    def provider_openai(self):
        if self._provider_openai is None:
            self._provider_openai = OpenAI()
        return self._provider_openai

    @property
    def provider_llama3(self):
        if self._provider_llama3 is None:
            self._provider_llama3 = LiteLLM()
            self._provider_llama3.model_engine = "ollama/llama3"
            self._provider_llama3.completion_args = {
                "api_base": "http://localhost:11434"
            }