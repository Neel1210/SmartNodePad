import NotePadModel

class Controller:

    def __init__(self):
        self.notepadModel = NotePadModel.Model()

    def save_file(self, msg):
        self.notepadModel.save_file(msg)

    def save_as(self, msg1):
        self.notepadModel.save_as(msg1)

    def read_file(self):
        self.msg, self.base = self.notepadModel.read_file()
        return self.msg, self.base

    def saysomeThing(self):
        self.takeAudio = self.notepadModel.takeQuery()
        return self.takeAudio
    def new_file(self):
        self.notepadModel.new_file()
