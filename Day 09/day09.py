import timeit


def parse_file(file_to_process: str) -> list[str]:
    with open(file_to_process, mode="r") as file:
        data = file.read().split("\n")

    return data


def get_coeff(seq_len: int) -> list[int]:
    if seq_len == 1:
        return [1]
    else:
        prev = get_coeff(seq_len - 1)
        return (
            [prev[0] + 0]
            + [
                (-1) ** (i) * (abs(prev[i - 1]) + abs(prev[i]))
                for i in range(1, len(prev))
            ]
            + [0 + abs(prev[-1])]
        )


def get_diff(values):
    layers = []
    layers.append(values)

    n = 1
    while True:
        layers.append([])
        for i in range(0, len(values) - 1):
            layers[n].append(values[i + 1] - values[i])

        if sum(layers[n]) == 0:
            break
        values = layers[n]
        n += 1

    diff = 0
    for i in range(len(layers) - 1, -1, -1):
        diff += int(layers[i][-1])

    print(diff)
    return diff


def solve_part_one(input):
    res = 0
    res1 = 0
    for line in input:
        res += get_diff(line)

    # if res != res1:
    #     print('STOP', res, res1)
    #     pass

    return res


def main():
    file_name = "Day 09\\day09-dev.txt"
    file_data = parse_file(file_name)


    # for i in range(1, 10):
    #     print(get_coeff(i))

    # return

    input = []
    for line in file_data:
        values = [int(n) for n in line.split(" ")]
        input.append(values)

    res_part_one = solve_part_one(input)
    res_part_two = 0

    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

# Part One: 1882395934 too high
# Part Two:
