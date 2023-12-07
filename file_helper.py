
class file_helper:
    """
    static helper class to write and read array from txt file
    """

    @classmethod
    def save_array_to_file(cls, array_to_write: list, path: str):
        with open(path, "w") as file:
            for line in array_to_write:
                file.write(f"{line}\n")

    @classmethod
    def read_array_from_file(cls, path: str) -> list:
        arr_to_return: list = []
        with open(path, "r") as file:
            arr_to_return = file.readline()

        return arr_to_return

