# llama-peft-bt

### Clone the repository

```bash
git clone --recurse-submodules git@github.com:sunfu-chou/llama-peft-bt.git
```

### Pull the docker image

```bash
docker pull sunfuchou/llama-peft-bt:ubuntu20.04-cuda12.1.1
```

### Run the docker container

```bash
source docker_run.sh
```

### Download the dataset

Run the following command in the docker container

```bash
huggingface-cli download sunfu-chou/symbolic-bt --repo-type dataset
```

### Generate the descriptions for the trees

Modify the task name in the [`generate_description.py`](generate_description.py) [#L12](https://github.com/sunfu-chou/llama-peft-bt/blob/master/generate_description.py#L12)

```python
base_path = "data/inspection"
```

Run the following command in the docker container

```bash
python3 generate_descriptions.py
```

### Convert the descriptions to the json format

Modify the datasets name in the [`convert_description_to_json.py`](convert_description_to_json.py) [#5](https://github.com/sunfu-chou/llama-peft-bt/blob/master/convert_description_to_json.py#L5)

```python
base_path = "data/inspection"
```

Run the following command in the docker container

```bash
python3 convert_description_to_json.py
```

### Merge the json files

Modify the task name in the [`merge_json_dataset.py`](merge_json_dataset.py) [#5](https://github.com/sunfu-chou/llama-peft-bt/blob/master/merge_json_dataset.py#L5)

```python
dataset1_path = "data/visual_servoing/dataset.json"
dataset2_path = "data/inspection/dataset.json"
```

Run the following command in the docker container

```bash
python3 merge_json_dataset.py
```

### Push the dataset to the huggingface

Modify the task name in the [`push_dataset_to_hub.py`](push_dataset_to_hub.py) [#3](https://github.com/sunfu-chou/llama-peft-bt/blob/master/push_dataset_to_hub.py#L3)

```python
train_dataset = load_dataset("json", data_files="data/dataset.json")
test_dataset = load_dataset("json", data_files="data/object_navigation/dataset.json")
```

Run the following command in the docker container

```bash
huggingface-cli login
```

```bash
python3 push_dataset_to_hub.py
```

### Finetune the model

Run the following command in the docker container

```bash
python3 ./alpaca-lora/finetune.py \
    --base_model 'meta-llama/Meta-Llama-3-8B' \
    --data_path 'sunfu-chou/symbolic-bt' \
    --output_dir './output-test' \
    --batch_size 500 \
    --micro_batch_size 10 \
    --num_epochs 100 \
    --learning_rate 1e-4 \
    --cutoff_len 1024 \
    --val_set_size 1 \
    --lora_r 8 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --lora_target_modules '[k_proj, q_proj, v_proj, o_proj, gate_proj, down_proj, up_proj]'
```

### Inference

Modify the input text in the [`inference.py`](inference.py) #L15

```python
input_text = "The behavior tree first checks if there is any object in view. If there is an object, it simultaneously executes control actions for linear x and linear y directions. If no object is in view, the robot will then proceed to explore a pattern block."
```

Run the following command in the docker container

```bash
python3 ./alpaca-lora/inference.py
```
