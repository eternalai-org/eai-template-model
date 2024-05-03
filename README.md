# Launching Image Generative AI Models

## Introduction

This is a simple template for launching your Image Generative AI Model.

### Requirements for your checkpoint

- Stable Diffusion model

- Supported checkpoint types: safetensors, lora.

Note: Currently, we only support the above-mentioned checkpoint types. However, we are continuously working to expand our support.

Questions? Join our community at [https://eternalai.org/](https://eternalai.org/)

### Launch your model
- Placing your model checkpoint in the [checkpoint](./checkpoints/). 

- To configure your model checkpoint, modify the [config.json](./config.json) file as follows:
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
    FOR LOADING MODEL:

    - `checkpoint_type`: Specify the type of your checkpoint. It should be either 'safetensors' or 'lora'.
    - `model_ckpt`: Define the path to your checkpoint.
    - `base_model_ckpt`: Specify the path to your base model checkpoint. This should not be null if your checkpoint type is 'lora'. This checkpoint represents the base model that you have fine-tuned.

    FOR INFERENCE:
    - `cfg`:  This represents the default `guidance_scale`. A higher value encourages the model to generate images that closely align with the text prompt, potentially at the cost of image quality. Guidance scale is activated when `guidance_scale` > 1.
    - `steps`: This represents the default `num_inference_steps`, i.e., the number of denoising steps. More steps can lead to higher image quality but may slow down inference.
    - `width`: Define the default width (in pixels) of the generated image.
    - `height`: Define the default height (in pixels) of the generated image.
