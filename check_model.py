import json
from loguru import logger
from model import ImageGenerator

logger.add("log.txt", format="{time} {level} {message}", level="DEBUG")

class ValidChecker:
    def __init__(self, config):
        try:
            self.model = ImageGenerator(config)
            logger.info("ImageGenerator model loaded sucessfully.")
        except Exception:
            self.model = None
            logger.info("ImageGenerator model failed to load.")


    def check(self, prompt, seed=None, h=None, w=None, steps=None, cfg=None):
        if self.model is None:
            return False
        logger.info("Try to run prediction with the model.")
        try:
            _ = self.model(prompt, seed, h, w, steps, cfg)
            logger.info("Prediction successful.")   
        except Exception:
            logger.info("Prediction failed.")
            return False
        return True

    def is_valid(self):
        return self.check(prompt="A man", seed=10, steps=2)

if __name__ == "__main__":
    logger.info("-" * 50 + "START CHECK" + "-" * 50)
    with open("config.json", "r") as f:
        config = json.load(f)
    checker = ValidChecker(config)
    if checker.is_valid():
        logger.info("Model is valid.")
    else:
        logger.info("Model is invalid.")
    logger.info("-" * 50 + "END CHECK" + "-" * 50)