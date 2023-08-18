from txtSummarizer.config.configuration import ConfigurationManager
from txtSummarizer.components.model_evaluation import ModelEvaluation
from txtSummarizer.logging import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_pipeline = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_pipeline.evaluate()