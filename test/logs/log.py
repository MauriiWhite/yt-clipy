import logging.config
import yaml

with open("logging.yaml", "r") as f:
    config = yaml.safe_load(f)
    logging.config.dictConfig(config)

logger = logging.getLogger("my_application")
logger.info("Logger configured with YAML")
