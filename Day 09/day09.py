import timeit


def parse_file(file_to_process: str) -> list[str]:
    with open(file_to_process, mode="r") as file:
        data = file.read().split("\n")

    return data


def get_coefficients(n: int) -> list[int]:
    coefficients = [1]
    for i in range(n):
        coefficients.append(-(1 ** (i + 1)) * coefficients[i] * (n - i) // (i + 1))
    coefficients[-1] = abs(coefficients[-1])
    return coefficients


def calculate_solution(input_data: list[int], part: int) -> int:
    result = 0
    for value in input_data:
        coefficients = get_coefficients(len(value))
        if part == 2:
            if len(value) % 2 == 1:
                coefficients = get_coefficients(len(value) + (-1))
                value.pop(-1)
            coefficients.pop(0)

        x = sum(v * coef for v, coef in zip(value, coefficients))
        result += x

    return abs(result)


def main():
    file_name = "Day 09\\day09-prd.txt"
    input_data = [list(map(int, line.split())) for line in parse_file(file_name)]

    print("Part One:", calculate_solution(input_data, part=1))
    print("Part Two:", calculate_solution(input_data, part=2))


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

# Part One: 1882395907
# Part Two: 1005
