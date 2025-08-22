from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

model_name = 'gemma-2b'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def format(example):

Question: {example['question']}

    example['text'] = prompt + ' ' + example['answer']
    return example

dataset = load_dataset('json', data_files='data/train.jsonl')['train'].map(format)
tokenized = dataset.map(lambda e: tokenizer(e['text'], truncation=True, padding='max_length'), batched=True)

args = TrainingArguments(
    output_dir='outputs',
    per_device_train_batch_size=2,
    num_train_epochs=3,
    logging_steps=10,
    save_steps=50,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized,
    data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
)

trainer.train()
