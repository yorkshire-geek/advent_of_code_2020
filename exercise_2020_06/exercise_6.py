def setup(filename: str) -> []:
    with open(filename, 'r') as file:
        data = file.read()
    file.close()

    return data.split('\n\n')


def question_one(sections: []):
    count = 0
    for section in sections:
        h_letters = {letter for letter in section if letter is not '\n'}
        count += len(h_letters)

    print("Question 1: ", count)


def question_two(sections: []):
    count = 0
    for section in sections:
        lines = section.split("\n")
        list_of_sets = []
        for line in lines:
            set_of_line = {letter for letter in line}
            list_of_sets.append(set_of_line)
        count += len(set.intersection(*list_of_sets))

    print("Question 2:", count)


if __name__ == '__main__':
    group_data = setup('input.txt')
    question_one(group_data)
    question_two(group_data)






