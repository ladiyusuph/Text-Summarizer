import os
from txtSummarizer.logging import logging
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from txtSummarizer.entity import DataTransformationConfig

#Component
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    #converting data to features
    def convert_examples_to_features(self, example_batch):
        input_encodings =self.tokenizer(example_batch['dialogue'] , max_length = 512,
                                    truncation = True )

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128,
                                        truncation = True )

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    def convert(self):
        samsum_data = load_from_disk(self.config.data_path)
        tokenized_samsum = samsum_data.map(self.convert_examples_to_features, batched = True)
        tokenized_samsum.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))