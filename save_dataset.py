import json
import os

# Define paths
base_path = "data/inspection"
instruction_path = os.path.join(base_path, "prompt", "instruction.txt")
input_dir = os.path.join(base_path, "description")
output_dir = os.path.join(base_path, "tree")
print(f"base_path: {base_path}")
print(f"instruction_path: {instruction_path}")
print(f"input_dir: {input_dir}")
print(f"output_dir: {output_dir}")

# Read instruction content
with open(instruction_path, "r", encoding="utf-8") as file:
    instruction_content = file.read()

data = []
for i in range(5):
    # Read output content
    output_file = os.path.join(output_dir, f"{i}.txt")
    with open(output_file, "r", encoding="utf-8") as file:
        output_content = file.read()
    for j in range(50):
        # Read input content
        input_file = os.path.join(input_dir, str(i), f"{j}.txt")
        with open(input_file, "r", encoding="utf-8") as file:
            input_content = file.read()
        data.append(
            {
                "output": output_content,
                "instruction": instruction_content,
                "input": input_content,
            }
        )

json_file = os.path.join(base_path, "dataset.json")
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
