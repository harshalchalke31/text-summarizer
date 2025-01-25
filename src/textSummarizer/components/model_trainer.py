import os
from textSummarizer.entity import ModelTrainerConfig

from transformers import Trainer, TrainingArguments, DataCollatorForSeq2Seq, AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        datacollator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

        # loading data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,  # Updated
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            learning_rate=float(self.config.learning_rate),        # New parameter
            save_total_limit=self.config.save_total_limit,  # New parameter
            load_best_model_at_end=self.config.load_best_model_at_end,  # New parameter
            metric_for_best_model=self.config.metric_for_best_model,    # New parameter
            fp16=self.config.fp16,                                   # New parameter
            report_to=self.config.report_to                           # New parameter
        )

        trainer = Trainer(
            model=model,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=datacollator,
            train_dataset=dataset_samsum_pt['test'],
            eval_dataset=dataset_samsum_pt['validation']
        )

        trainer.train()

        # Save final model and tokenizer
        model.save_pretrained(os.path.join(self.config.root_dir, "distilbart_model_01"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "distilbart_tokenizer_01"))
