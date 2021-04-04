import pathlib


class PathStorage:

    def __init__(self, sep):
        self.sep = sep
        self.__storage = ["storage"]

    def add_path(self, path):
        if ".." in path and len(self.__storage) != 1:
            self.__storage.pop(-1)
        elif ".." in path:
            print("Вы хотите выйти за пределы песочницы!")
        else:
            self.__storage.append(path)

    def file2path(self, file_name):
        locale_storage = self.__storage.copy()
        locale_storage.append(file_name)
        abs_path = pathlib.Path(__file__).parent.absolute()
        return str(abs_path) + self.sep + self.sep.join(locale_storage)

    @property
    def path(self):
        abs_path = pathlib.Path(__file__).parent.absolute()
        return str(abs_path) + self.sep + self.sep.join(self.__storage)

    @property
    def upper_path(self):
        abs_path = pathlib.Path(__file__).parent.absolute()
        print(self.__storage[1:])
        return str(abs_path) + self.sep + self.sep.join(self.__storage[:1])