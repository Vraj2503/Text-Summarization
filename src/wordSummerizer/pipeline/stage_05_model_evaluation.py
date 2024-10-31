from wordSummerizer.config.configuration import ConfigurationManager
from wordSummerizer.components.model_evaluation import ModelEvaluation
from wordSummerizer.logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(model_evaluation_config)
        model_evaluation_config.evaluate()
        
