from src.commands.base import Command


class CommandIndex(Command):
    def do(self):
        self.check_resume()
        self.get_file_lists()
        self.index()

    def check_resume(self):
        pass

    def get_file_lists(self):
        pass

    def index(self):
        pass