import timeit
import collections


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
    return res


def get_combination(input):
    counter = collections.Counter(input)
    res = []

    for char, count in counter.items():
        res.append([char, count])

    nice_hand = convert_to_hand(input)

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
    hands = {}
    hands_with_values = {}
    qqq = []

    my_dict = {}

    file_name = "Day 07\\day07-prd.txt"
    file_data = parse_file(file_name)
    for f in file_data:
        x = f.split(" ")[0]
        hand_value = int(f.split(" ")[1])
        z = get_combination(x)
        zzz = get_combination2(x)
        if zzz not in my_dict:
            my_dict[zzz] = hand_value

        qqq.append(zzz)
        key = z[0]
        nice_hand = z[2]

        if key not in hands:
            hands[key] = [nice_hand]
        else:
            hands[key].append(nice_hand)

        if nice_hand not in hands_with_values:
            hands_with_values[nice_hand] = hand_value

    qqq.sort(reverse=False)
    res_part_one = 0

    i = 1
    for x in qqq:
        res_part_one+=my_dict[x] * i
        i += 1


    print(res_part_one)
    res_part_one = 0
    print("----------")
    cnt = 1
    for i in range(0, 7):
        if i in hands:
            x = hands[i]
            x.sort(reverse=True)
            for hand in x:
                res_part_one += cnt * hands_with_values[hand]

                cnt += 1

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
