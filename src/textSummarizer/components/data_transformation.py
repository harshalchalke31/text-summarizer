from textSummarizer.config.configuration import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
import os

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path=config.TOKENIZER)
    
    def extract_features(self,input_batch):
        input_encodings = self.tokenizer(input_batch['dialogue'],truncation=True,max_length=1024)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(input_batch['summary'],truncation=True,max_length=128)
        
        return {
            'input_ids':input_encodings['input_ids'],
            'attention_mask':input_encodings['attention_mask'],
            'labels':target_encodings['input_ids']
        }
    
    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt= dataset_samsum.map(self.extract_features,batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,'samsum_dataset'))

    