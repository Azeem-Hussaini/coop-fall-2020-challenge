class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.history = []
        self.undoHistory = []

    def add(self, num: int):
        self.value = self.value + num
        self.history.append(num) 

    def subtract(self, num: int):
        self.value = self.value - num
        self.history.append(-num)

    def undo(self):
        if len(self.history) > 0:
            num = self.history[-1]
            self.value = self.value - num
            self.undoHistory.append(-num)

    def redo(self):
        if len(self.undoHistory) > 0:
            num = self.undoHistory[-1]
            self.value = self.value - num
            self.undoHistory = []

    def bulk_undo(self, steps: int):
        while len(self.history) > 0 and steps > 0:
            num = self.history[-1]
            self.value = self.value - num
            del self.history[-1]
            self.undoHistory.append(-num)
            steps = steps - 1

    def bulk_redo(self, steps: int):
        while len(self.undoHistory) > 0 and steps > 0:
            num = self.undoHistory[-1]
            self.value = self.value - num
            del self.undoHistory[-1]
            
            steps = steps - 1
    

example = EventSourcer()

example.add(5)
print("value: " + str(example.value))

example.add(5)
print("value: " + str(example.value))

example.add(5)
print("value: " + str(example.value))

example.undo()
print("value: " + str(example.value))

example.undo()
print("value: " + str(example.value))

example.add(1)
print("value: " + str(example.value))

example.redo()
print("value: " + str(example.value))

