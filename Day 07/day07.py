import timeit
import collections


def parse_file(file_to_process: str) -> list[str]:
    with open(file_to_process, mode="r") as file:
        data = file.read().split("\n")
    return data


def get_hand_rank(hand: str) -> int:
    card_ranks = {
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

    counter = collections.Counter(hand)
    rank = sorted([count for _, count in counter.items()], reverse=True)
    rank += [0] * (5 - len(rank))
    rank += [card_ranks[card] for card in hand[:5]]

    return sum(n * 100**i for i, n in enumerate(rank[::-1]))


def main():
    sorted_hands = []
    hands_and_values = {}

    file_name = "Day 07\\day07-prd.txt"
    file_data = parse_file(file_name)

    for line in file_data:
        hand, hand_value = line.split(" ")
        key = get_hand_rank(hand)
        hands_and_values[key] = int(hand_value)

    sorted_hands = sorted(hands_and_values.keys())
    res_part_one = sum(
        hands_and_values[key] * i for i, key in enumerate(sorted_hands, 1)
    )

    print("----------------------------")
    print("Part One:", res_part_one)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

# Part One: 248179786
# Part Two:248469601 - nope
