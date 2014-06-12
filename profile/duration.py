import time, sys

stats = {}
def duration(name='stats', stats=stats):
    def _duration(function):
        def __duration(*args, **kw):
            start_time = time.time()
            try:
                return function(*args, **kw)
            finally:
                stats[name] = time.time() - start_time

        return __duration
    return _duration




