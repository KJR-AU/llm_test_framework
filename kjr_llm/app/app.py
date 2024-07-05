from trulens_eval import Tru  # Import the Tru class from the trulens_eval module.
from trulens_eval.app import App as trulens_app  # Import the App class from the trulens_eval.app module and alias it as trulens_app.
import uuid  # Import the uuid module for generating unique identifiers.

class App:
    def __init__(self, app_name: str | None = None, context = None, reset_database: bool = False):
        """
        Initialize the App instance.
        
        Args:
            app_name (str | None): The name of the application. If not provided, a unique identifier will be generated.
        """
        self.tru = Tru()  # Create an instance of the Tru class.
        if reset_database:
            self.reset_database()
        if context:
            self.set_context(context)
        self.app_name = app_name if app_name else uuid.uuid4().hex  # Set the application name, generating a unique identifier if none is provided.

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

