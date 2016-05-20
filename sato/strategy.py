class Strategy:
    def execute(self, a, b):
        pass


class Add(Strategy):
    def execute(self, a, b):
        return a + b


class Subtract(Strategy):
    def execute(self, a, b):
        return a - b


class Multiply(Strategy):
    def execute(self, a, b):
        return a * b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, a, b):
        return self.strategy.execute(a, b)


if __name__ == "__main__":
    context = None

    context = Context(Add())
    print "Add Strategy %d" % context.execute(10, 5)

    context = Context(Subtract())
    print "Subtract Strategy %d" % context.execute(10, 5)

    context = Context(Multiply())
    print "Multiply Strategy %d" % context.execute(10, 5)
