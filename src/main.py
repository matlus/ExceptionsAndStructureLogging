import logging

from opencensus.ext.azure.log_exporter import AzureLogHandler

from application_base_exception import ApplicationBaseException
from application_logger import ApplicationLogger
from music_processor import MusicProcessor


def main():
    # Configure the logger
    logger = logging.getLogger(__name__)
    logger.addHandler(
        AzureLogHandler(
            connection_string="InstrumentationKey=482f6ac8-de27-4cdf-ac3f-80c743b787d0;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/;ApplicationId=0c23274f-b6fb-4780-b382-9e21d11f7a3a"
        )
    )
    application_logger = ApplicationLogger(logger)

    try:
        mp3_path_and_filename = (
            "C:\\Users\\user\\Music\\My Head (Can't Get You Out).mp3"
        )
        music_processor = MusicProcessor()
        music_processor.process_music_metadata(mp3_path_and_filename)
    except ApplicationBaseException as e:
        e.add_contextual_data({"NewCustomKey1": "CustomValue1", "NewCustomKey2": 2})
        application_logger.log_exception(e)


if __name__ == "__main__":
    main()
