import logging

def get_logger():

    logger = logging.getLogger("loan_api")

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger