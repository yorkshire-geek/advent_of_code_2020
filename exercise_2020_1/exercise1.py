def return_list():
    result = []
    with open("input.txt", 'r') as input_file:
        for line in input_file:
            result.append(int(line.strip()))
    input_file.close()

    return result


if __name__ == "__main__":

    list_of_ints = return_list()
    list_of_ints.sort()

    print("--- find 2020 with two entries---")

    for first in list_of_ints:
        for second in list_of_ints:
            total = first + second
            if total == 2020:
                print(first, second)
                print(first * second)

    for first in list_of_ints:
        for second in list_of_ints:
            for third in list_of_ints:
                total = first + second + third
                if total == 2020:
                    print(first, second, third)
                    print(first * second * third)
