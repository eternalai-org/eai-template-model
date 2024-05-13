import os
import torch
import diffusers

class ImageGenerator:
    def __init__(self, config, device=None):
        self.device = device
        if self.device is None:
            self.device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        self.config = config
        self.pipeline = self._load_pipeline()
        self.generator = torch.Generator(device=self.device)

    def _load_pipeline(self):
        dtype = torch.float32 if self.config["torch_dtype"] == "float32" else torch.float16
        ckpt_type = self.config["checkpoint_type"]
        sd_model_type = self.config["sd_type"]
        
        if sd_model_type == "XL":
            model_constructor = diffusers.StableDiffusionXLPipeline
        else:
            model_constructor = diffusers.StableDiffusionPipeline

        if ckpt_type == "safetensors":
            pipeline = model_constructor.from_single_file(self.config["model_ckpt"], torch_dtype = dtype).to(self.device)
        elif ckpt_type == "lora":
            base_model_ckpt = self.config["base_model_ckpt"]
            pipeline = model_constructor.from_single_file(base_model_ckpt, torch_dtype = dtype).to(self.device)
            pipeline.load_lora_weights(self.config["model_ckpt"])
        elif ckpt_type == "diffusers":
            pipeline = model_constructor.from_pretrained(self.config["model_ckpt"], torch_dtype = dtype).to(self.device)
        else:
            raise ValueError(f"Unknown checkpoint type: {ckpt_type}")

        return pipeline

    def __call__(self, prompt, seed = None, h=None, w=None, steps=None, cfg=None, clip_skip = None):
        h = h or self.config["height"]
        w = w or self.config["width"]
        steps = steps or self.config["steps"]
        cfg = cfg or self.config["cfg"]
        seed = seed or self.config["seed"]
        clip_skip = clip_skip or self.config["clip_skip"]

        self.generator.manual_seed(seed)
        pil_images = self.pipeline(
            prompt,
            generator = self.generator,
            height=h,
            width=w,
            guidance_scale=cfg,
            num_images_per_prompt=1,
            num_inference_steps=steps,
            clip_skip = clip_skip,
        ).images
        checked_image = pil_images[0]
        torch.cuda.empty_cache()
        return checked_image