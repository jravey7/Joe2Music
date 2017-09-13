#private class for easier queue management 
class _PlayQueue:
    name = None
    playqueue = None
    def __init__(self, name="default"):
        self.playqueue = []
        self.name = name
        
    def add(self, item):
        self.playqueue.extend(item)
        
    def print_queue(self):
        print("{}:".format(self.name))
        for item in self.playqueue:
            print("\t{}".format(item) )

class PlayQueues:

    # Queue names must be unique

    queues = None
    playqueue_counter = 0
    
    def __init__(self):
        self.cur_queue = "default"
        self.queues = {}
        self.queues[self.cur_queue] = _PlayQueue(self.cur_queue)
        
    # add a new queue to the list
    def new_queue(self, key="default"):
        if key in self.queues:
            return
        self.queues[key] = _PlayQueue()
