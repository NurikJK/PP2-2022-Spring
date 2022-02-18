class stroka:
    def __init__(self):
        self.string = str
    def get_string(self):
        self.string = input()
    def print_string(self):
        print(self.string.upper())

s = stroka()
s.get_string()
s.print_string()