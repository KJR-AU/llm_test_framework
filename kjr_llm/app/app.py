from trulens_eval import Tru
from trulens_eval.app import App as trulens_app
import uuid
from typing import Any

class App:
    def __init__(self, app_name: str | None = None, context: Any = None, reset_database: bool = False):
        """
        Initialize the App instance.
        
        Args:
            app_name (str | None, optional): The name of the application. If not 
            provided, a unique identifier will be used.
            context (any, optional): Set the context of the application.
            reset_database (bool, optional): If True, reset the local sqlite database
            used to store test results.
        """
        self.tru = Tru() 
        if reset_database:
            self.reset_database()
        if context:
            self.set_context(context)

        # Generate a unique identifier if no app name is provided
        self.app_name = app_name if app_name else uuid.uuid4().hex  

    def reset_database(self):
        """
        Reset the database associated with the Tru instance.
        """
        self.tru.reset_database()

    def set_context(self, llm_application: str):
        """
        Set the context for the LLM application.
        
        Args:
            llm_application (str): The LLM application context to set.
        
        Returns:
            The result of selecting the context for the LLM application.
        """
        return trulens_app.select_context(llm_application)

    def run_dashboard(self):
        """
        Run the dashboard associated with the Tru instance.
        """
        self.tru.run_dashboard()

