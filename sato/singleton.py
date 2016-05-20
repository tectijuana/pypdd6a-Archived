class SingletonType(type):
    def __call__(cls):
        if getattr(cls, '__instance__', None) is None:
            instance = cls.__new__(cls)
            instance.__init__()
            cls.__instance__ = instance
        return cls.__instance__
# Usage
class Singleton(object):
    __metaclass__ = SingletonType
    def __init__(self):
        print '__init__:', self
class OtherSingleton(object):
    __metaclass__ = SingletonType
    def __init__(self):
        print 'OtherSingleton __init__:', self
# Tests
s1 = Singleton()
s2 = Singleton()
assert s1
assert s2
assert s1 is s2
os1 = OtherSingleton()
os2 = OtherSingleton()
assert os1
assert os2
assert os1 is os2
