from trulens_eval.feedback.provider import OpenAI, LiteLLM
from trulens_eval import Feedback

class Metric:
    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs

        self._feedback = None
        self._feedback_fn = None

    def __feedback(self, provider):
        feedback_metric = getattr(provider, self.feedback_name)
        return Feedback(feedback_metric, *self.args, **self.kwargs)


    def __feedback_with_selector(self, feedback):
        return (
            feedback
            .on_input_output()
        )
    
    @property
    def feedback_name(self):
        raise NotImplementedError()

    @property
    def openai(self):
        provider = OpenAI()
        feedback = self.__feedback(provider)
        return self.__feedback_with_selector(feedback)

    @property
    def llama3(self):
        provider = LiteLLM()
        provider.model_engine = "ollama/llama3"
        provider.completion_args = {
            "api_base": "http://localhost:11434"
        }
        feedback = self.__feedback(provider)
        return self.__feedback_with_selector(feedback)