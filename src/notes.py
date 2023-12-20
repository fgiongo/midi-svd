class Note:
    def __init__(self, notetype, time, pitch):
        self.type = notetype
        self.time = time
        self.pitch = pitch

    def toString(self):
        return ("Note: {{type: {}, time: {}, pitch: {}}}".format(self.type, self.time, self.pitch))
