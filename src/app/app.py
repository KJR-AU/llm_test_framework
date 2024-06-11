from trulens_eval import Tru
from trulens_eval.app import App as trulens_app
import uuid

class App:
    def __init__(self, app_name: str | None = None):
        self.tru = Tru()
        self.app_name = app_name if app_name else uuid.uuid4().hex

    def reset_database(self):
        self.tru.reset_database()

    def set_context(self, llm_application: str):
        return trulens_app.select_context(llm_application)

    def run_dashboard(self):
        self.tru.run_dashboard()

