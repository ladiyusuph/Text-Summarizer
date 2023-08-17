from txtSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from txtSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from txtSummarizer.logging import logger

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.error(f"stage {STAGE_NAME} failed with error: {e}")
    raise e

STAGE_NAME = 'Data Validation Stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.error(f"stage {STAGE_NAME} failed with error: {e}")
    raise e