from wordSummerizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from wordSummerizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Started {STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.exception(e)
    raise e
