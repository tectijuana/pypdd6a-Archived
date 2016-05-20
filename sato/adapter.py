from dog import Dog
class Creature(object):
    """The base class for creatures in 2D Land"""

    def make_noise(self):
        """
        This is a technique to fake an ABC
        in Python 2.X
        """
        raise NotImplementedError

class Person(Creature):
    """A representation of a person in 2D Land"""
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        return "hello"

class DogClassAdapter(Creature, Dog):
    """Adapts the Dog class through multiple inheritance"""
    def __init__(self, name):
        Dog.__init__(self, name)

    def make_noise(self):
        """
        Provide the 'make_noise' method that
        the client expects
        """
        return self.bark()
