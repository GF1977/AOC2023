import timeit
import collections
from collections import Counter


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data


def convert_to_hand(hand_list):
    res = ""
    replacement = {
        "A": "A",
        "K": "B",
        "Q": "C",
        "J": "D",
        "T": "E",
        "9": "F",
        "8": "G",
        "7": "H",
        "6": "I",
        "5": "J",
        "4": "K",
        "3": "L",
        "2": "M",
    }
    for x in hand_list:
        card = str(x).rstrip("0")
        if card in replacement:
            card = replacement[card]
            res += card
        else:
            print("Stop")
    return res


def get_combination(input):
    counter = collections.Counter(input)
    res = []

    for char, count in counter.items():
        res.append([char, count])

    nice_hand = new_sorting(convert_to_hand(input))

    card_value = 0
    len_res = len(res)

    if len_res == 5:  # "High card"
        return [0, card_value, nice_hand]

    if len_res == 4:  # "One pair"
        return [1, card_value, nice_hand]

    if len_res == 3:
        for card in res:
            if card[1] == 2:  # "Two pair"
                return [2, card_value, nice_hand]

            if card[1] == 3:  # "Three of a kind"
                return [3, card_value, nice_hand]

    if len_res == 2:
        for card in res:
            if card[1] == 3:  # "Full house"
                return [4, card_value, nice_hand]

            if card[1] == 4:  # Four of a kind"
                return [5, card_value, nice_hand]

    if len_res == 1:  # "Five of a kind"
        return [6, card_value, nice_hand]


def get_result(hands, combination, i):
    res = 0
    for hand in hands:
        if hand[2] == combination:
            res += hand[1] * i
            i += 1
    return res, i


def new_sorting(hand):
    # Count the frequency of each character
    freq = Counter(hand)

    # Sort the characters first by frequency (desc), then by character (asc)
    sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # Join the characters back into a string
    sorted_string = "".join([char * count for char, count in sorted_chars])

    return sorted_string


def main():
    hands = {}
    hands_with_values = {}

    file_name = "Day 07\\day07-prd.txt"
    file_data = parse_file(file_name)
    for f in file_data:
        x = f.split(" ")[0]
        hand_value = int(f.split(" ")[1])
        z = get_combination(x)
        key = z[0]
        nice_hand = z[2]

        if key not in hands:
            hands[key] = [nice_hand]
        else:
            hands[key].append(nice_hand)

        if nice_hand not in hands_with_values:
            hands_with_values[nice_hand] = hand_value

    res_part_one = 0

    print("----------")
    cnt = 1
    for i in range(0, 7):
        tpm_res = 0 
        if i in hands:
            x = hands[i]
            x.sort(reverse=True)
            for hand in x:
                #print(i, hand, hands_with_values[hand])
                tpm_res = cnt * hands_with_values[hand]
                res_part_one += tpm_res
                cnt += 1
        print(i, tpm_res)

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

# 248469601 - nope
# 248755486 - nope
# 248806739 too high
# 249019601 too high
# 253201326
# 253201326
# Part Two:
