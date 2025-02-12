import logging
from functools import wraps

import pandas as pd

from logging_config import setup_logging

setup_logging()
logger = logging.getLogger("my_log")


def decorator_record_file(file_name):
    """
    Декоратор, который записывает результат выполнения функции в JSON файл. Принимает на вход имя файла.
    """

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):

            df = func(*args, **kwargs)

            logger.info('Проверка: являются ли данные дата фреймом')

            if isinstance(df, pd.DataFrame):

                logger.info('Запись отчёта в файл')

                df.to_json(file_name, orient="records", lines=True, force_ascii=False)

            else:
                logger.error('Данные не являются дата фреймом. В файл записаны не будут')

            return df

        return inner

    return wrapper
