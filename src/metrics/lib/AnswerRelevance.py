from ..Metric import Metric

class AnswerRelevance(Metric):
    
    def __init__(self):
        super().__init__(name="Answer Relevance")


    def _feedback_with_selector(self, feedback):
        return (
            feedback
            .on_input_output()
        )


    @property
    def feedback_name(self):
        return "relevance_with_cot_reasons"