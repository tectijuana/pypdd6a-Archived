class Window(object):
    def draw(self, device):
        device.append('flat window')
    def info(self):
        pass
# The decorator pattern approch
class WindowDecorator:
    def __init__(self, w):
        self.window = w
    def draw(self, device):
        self.window.draw(device)
    def info(self):
        self.window.info()
class BorderDecorator(WindowDecorator):
    def draw(self, device):
        self.window.draw(device)
        device.append('borders')
class ScrollDecorator(WindowDecorator):
    def draw(self, device):
        self.window.draw(device)
        device.append('scroll bars')
def test_deco():
    # The way of using the decorator classes
    w = ScrollDecorator(BorderDecorator(Window()))
    dev = []
    w.draw(dev)
    print dev
test_deco()
Difference between subclass method and decorator pattern
# The subclass approch
class BorderedWindow(Window):
    def draw(self, device):
        super(BorderedWindow, self).draw(device)
        device.append('borders')
class ScrolledWindow(Window):
    def draw(self, device):
        super(ScrolledWindow, self).draw(device)
        device.append('scroll bars')
# combine the functionalities using multiple inheritance.
class MyWindow(ScrolledWindow, BorderedWindow, Window):
    pass
def test_muli():
    w = MyWindow()
    dev = []
    w.draw(dev)
    print dev
def test_muli2():
    # note that python can create a class on the fly.
    MyWindow = type('MyWindow', (ScrolledWindow, BorderedWindow, Window), {})
    w = MyWindow()
    dev = []
    w.draw(dev)
    print dev
test_muli()
test_muli2()
