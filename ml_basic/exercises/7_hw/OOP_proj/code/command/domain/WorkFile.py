from enum import Enum

# enum типов для аудио файлов
class AudioExtension(Enum):
    MP3 = 1
    WAV = 2
    MIDI = 3
    AAC = 4

# enum типов для видео файлов
class VideoExtension(Enum):
    AVI = 1
    WMW = 2
    MKV = 3
    MPEG = 4

# enum типов для photo файлов
class PhotoExtension(Enum):
    BMP = 1
    JPG = 2
    GIF = 3
    PNG = 4

# базовый(абсрактный) класс
class WorkFile:

    def __init__(self, author, name, size, create_date):
        self._author = author
        self._name = name
        self._size = size
        self._createdate = create_date

# функция для создания файла
    def create(self):
        raise NotImplementedError()

    # функция для обновления файла
    def update(self):
        raise NotImplementedError()

    # функция для удаления файла
    def delete(self):
        raise NotImplementedError()

    # функция для конвертациии файла
    def convert(self):
        raise NotImplementedError()

# класс для файлов с изображениями
class PhotoFile(WorkFile):

    def __init__(self, author, name, size, create_date, extension: PhotoExtension):
        super().__init__(author, name, size, create_date)
        self.extension: PhotoExtension = extension

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def convert(self):
        pass

#класс для виедеофайлов
class VideoFile(WorkFile):

    def __init__(self, author, name, size, create_date, extension: VideoExtension):
        super().__init__(author, name, size, create_date)
        self.extension: VideoExtension = extension

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def convert(self):
        pass

#класс для аудио файлов
class AudioFile(WorkFile):

    def __init__(self, author, name, size, create_date, extension: AudioExtension):
        super().__init__(author, name, size, create_date)
        self.extension: AudioExtension = extension

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def convert(self):
        pass


