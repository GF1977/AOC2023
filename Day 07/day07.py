import timeit
import collections


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data


def get_combination2(input):
    replacement = {
        "A": 22,
        "K": 21,
        "Q": 20,
        "J": 19,
        "T": 18,
        "9": 17,
        "8": 16,
        "7": 15,
        "6": 14,
        "5": 13,
        "4": 12,
        "3": 11,
        "2": 10,
    }

    counter = collections.Counter(input)
    res = []
    for char, count in counter.items():
        res.append(count)

    for i in range(len(res), 5):
        res.append(0)

    res.sort(reverse=True)

    for i in range(0, 5):
        card_score = replacement[input[i]]
        res.append(card_score)

    my_res = 0
    for n in res:
        my_res = my_res * 100 + int(n)

    return my_res


def main():
    qqq = []
    my_dict = {}

    file_name = "Day 07\\day07-prd.txt"
    file_data = parse_file(file_name)
    for f in file_data:
        x = f.split(" ")[0]
        hand_value = int(f.split(" ")[1])

        zzz = get_combination2(x)
        if zzz not in my_dict:
            my_dict[zzz] = hand_value

        qqq.append(zzz)

    qqq.sort(reverse=False)
    res_part_one = 0

    i = 1
    for x in qqq:
        res_part_one += my_dict[x] * i
        i += 1

    print(res_part_one)
    print("----------")

    res_part_two = 0

    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

# Part One: 248179786


# Part Two:248469601 - nope
