class Note:
    def __init__(self, degree, pitch, duration):
        self.degree = degree
        self.pitch = pitch
        self.duration = duration

    def print_name(self):
        print(self.pitch)
