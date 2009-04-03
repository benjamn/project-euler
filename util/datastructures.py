from Queue import deque

class BoundedQueue(deque):
    def __init__(self, bound=None, *args, **kwargs):
        self._bound = bound
        super(BoundedQueue, self).__init__(*args, **kwargs)
        
    def put(self, *args, **kwargs):
        if self._bound is not None:
            while len(self) >= self._bound:
                self.get()
        super(BoundedQueue, self).put(*args, **kwargs)