from datasets import DatasetDict, load_dataset

# with open("data/dataset.json", "r", encoding="utf-8") as file:
#     print(file.read())

train_dataset = load_dataset("json", data_files="data/dataset.json")
test_dataset = load_dataset("json", data_files="data/object_navigation/dataset.json")

dataset = DatasetDict({
    "train": train_dataset["train"],
    "test": test_dataset["train"]
})

dataset.push_to_hub("sunfu-chou/symbolic-bt")
