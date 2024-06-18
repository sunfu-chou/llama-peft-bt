import json
import os

# 定義兩個 dataset.json 的路徑
dataset1_path = "data/visual_servoing/dataset.json"
dataset2_path = "data/inspection/dataset.json"

# 讀取 dataset1.json 的內容
with open(dataset1_path, "r", encoding="utf-8") as file:
    dataset1 = json.load(file)

# 讀取 dataset2.json 的內容
with open(dataset2_path, "r", encoding="utf-8") as file:
    dataset2 = json.load(file)

# 合併兩個 JSON 內容
merged_dataset = dataset1 + dataset2

# 定義合併後的輸出文件路徑
merged_output_path = "data/dataset.json"

# 將合併後的內容寫入新的 JSON 文件
with open(merged_output_path, "w", encoding="utf-8") as json_file:
    json.dump(merged_dataset, json_file, ensure_ascii=False, indent=4)

print(f"Merged JSON data written to {merged_output_path}")
print(f"Total number of data: {len(merged_dataset)}")