from datasets import load_dataset

with open("data/dataset.json", "r", encoding="utf-8") as file:
    print(file.read())

dataset = load_dataset("json", data_files="data/dataset.json")
dataset.push_to_hub("sunfu-chou/symbolic-bt")
