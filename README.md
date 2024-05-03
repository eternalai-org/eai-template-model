# Launching Image Generative AI Models

## Introduction

This is a simple template for launching your Image Generative AI Model.

### Requirements for your checkpoint

- Stable Diffusion model

- Supported checkpoint types: safetensors, lora.

Note: Currently, we only support the above-mentioned checkpoint types. However, we are continuously working to expand our support.

Questions? Join our community at [https://eternalai.org/](https://eternalai.org/)

### Launch your model
Your checkpoint should placed in folder [checkpoint](./checkpoints/).
You should change [config.json](./config.json) file to adapt your model checkpoint:
```json
{
    "checkpoint_type": "safetensors",
    "model_ckpt": "checkpoints/model.safetensors",
    "base_model_ckpt": null,
    "steps": 30,
    "cfg": 2.0,
    "width": 1024,
    "height": 1024
}
```
- `checkpoint_type`: your checkpoint type (should be safetensors or lora).
- `model_ckpt`: your checkpoint path.
- `base_model_ckpt`: your base model checkpoint path (should not be null if your checkpoint type is lora), this checkpoint represents your base model you finetuned on.
- `cfg`: 
