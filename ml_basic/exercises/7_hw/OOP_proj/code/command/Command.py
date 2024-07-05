from code.command.domain import WorkFile

# базовый класс по созданию команды, от него наследуются другие классы
# по выполнению команды
class Command:

    def __init__(self, file: WorkFile):
        self.file: WorkFile = file

    def execute(self):
        raise NotImplementedError()

#команда по созданию файла
class CreateCommand(Command):

    def __init__(self, file: WorkFile):
        super().__init__(file)

    def execute(self):
        self.file.create()

#команда по удалению файла
class DeleteCommand(Command):

    def __init__(self, file: WorkFile):
        super().__init__(file)

    def execute(self):
        self.file.delete()

#команда по обновлению файла
class UpdateCommand(Command):

    def __init__(self, file: WorkFile):
        super().__init__(file)

    def execute(self):
        self.file.update()

#команда по конвертации файла
class ConvertCommand(Command):

    def __init__(self, file: WorkFile):
        super().__init__(file)

    def execute(self):
        self.file.convert()
