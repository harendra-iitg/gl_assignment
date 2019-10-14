import queue

class QueueProcessor:
    def __init__(self):
        self.queue = queue.Queue()

    def add_data(self, arr):
        self.queue.put(arr)

    def get_data(self):
        if not self.queue.empty():
            return self.queue.get()
        else:
            raise Exception("Queue is empty")

    def queue_size(self):
        return self.queue.qsize()

    def is_empty(self):
        return self.queue.empty()
