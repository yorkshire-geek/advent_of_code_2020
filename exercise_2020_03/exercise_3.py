class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, right : int, down :int):
        self.x = (self.x + right) % 31
        self.y += down


def get_input_map() -> []:
    result = []
    with open("input.txt", 'r') as input_file:
        for line in input_file:
            result.append(line.strip())
    input_file.close()
    return result


def do_a_run(right: int, down: int) -> int:
    trees_hit = 0
    loc = Location(0, 0)
    while loc.y < 322:
        loc.move(right, down)
        if input_map[loc.y][loc.x] == '#':
            trees_hit += 1
    print("Trees hit [", right, ",", down, "] ", trees_hit)
    return trees_hit


if __name__ == '__main__':
    input_map = get_input_map()
    inputs = [(1, 1),(3,1), (5,1), (7,1), (1,2)]
    for ip in inputs:
        do_a_run(ip[0], ip[1])