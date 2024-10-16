from wordSummerizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from wordSummerizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from wordSummerizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
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



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"Started {STAGE_NAME}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"Started {STAGE_NAME}")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.exception(e)
    raise e
