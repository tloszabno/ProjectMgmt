# instead of putting all format function to Config.py, do it here

import datetime


def get_datetime_prefix():
    date_format = '%Y-%m-%d_%H_%M_%S'
    return datetime.datetime.now().strftime(date_format)
