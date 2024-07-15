# Python sample code demonstrating Custom Exceptions and Structured Logging
### Application Base Exception
__init__ method arguments:
1. message - The Exception Message
2. log_event - This is a custom Enum, that is a descendant of `LogEvent`. Each Enum item is conceptually a processing Step in your code.

Properties Descendants MUST override in Code
  * severity
  * reason
  * http_status_code

### Sample Custom Exception
```python
class MusicMetadataException(ApplicationBaseException):
    def __init__(self, message: str, log_event: LogEvent, data):
        context_data = dc.asdict(data)
        super().__init__(message, log_event, **context_data)

    @property
    def severity(self) -> int:
        return logging.ERROR

    @property
    def reason(self) -> str:
        return "Music metadata processing error"

    @property
    def http_status_code(self) -> int:
        return 400
```

### Application Logger

### Music Metadata Exception
