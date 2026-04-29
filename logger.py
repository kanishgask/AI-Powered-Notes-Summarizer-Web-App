# logger.py

import logging

def setup_logger():
    logging.basicConfig(
        filename='app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def log_request(text):
    logging.info(f"User Input: {text[:100]}")  # log first 100 chars

def log_summary(summary):
    logging.info(f"Generated Summary: {summary[:100]}")
