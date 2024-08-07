import uuid
import webbrowser

import pandas as pd
from trulens_eval import Tru
from trulens_eval.app import App as TrulensApp
from trulens_eval.schema.record import Record
from trulens_eval.utils.serial import Lens


class App:
    def __init__(self, app_name: str | None = None, context: object | None = None, reset_database: bool = False):
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

    def reset_database(self) -> None:
        """
        Reset the database associated with the Tru instance.
        """
        self.tru.reset_database()

    def set_context(self, llm_application: object) -> Lens:
        """
        Set the context for the LLM application.

        Args:
            llm_application (str): The LLM application context to set.

        Returns:
            The result of selecting the context for the LLM application.
        """
        return TrulensApp.select_context(llm_application)

    def run_dashboard(self, port: int = 8501, open_in_browser: bool = True) -> None:
        """
        Run the dashboard associated with the Tru instance.
        """
        self.tru.run_dashboard()
        if open_in_browser:
            webbrowser.open(f"http://localhost:{port}", new=0, autoraise=True)

    def get_records_and_feedback(self, app_ids: list[str] | None = None) -> tuple[pd.DataFrame, list[str]]:
        """
        Retrieve records and feedback for the specified application IDs.

        Args:
            app_ids (list): A list of application IDs for which to retrieve records and feedback.

        Returns:
            The records and feedback for the specified application IDs.
        """
        if app_ids is None:
            app_ids = []
        rtn: tuple[pd.DataFrame, list[str]] = self.tru.get_records_and_feedback(app_ids)
        return rtn

    def stop_dashboard(self) -> None:
        """
        Stop the dashboard associated with the Tru instance.
        """
        self.tru.stop_dashboard()

    def start_evaluator(self) -> None:
        """
        Start the evaluator associated with the Tru instance.
        """
        self.tru.start_evaluator()

    def stop_evaluator(self) -> None:
        """
        Stop the evaluator associated with the Tru instance.
        """
        self.tru.stop_evaluator()

    def get_leaderboard(self, app_ids: list[str] | None = None) -> pd.DataFrame:
        """
        Retrieve the leaderboard for the specified application IDs.

        Args:
            app_ids (list): A list of application IDs for which to retrieve the leaderboard.

        Returns:
            The leaderboard for the specified application IDs.
        """
        if app_ids is None:
            app_ids = []
        return self.tru.get_leaderboard(app_ids)

    def export_result_to_file(
        self, result: list[Record] | None = None, app_ids: list[str] | None = None, filename: str = ""
    ) -> None:
        if result is None:
            result = []

        coerced_app_ids = [] if app_ids is None else app_ids

        # Wait for all feedback to finish
        for test_result in result:
            for item in test_result:
                item.wait_for_feedback_results()

        record, feedback = self.get_records_and_feedback(coerced_app_ids)
        print("Finished evaluation")

        coerced_app_ids = record.app_id.unique()

        prepare_filename = self.app_name if filename == "" else filename
        export_filename = "data" if prepare_filename == "" else prepare_filename

        with pd.ExcelWriter(f"{export_filename}.xlsx") as writer:
            counter = 0
            for app_id in coerced_app_ids:
                id_record = record[record["app_id"] == app_id]
                id_record.drop(
                    columns=[
                        "app_json",
                        "type",
                        "record_id",
                        "record_json",
                        "cost_json",
                        "perf_json",
                        "total_tokens",
                        "total_cost",
                    ],
                    inplace=True,
                )
                id_record.dropna(how="all", axis=1, inplace=True)
                feedback_name = app_id.replace(f"{self.app_name}-", "")
                max_length = 31
                sheetname = feedback_name if len(feedback_name) < max_length else "sheet" + str(counter)
                column_to_move = id_record.pop("ts")
                id_record.insert(len(id_record.columns), "ts", column_to_move)
                id_record.to_excel(writer, sheet_name=sheetname)
