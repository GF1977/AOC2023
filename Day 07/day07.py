import timeit
import collections


def parse_file(file_to_process: str) -> list[str]:
    with open(file_to_process, mode="r") as file:
        data = file.read().split("\n")
    return data


def get_hand_rank(hand: str, puzzle_part: int) -> int:
    card_ranks = {
        "A": 24,
        "K": 23,
        "Q": 22,
        "J": 21,
        "T": 20,
        "9": 19,
        "8": 18,
        "7": 17,
        "6": 16,
        "5": 15,
        "4": 14,
        "3": 13,
        "2": 12,
    }

    counter = collections.Counter(hand)
    rank = sorted([count for _, count in counter.items()], reverse=True)
    rank += [0] * (5 - len(rank))
    if puzzle_part == 2 and "J" in counter:
        card_ranks["J"] = 10
        joker_cnt = counter["J"]
        counter["J"] = 0
        rank = sorted([count for _, count in counter.items()], reverse=True)
        rank += [0] * (5 - len(rank))
        rank[0] = (rank[0] + joker_cnt) % 6
    rank += [card_ranks[card] for card in hand[:5]]

    return sum(n * 100**i for i, n in enumerate(rank[::-1]))


def main():
    sorted_hands = []
    hands_and_values = {}

    file_name = "Day 07\\day07-prd.txt"
    file_data = parse_file(file_name)

    for line in file_data:
        hand, hand_value = line.split(" ")
        key = get_hand_rank(hand, 1)
        hands_and_values[key] = int(hand_value)

    sorted_hands = sorted(hands_and_values.keys())
    res_part_one = sum(
        hands_and_values[key] * i for i, key in enumerate(sorted_hands, 1)
    )

    sorted_hands = []
    hands_and_values = {}

    for line in file_data:
        hand, hand_value = line.split(" ")
        key = get_hand_rank(hand, 2)
        hands_and_values[key] = int(hand_value)

    sorted_hands = sorted(hands_and_values.keys())
    res_part_two = sum(
        hands_and_values[key] * i for i, key in enumerate(sorted_hands, 1)
    )

    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part One:", res_part_two)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

# Part One: 248179786
# Part Two: 247885995
