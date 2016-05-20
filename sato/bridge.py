class AbstractInterface:

    """ Target interface.
    This is the target interface, that clients use.
    """

    def someFunctionality(self):
        raise NotImplemented()


class Bridge(AbstractInterface):

    """ Bridge class.
    
    This class forms a bridge between the target
    interface and background implementation.
    """

    def __init__(self):
        self.__implementation = None


class UseCase1(Bridge):

    """ Variant of the target interface.
    This is a variant of the target Abstract interface.
    It can do something little differently and it can
    also use various background implementations through
    the bridge.
    """
    
    def __init__(self, implementation):
        self.__implementation = implementation

    def someFunctionality(self):
        print "UseCase1: ",
        self.__implementation.anotherFunctionality()


class UseCase2(Bridge):
    def __init__(self, implementation):
        self.__implementation = implementation

    def someFunctionality(self):
        print "UseCase2: ",
        self.__implementation.anotherFunctionality()


class ImplementationInterface:
    
    """ Interface for the background implementation.
    This class defines how the Bridge communicates
    with various background implementations.
    """

    def anotherFunctionality(self):
        raise NotImplemented

class Linux(ImplementationInterface):

    """ Concrete background implementation.
    A variant of background implementation, in this
    case for Linux!
    """

    def anotherFunctionality(self):
        print "Linux!"


class Windows(ImplementationInterface):
    def anotherFunctionality(self):
        print "Windows."


def main():
    linux = Linux()
    windows = Windows()

    # Couple of variants under a couple
    # of operating systems.
    useCase = UseCase1(linux)
    useCase.someFunctionality()

    useCase = UseCase1(windows)
    useCase.someFunctionality()

    useCase = UseCase2(linux)
    useCase.someFunctionality()

    useCase = UseCase2(windows)
    useCase.someFunctionality()


if __name__ == "__main__":
    main()
