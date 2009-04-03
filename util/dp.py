def memo(fn):
    cache = {}
    def wrapped(*args):
        try:
            return cache[args]
        except:
            cache[args] = fn(*args)
            return cache[args]
    return wrapped
