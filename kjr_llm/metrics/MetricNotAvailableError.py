# Define a custom exception class named MetricNotAvailableError that inherits from the built-in Exception class

class MetricNotAvailableError(Exception):
    """
    A custom exception class to indicate that a required metric is not available for evaluation.
    """
    pass