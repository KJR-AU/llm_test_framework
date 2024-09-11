import requests
from trulens_eval.tru_custom_app import instrument

from .target import Target


class EndpointTarget(Target):
    def __init__(
        self,
        endpoint_url: str,
        content_type: str = "application/json",
        prompt_key: str = "prompt",
        additional_args: dict[str, str] | None = None,
    ):
        self._endpoint_url: str = endpoint_url
        self._content_type: str = content_type
        self._prompt_key: str = prompt_key
        if additional_args is None:
            additional_args = {}
        self._additional_args: dict[str, str] = additional_args

    @property
    def endpoint_url(self) -> str:
        return self._endpoint_url

    @property
    def content_type(self) -> str:
        return self._content_type

    @property
    def prompt_key(self) -> str:
        return self._prompt_key

    @property
    def additional_args(self) -> dict[str, str]:
        return self._additional_args

    @instrument
    def invoke(self, prompt: str, timeout: int = 60) -> str:
        """Invoke the endpoint with a prompt and return the response."""
        headers = {"Content-Type": self.content_type}
        body = {self.prompt_key: prompt, **self.additional_args}
        response = requests.post(self.endpoint_url, json=body, headers=headers, timeout=timeout)
        ok_status: int = 200
        if not response.status_code == ok_status:
            msg: str = f"Endpoint request failed with status code: {response.status_code}"
            raise Exception(msg)
        return str(response.json()["response"])
