import timeit


def parse_file(file_to_process: str) -> list[str]:
    my_dict = {}
    with open(file_to_process, "r") as file:
        for row, line in enumerate(file):
            for col, char in enumerate(line.strip()):
                my_dict[(row, col)] = char
    return my_dict


def get_key_for_value(map, value):
    for key, val in map.items():
        if val == value:
            return key
    return None


def get_single_neighbour(map, coord, delta_x, delta_y):
    x, y = coord
    key = (x + delta_x, y + delta_y)
    if key in map:
        return (key, map[key])
    else:
        return None


def get_neighbors(map, coord):
    res = {}
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for delta in deltas:
        n = get_single_neighbour(map, coord, delta[0], delta[1])
        if n is not None:
            res[n[0]] = n[1]
    return res


def main():
    file_name = "Day 10\\day10-dev.txt"
    map = parse_file(file_name)

    s_coordinates = get_key_for_value(map, "S")
    print(s_coordinates)
    neighbours = get_neighbors(map, s_coordinates)
    print(neighbours)

    # Y X
    # L (-1, 0) (0, 1)
    # J (-1, 0) (0, -1)
    # 7 (1, 0) (0,1)
    # F (1, 0) (0, -1)
    # | (-1,0) (1,0)
    # - (0,-1) (0,1)

    for key in neighbours:
        v = neighbours[key]
        print(v)
        if v == 'J':
            next_step = get_single_neighbour(map, key, -1, 0)
        


    res_part_one = 0
    res_part_two = 0

    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

# Part One:
# Part Two:
