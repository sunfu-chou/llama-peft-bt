import os
import time

from openai import OpenAI
from tqdm import tqdm

NUM_TREE = 5
NUM_DESCRIPTION = 50

client = OpenAI()

base_path = "data/object_navigation"
instruction_path = os.path.join(base_path, "prompt-self-instruct", "instruction.txt")
input_path = os.path.join(base_path, "prompt-self-instruct", "input.txt")
tree_path = os.path.join(base_path, "tree")

with open(instruction_path, "r", encoding="utf-8") as file:
    instruction_content = file.read()

with open(input_path, "r", encoding="utf-8") as file:
    input_content = file.read()


def generate_output(tree_file, output_dir, output_filename):
    with open(tree_file, "r", encoding="utf-8") as file:
        tree_content = file.read()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instruction_content},
            {"role": "user", "content": f"{input_content}\n{tree_content}"},
        ],
    )
    output_content = completion.choices[0].message.content
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, output_filename)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(output_content)


for i in tqdm(range(NUM_TREE)):
    tree_file = os.path.join(tree_path, f"{i}.txt")
    output_dir = os.path.join(base_path, "description", str(i))
    for j in tqdm(range(NUM_DESCRIPTION), leave=False):
        generate_output(tree_file, output_dir, f"{j}.txt")
