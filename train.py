import torch
from transformers import AutoTokenizer, BartForConditionalGeneration, Seq2SeqTrainer, Seq2SeqTrainingArguments

# Tải mô hình BART pre-trained và tokenizer
from transformers import  AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("VietAI/vit5-base")  
model = AutoModelForSeq2SeqLM.from_pretrained("VietAI/vit5-base")

import pandas as pd
from datasets import Dataset

# Đọc file CSV bằng pandas
df_train = pd.read_csv("datasetafter.csv")
df_test = pd.read_csv("datasetafter.csv")


# Chuyển đổi sang định dạng Dataset
train_dataset = Dataset.from_pandas(df_train)
test_dataset = Dataset.from_pandas(df_test)


# Tiền xử lý dữ liệu
def preprocess_data(dataset):
    def preprocess_function(examples):
        inputs = examples["Content"] 
        model_inputs = tokenizer(inputs, max_length=512, padding="max_length", truncation=True)

        with tokenizer.as_target_tokenizer():
            labels = tokenizer(examples["Summary"], max_length=150, padding="max_length", truncation=True)
        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    return dataset.map(preprocess_function, batched=True)


# Áp dụng tiền xử lý cho dataset
tokenized_train_dataset = preprocess_data(train_dataset)
tokenized_test_dataset = preprocess_data(test_dataset)


# Cấu hình tham số huấn luyện
training_args = Seq2SeqTrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=3,
    predict_with_generate=True,
    fp16=True,
    logging_dir='./logs',
)

# Tạo Trainer để huấn luyện mô hình
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_test_dataset,
    tokenizer=tokenizer,
)


# Huấn luyện mô hình
trainer.train()

# Lưu mô hình sau khi huấn luyện
model.save_pretrained("./bart_summarization_model")
tokenizer.save_pretrained("./bart_summarization_model")
