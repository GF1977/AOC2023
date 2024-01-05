import timeit


def parse_file(file_to_process: str) -> list[str]:
    with open(file_to_process, mode="r") as file:
        data = file.read().split("\n")

    return data


def get_coeff_old(seq_len: int) -> list[int]:
    if seq_len == 1:
        return [1]
    else:
        prev = get_coeff(seq_len - 1)
        return (
            [prev[0]]
            + [
                (-1) ** (i) * (abs(prev[i - 1]) + abs(prev[i]))
                for i in range(1, len(prev))
            ]
            + [0 + abs(prev[-1])]
        )
    
def get_coeff(n):
    row = [1]
    for i in range(n):
        row.append(-1 ** (i+1) * row[i] * (n-i) // (i+1))
    row[-1]=abs(row[-1])
    return row

def get_solutioin(input, part):
    res = 0
    for value in input:
        #coef = get_coeff_old(len(value) + (2 - part))
        coef = get_coeff(len(value))
        if part == 2:
           #value.pop(-1)
           coef.pop(0)
        x = 0
        i = 0
        for v in value:
            x += v * coef[i]
            i += 1
        res += x

    return abs(res)


def main():
    file_name = "Day 09\\day09-dev.txt"
    file_data = parse_file(file_name)

    input = []
    for line in file_data:
        values = [int(n) for n in line.split(" ")]
        input.append(values)

    print("Part One:", get_solutioin(input, part=1))
    print("Part Two:", get_solutioin(input, part=2))


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

# Part One: 1882395907
# Part Two: 1988629085 too high