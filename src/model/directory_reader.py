from os import listdir, path


class DirectoryReader:
    def __init__(self):
        self.__all_my_files = []
        self.__all_my_file_dirs = []
        self.__folder_dir = ""

    def set_directory(self, new_folder_path):
        self.__folder_dir = new_folder_path
        self.__all_my_files = listdir(new_folder_path)
        self.__set_file_dirs()

    def is_valid_file(self, new_file_path):
        """Will return true if the provided path\
         is a javascript file. (.js)"""
        return path.isfile(new_file_path) and  \
               new_file_path.endswith((".js", ".py"))

    def is_valid_dir(self, new_folder_path):
        """Will return true if the provided directory\
         contains at least 1 javascript file. (.js)"""
        if path.isdir(new_folder_path):
            files_to_check = listdir(new_folder_path.replace("\\", "/"))
            for file in files_to_check:
                if str(file).endswith((".js", ".py")):
                    return True
        return False

    def __set_file_dirs(self):
        for file in self.__all_my_files:
            if str(file).endswith((".js", ".py")):
                self.__all_my_file_dirs.append(str.format("{}/{}",
                                                          self.__folder_dir,
                                                          file))

    def get_file_dirs(self):
        return self.__all_my_file_dirs
