

class Nome():

    def __init__(self):
        print("Criacao")

    def __new__(cls, *args, **kwargs):
        print("New")

    def __del__(self):
        print("del")

    def printValue(value):
        print("print" + value)


test = Nome()

del test
