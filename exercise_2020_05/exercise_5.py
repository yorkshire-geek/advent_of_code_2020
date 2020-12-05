from utils.objectmother import ObjectMother
from utils.datawrapper import DataWrapper


class DataWrapper (DataWrapper):

    @staticmethod
    def factory(data):
        return DataWrapper(data)

    def get_row_str(self) -> str:
        return self.data[0:7]

    def get_column_str(self) -> str:
        return self.data[7:10]

    def get_row_binary(self) -> str:
        return self.get_row_str().replace("F", "0").replace("B", "1")

    def get_row(self) -> int:
        stream_binary = self.get_row_binary()

        result = (int(stream_binary[0]) * 64) + (int(stream_binary[1]) * 32) + \
                 (int(stream_binary[2]) * 16) + (int(stream_binary[3]) * 8) + \
                 (int(stream_binary[4]) * 4) + (int(stream_binary[5]) * 2) + (int(stream_binary[6]))
        return result

    def get_column_binary(self) -> str:
        return self.get_column_str().replace("L", "0").replace("R", "1")

    def get_column(self) -> int:
        stream_binary = self.get_column_binary()

        result = (int(stream_binary[0]) * 4) + (int(stream_binary[1]) * 2) + \
                 (int(stream_binary[2]))
        return result

    def get_id(self) -> int:
        return 8 * self.get_row() + self.get_column()


def find_maximum() :
    list_of_data = ObjectMother("input.txt").return_list(DataWrapper.factory)

    maximum_id = 0
    for data in list_of_data:
        maximum_id = max(maximum_id, data.get_id())

    print("maximum ", maximum_id)


def find_all_ids() :
    list_of_data = ObjectMother("input.txt").return_list(DataWrapper.factory)

    list_of_ids = []
    for data in list_of_data:
        list_of_ids.append(data.get_id())

    list_of_ids.sort()

    last_seat = list_of_ids[0] - 1
    for seat in list_of_ids:
        if seat == last_seat + 2:
            print("seat: ", seat - 1)
        last_seat = seat


if __name__ == '__main__':
    find_maximum()
    print("------")
    find_all_ids()


