from flask import Flask
import yaml
import logging
from logging.config import dictConfig
"""
dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s >>> %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            }
        },
        "root": {"level": "DEBUG", "handlers": ["console"]},
    }
)
"""

with open('loggin.yaml', 'rt') as file:
        config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/info")
def info():
    app.logger.info("Hello, World!")
    return "Hello, World! (info)"

@app.route("/warning")
def warning():
    app.logger.warning("A warning message.")
    return "A warning message. (warning)"

@app.route("/logcheck")
def logcheck():

    app.logger.debug("A debug message")
    app.logger.info("An info message")
    app.logger.warning("A warning message")
    app.logger.error("An error message")
    app.logger.critical("A critical message")

    return "Hello, World -- logcheck!"

if __name__ == "__main__":
    app.run(debug=False)
