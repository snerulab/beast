class HatchedBeast():
    start = "\033[0;31m" # Red
    stop = "\033[0;0m" # All atributes off
    def __init__(self):
        self.type = 'H'
        self.symbol = self.start + u'\u256c'u'\u256c' + self.stop
        self.isAlive = True
        pass
