from txtSummarizer.config.configuration import ConfigurationManager
from txtSummarizer.components.model_training import ModelTraining
from txtSummarizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        model_training_pipeline = ModelTraining(config=model_training_config)
        model_training_pipeline.train()