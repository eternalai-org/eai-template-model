import json
import argparse
from loguru import logger
from model import ImageGenerator

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="config.json", help="Path to the config file")
    parser.add_argument("--prompt", type=str, default = "A man", help="Prompt to generate an image from")
    parser.add_argument("--seed", type=int, default= 10, help="Seed for random number generator")
    parser.add_argument("--h", type=int, default=None, help="Height of the image")
    parser.add_argument("--w", type=int, default=None, help="Width of the image")
    parser.add_argument("--steps", type=int, default= 2, help="Number of inference steps")
    parser.add_argument("--cfg", type=float, default=None, help="Guidance scale")
    parser.add_argument("--output_path", type=str, default=None, help="Path to save the generated image or to check the image")
    parser.add_argument("--log", type=str, default="log.txt", help="Path to the log file")
    parser.add_argument("--check-result-path", type=str, default=None, help="Path to save the check result")
    return parser.parse_args()


class ValidChecker:
    def __init__(self, config):
        try:
            self.model = ImageGenerator(config)
            logger.info("ImageGenerator model loaded sucessfully.")
        except Exception as e:
            self.model = None
            logger.info(e)
            logger.info("ImageGenerator model failed to load.")


    def check(self, prompt, seed=None, h=None, w=None, steps=None, cfg=None):
        if self.model is None:
            return False
        logger.info("Try to run prediction with the model.")
        try:
            _ = self.model(prompt, seed, h, w, steps, cfg)
            logger.info("Prediction successful.")   
        except Exception as e:
            logger.info(e)
            logger.info("Prediction failed.")
            return False
        return True

if __name__ == "__main__":
    args = parse_args()
    result = {"is_valid": False}
    logger.add(args.log, format="{time} {level} {message}", level="DEBUG")
    logger.info("-" * 50 + "START CHECK" + "-" * 50)
    with open("config.json", "r") as f:
        config = json.load(f)
    checker = ValidChecker(config)
    if checker.check(args.prompt, args.seed, args.h, args.w, args.steps, args.cfg):
        logger.info("Model is valid.")
        result["valid"] = True
    else:
        logger.info("Model is invalid.")
    if args.check_result_path is not None:
        with open(args.check_result_path, "w") as f:
            json.dump(result, f)
    logger.info("-" * 50 + "END CHECK" + "-" * 50)