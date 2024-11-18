class A:
    def __init__(self):
        self._t = 1
    
    def print(self):
        print(self._t)

class B(A):
    def __init__(self):
        super().__init__()
        self._t = 2


A().print()
B().print()