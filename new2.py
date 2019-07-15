class A:

    def play(self):
        print("play")
        print(self.password)
    def clay(self):
        print("clay")

class B(A):
    def __init__(self):
        self.password = "hh"
        self.user = "uu"

class C(A):
    def __init__(self):
        self.password = "hdssh"
        self.user = "ussu"


def hello(aaa):
    if(aaa=="h"):
        return B()
A = hello("h")
A.play()
