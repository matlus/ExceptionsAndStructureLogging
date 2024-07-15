import logging
from enum import Enum


class LogEvent(Enum):
    pass


class ApplicationBaseException(Exception):
    CUSTOM_DIEMENSIONS: str = "custom_dimensions"

    def __init__(
        self, message: str, log_event: LogEvent, **context_data: dict[str, any]
    ):
        """Initializes a new instance of the ExceptionBase class.
        message: The error message.
        log_event: The LogEvent step in the process being attempted when the exception occurred.
        context_data: Additional contextual data you want associated with the exception. This data will be included in the custom_dimensions property and logged.
        """
        super().__init__(message)
        self.__log_event = log_event
        self.__contextual_data = self.__build_contextual_data(context_data)

    def __build_contextual_data(
        self, context_data: dict[str, any]
    ) -> dict[str, dict[str, any]]:
        """Builds the contextual_data dictionary with additional context."""
        contextual_data = {
            "LogEvent": self.log_event.value,
            "Severity": self.get_severity_str(self.severity),
            "Reason": self.reason,
            "HttpStatusCode": self.http_status_code,
            **context_data,
        }
        return {self.CUSTOM_DIEMENSIONS: contextual_data}

    @property
    def log_event(self) -> LogEvent:
        return self.__log_event

    @property
    def contextual_data(self) -> dict[dict[str, any]]:
        return self.__contextual_data

    def add_contextual_data(self, value: dict[str, any]) -> None:
        return self.__contextual_data[self.CUSTOM_DIEMENSIONS].update(value)

    @property
    def severity(self) -> int:
        return logging.ERROR

    @property
    def reason(self) -> str:
        return "An error occurred"

    @property
    def http_status_code(self) -> int:
        return 400

    @staticmethod
    def get_severity_str(severity_level: int) -> str:
        match severity_level:
            case 0:
                return "NotSet"
            case 10:
                return "Debug"
            case 20:
                return "Information"
            case 30:
                return "Warning"
            case 40:
                return "Error"
            case 50:
                return "Critical"
            case _:
                raise ValueError(
                    f"Invalid severity level: {severity_level}. Possible values are 0, 10, 20, 30, 40, 50."
                )
