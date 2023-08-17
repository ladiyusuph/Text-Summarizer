from txtSummarizer.constants import *
from txtSummarizer.utils.common import read_yaml, create_directory
from txtSummarizer.entity import (DataIngestionConfig, 
                                  DataValidationConfig,
                                  DataTransformationConfig,
                                  ModelTrainingConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directory([self.config.artifacts_root])

    def get_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directory([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directory([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            ALL_REQUIRED_FILES= config.ALL_REQUIRED_FILES,
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directory([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path= config.data_path,
            tokenizer_name= config.tokenizer_name,
        )

        return data_transformation_config

    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        params = self.params.TrainingArguments

        create_directory([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir = config.root_dir,
            data_path= config.data_path,
            model_ckpt= config.model_ckpt,
            num_train_epochs= params.num_train_epochs,
            warmup_steps= params.warmup_steps,
            per_device_train_batch_size= params.per_device_train_batch_size,
            weight_decay= params.weight_decay,
            logging_steps= params.logging_steps,
            evaluation_strategy= params.evaluation_strategy,
            eval_steps= params.eval_steps,
            save_steps= params.save_steps,
            gradient_accumulation_steps= params.gradient_accumulation_steps,
        )

        return model_training_config