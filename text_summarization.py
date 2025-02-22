# -*- coding: utf-8 -*-
"""Text_Summarization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11X4k95Hskc5CiXxAljhGEtKSP--6bBYn
"""

!nvidia-smi

!pip install transformers[sentencepiece] datasets sacrebleu rouge_score py7zr -q

!pip install --upgrade accelerate
!pip uninstall -y transformers accelerate
!pip install transformers accelerate

from transformers import pipeline, set_seed
from datasets import load_dataset, load_from_disk
import matplotlib.pyplot as plt
from datasets import load_dataset
import pandas as pd
from datasets import load_dataset, load_metric

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

import nltk
from nltk.tokenize import sent_tokenize

from tqdm import tqdm
import torch
import pickle


nltk.download("punkt")

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

device = "cuda" if torch.cuda.is_available() else "cpu"
device

model_ckpt = "google/pegasus-cnn_dailymail"

tokenizer = AutoTokenizer.from_pretrained(model_ckpt)

model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt).to(device)

#dowload & unzip data

!wget https://github.com/anubhav-05/ConciseAI/blob/main/summarizer-data.zip
!unzip summarizer-data.zip

dataset_samsum = load_from_disk('samsum_dataset')
dataset_samsum

split_lengths = [len(dataset_samsum[split])for split in dataset_samsum]

print(f"Split lengths: {split_lengths}")
print(f"Features: {dataset_samsum['train'].column_names}")
print("\nDialogue:")

print(dataset_samsum["test"][1]["dialogue"])

print("\nSummary:")

print(dataset_samsum["test"][1]["summary"])

def convert_examples_to_features(example_batch):
    input_encodings = tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )

    with tokenizer.as_target_tokenizer():
        target_encodings = tokenizer(example_batch['summary'], max_length = 128, truncation = True )

    return {
        'input_ids' : input_encodings['input_ids'],
        'attention_mask': input_encodings['attention_mask'],
        'labels': target_encodings['input_ids']
    }

dataset_samsum_pt = dataset_samsum.map(convert_examples_to_features, batched = True)

dataset_samsum_pt["train"]

# Training

from transformers import DataCollatorForSeq2Seq

seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

from transformers import TrainingArguments, Trainer

trainer_args = TrainingArguments(
    output_dir='pegasus-samsum', num_train_epochs=1, warmup_steps=500,
    per_device_train_batch_size=1, per_device_eval_batch_size=1,
    weight_decay=0.01, logging_steps=10,
    evaluation_strategy='steps', eval_steps=400, save_steps=1e6,
    gradient_accumulation_steps=16
)

trainer = Trainer(model=model_pegasus, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["train"],
                  eval_dataset=dataset_samsum_pt["validation"])

trainer.train()

# Save the model using pickle
torch.save(model_pegasus.state_dict(),'model_state_dict.pth')

print("Model saved as trained_model.pkl")

!zip -r pegasus-samsum.zip pegasus-samsum

from google.colab import drive
drive.mount('/content/drive')

# Copy files to Google Drive
!cp model_state_dict.pth /content/drive/MyDrive/
!cp pegasus-samsum.zip /content/drive/MyDrive/