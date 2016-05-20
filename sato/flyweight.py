from __future__ import print_function
import weakref


class Card(object):

    # comment __new__ and uncomment __init__ to see the difference

    '''The object pool. Has builtin reference counting'''
    _CardPool = weakref.WeakValueDictionary()

    '''If the object exists in the pool just return it (instead of creating a new one)'''
    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value + suit, None)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    # def __init__(self, value, suit):
    #     self.value, self.suit = value, suit

    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)

if __name__ == '__main__':
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(c1, c2)
    print(c1 == c2)
    print(id(c1), id(c2))
