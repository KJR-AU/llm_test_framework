from trulens_eval.feedback.provider import Provider


class FeedbackProvider:
    def __init__(self, name: str, model_name: str):
        self._name: str = name
        self._model_name: str = model_name

    @property
    def name(self) -> str:
        return self._name

    @property
    def model_name(self) -> str:
        return self._model_name

    @model_name.setter
    def model_name(self, model_name: str) -> None:
        self._model_name = model_name

    @property
    def provider(self) -> Provider:
        raise NotImplementedError()
