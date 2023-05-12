import datetime


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self, path_log):
        self.path_log = path_log

    def write_log(self, message, status):
        with open(self.path_log + '/' + 'log_file.log', 'a') as file:
            file.write(f'[{status}]: {str(datetime.datetime.now())} - Message: {message}' + '\n')
