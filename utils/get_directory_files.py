import os

class GetDirectoryFiles:
    def set_directory_path(self, path) -> None:
        self.__path = path
    def get_files(self) -> list:
        files = os.listdir(self.__path)
        return list(map(lambda x: self.__path + "/" + x, files))
