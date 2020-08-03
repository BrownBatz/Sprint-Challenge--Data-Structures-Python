class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.isFull = False

    def append(self, item):
        if len(self.storage) == self.capacity and self.isFull is False:
            self.isFull = True
            self.overwriteCurrent = 1
            self.storage[0] = item
        elif self.isFull:
            if self.overwriteCurrent < len(self.storage) - 1:
                self.storage[self.overwriteCurrent] = item
                self.overwriteCurrent = self.overwriteCurrent + 1
            else:
                oW = len(self.storage) - 1
                self.storage[oW] = item
                self.overwriteCurrent = 0
        else:
            self.storage.append(item)



    def get(self):
        return self.storage