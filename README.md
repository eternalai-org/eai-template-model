# Launching Image Generative AI Models

## Introduction

This is a simple template for launching your Image Generative AI Model.

### Requirements for your checkpoint

- Stable Diffusion model.

- Supported checkpoint types: `single` file checkpoint (`.safetensors` or `.ckpt`), and `lora`.

Note: Currently, we only support the above-mentioned checkpoint types. However, we are continuously working to expand our support.

### Launch your model
- Placing your model checkpoint in the [checkpoints](./checkpoints/). 

- To configure your model checkpoint, modify the [config.json](./config.json) file as follows:
    ## For single type:
    ```json
    {
        "checkpoint_type": "safetensors",
        "model_ckpt": "checkpoints/model.safetensors",
        "base_model_ckpt": null,
        "sd_type": "XL",
        "torch_dtype": "float32",
        "seed": 42,
        "steps": 30,
        "cfg": 2.0,
        "width": 1024,
        "height": 1024,
        "clip_skip": null
    }
    ```
    ## For lora:
    ```json
    {
        "checkpoint_type": "lora",
        "model_ckpt": "checkpoints/model.safetensors",
        "base_model_ckpt": "checkpoints/base_model.safetensors",
        "sd_type": "XL",
        "torch_dtype": "float32",
        "seed": 42,
        "steps": 30,
        "cfg": 2.0,
        "width": 1024,
        "height": 1024,
        "clip_skip": null
    }
    ```

    # FOR LOADING MODEL:

    - `checkpoint_type`: Specify the type of your checkpoint. It should be either 'safetensors' or 'lora'.
    - `model_ckpt`: Define the path to your checkpoint.
    - `base_model_ckpt`: Specify the path to your base model checkpoint. This should not be null if your checkpoint type is 'lora'. This checkpoint represents the base model that you have fine-tuned.
    - `sd_type`: Type of stable diffusion checkpoint. Set to 'XL' if `base_model_ckpt` is a Stable Diffusion XL checkpoint; otherwise, leave as null.

    # FOR INFERENCE:
    - `cfg`:  This represents the default `guidance_scale`. A higher value encourages the model to generate images that closely align with the text prompt, potentially at the cost of image quality. Guidance scale is activated when `guidance_scale` > 1.
    - `steps`: This represents the default `num_inference_steps`, i.e., the number of denoising steps. More steps can lead to higher image quality but may slow down inference.
    - `width`: Define the default width (in pixels) of the generated image.
    - `height`: Define the default height (in pixels) of the generated image.

### Importance
To ensure the validity of your model, you should use the [check_model.py](./check_model.py) script. This script performs several critical checks to confirm that your model is properly configured and can be loaded without errors. Specifically, it will:
 1. **Verify Model Integrity**: The script will examine the model file to ensure that it is not corrupted and that all necessary components are present.
 2. **Load the Model**: The script will attempt to load the model into memory. If the model cannot be loaded, it will provide detailed error messages to help you diagnose and fix any issues.
 3. **Run Initial Tests**: Basic tests may be performed to ensure that the model behaves as expected with sample input data.

Please run the following command to check your model:
```
conda env create -f environment.yml
conda activate check_valid
python check_model.py
```
# Need help?

Join our community at [https://eternalai.org/](https://eternalai.org/)