import logging
import logging.config

from pathlib import Path

import yaml


class LoggerConfigurator:
    @staticmethod
    def configure_logger(config_path: str = "config/logging.yaml") -> None:
        config_file = Path(config_path)
        if not config_file.exists():
            raise FileNotFoundError(
                f"Logging configuration file not found: {config_path}"
            )

        with open(config_file, "r") as file:
            config = yaml.safe_load(file)

        logging.config.dictConfig(config)

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        return logging.getLogger(name)
