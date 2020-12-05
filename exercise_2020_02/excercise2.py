from utils.objectmother import ObjectMother
from utils.datawrapper import DataWrapper


class DataWrapper (DataWrapper):

    @staticmethod
    def factory(data):
        return DataWrapper(data)

    def get_min(self) -> int:
        return int(self.data.split("-")[0])

    def get_max(self) -> int:
        return int(self.data.split(" ")[0].split("-")[1])

    def get_check_char(self) -> str:
        return self.data.split(" ")[1][0]

    def get_password(self) -> str:
        return self.data.split(" ")[2]


def check_valid_1(min_value: int, max_value: int, check_char: str, password : str ) -> bool:
    occurances = password.count(check_char)
    return (occurances >= min_value) & (occurances <= max_value)


def check_valid_2(min_value: int, max_value: int, check_char: str, password: str) -> bool:
    return (password[min_value-1] + password[max_value-1]).count(check_char) == 1


if __name__ == "__main__":
    count_1, count_2 = 0, 0
    list_of_data = ObjectMother("input.txt").return_list(DataWrapper.factory)
    for data in list_of_data:
        if check_valid_1(data.get_min(), data.get_max(), data.get_check_char(), data.get_password()):
            count_1 += 1

        if check_valid_2(data.get_min(), data.get_max(), data.get_check_char(), data.get_password()):
            count_2 += 1

    print(count_1, count_2)

