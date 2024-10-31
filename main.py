from wordSummerizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from wordSummerizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from wordSummerizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from wordSummerizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from wordSummerizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
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

STAGE_NAME = "Model Training Stage"
 
try:
    logger.info(f"Started {STAGE_NAME}")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f"Started {STAGE_NAME}")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.exception(e)
    raise e