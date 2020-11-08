from src.model.reader_strategy import ReaderStrategy


class FileReader:
    def __init__(self, new_reader_strategy: ReaderStrategy):
        self.reader_strategy = new_reader_strategy

    def check_if_valid_dir(self, new_dir):
        return self.reader_strategy.is_valid_dir(new_dir)

    def check_if_valid_file(self, new_file_dir):
        return self.reader_strategy.is_valid_file(new_file_dir)

    def get_file_contents(self, new_dir):
        return self.reader_strategy.get_file_contents(new_dir)
