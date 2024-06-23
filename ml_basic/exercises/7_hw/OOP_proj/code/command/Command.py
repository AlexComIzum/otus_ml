from code.command.domain import WorkFile


class Command:

    def __init__(self, file: WorkFile):
        self.file: WorkFile = file

    def execute(self):
        raise NotImplementedError()


class CreateCommand(Command):

    def __init__(self, file: WorkFile):
        super().__init__(file)

    def execute(self):
        self.file.create()


class DeleteCommand(Command):

    def __init__(self, file: WorkFile):
        super().__init__(file)

    def execute(self):
        self.file.delete()


class UpdateCommand(Command):

    def __init__(self, file: WorkFile):
        super().__init__(file)

    def execute(self):
        self.file.update()

class ConvertCommand(Command):

    def __init__(self, file: WorkFile):
        super().__init__(file)

    def execute(self):
        self.file.convert()
