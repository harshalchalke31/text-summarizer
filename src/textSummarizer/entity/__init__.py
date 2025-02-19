from dataclasses import dataclass
from pathlib import Path
from typing import List

# create entity
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:str
    ALL_REQUIRED_FILES:list
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    TOKENIZER: Path

# @dataclass(frozen=True)
# class ModelTrainerConfig:
#   root_dir: Path
#   data_path: Path
#   model_ckpt: Path
#   num_train_epochs: int
#   warmup_steps: int
#   per_device_train_batch_size: int
#   weight_decay: float
#   logging_steps: int
#   evaluation_strategy: str
#   eval_steps: int
#   save_steps: float
#   gradient_accumulation_steps: int 

@dataclass(frozen=True)
class ModelTrainerConfig:
  root_dir: Path
  data_path: Path
  model_ckpt: Path
  num_train_epochs: int
  warmup_steps: int
  per_device_train_batch_size: int
  weight_decay: float
  logging_steps: int
  evaluation_strategy: str
  eval_steps: int
  save_steps: float
  gradient_accumulation_steps: int
  #updated
  learning_rate: float
  save_total_limit: int
  load_best_model_at_end: bool
  metric_for_best_model: str
  fp16: bool
  report_to: List[str]

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file: Path