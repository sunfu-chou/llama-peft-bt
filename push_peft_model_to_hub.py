import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

prompt_template = ""
base_model = "meta-llama/Meta-Llama-3-8B"
model = AutoModelForCausalLM.from_pretrained(
    base_model,
    torch_dtype=torch.float16,
    device_map="auto",
)
lora_weights = "/home/arg/llama-peft-bt/output-test-2/"
model = PeftModel.from_pretrained(
    model,
    lora_weights,
    torch_dtype=torch.float16,
)
model.push_to_hub("sunfu-chou/symbolic-bt-lora-llama-3-8b")