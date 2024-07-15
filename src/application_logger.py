import inspect
import logging

from application_base_exception import ApplicationBaseException


class ApplicationLogger:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def log_exception(self, exception: ApplicationBaseException):
        calling_function = inspect.stack()[1].function
        contextual_information = exception.contextual_data["custom_dimensions"]
        self.logger.log(
            exception.severity,
            "Exception caught in function: '%s' - Message: %s. Contextual Information: %s",
            calling_function,
            exception,
            contextual_information,
            exc_info=exception,
            stack_info=False,
            extra=exception.contextual_data,
        )
