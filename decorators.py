import os
from datetime import datetime


def logger_(log_name, log_dir=None):
    if log_dir is None:
        log_path = os.path.join(os.getcwd(), log_name)
    else:
        os.makedirs(f'{os.getcwd()}/{log_dir}', exist_ok=True)
        log_path = os.path.join(log_dir, log_name)

    def logger(func):
        def log(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(f'{log_path}', 'a') as f:
                f.write(
                    f'{datetime.now().strftime("DATE: %m.%d.%Y  TIME: %H:%M:%S")}\n'
                    f'FUNCTION NAME:  {func.__name__!r}\n'
                    f'ARGUMENTS: {args}{kwargs}\n'
                    f'RESULT: {result}\n\n')
            return result

        return log

    return logger
