import re
import timeit
import collections

def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data

def convert_to_hand(hand_list):
    res = ''
    replacement = {'666':'A', '555':'K', '444':'Q', '333':'J', '222':'T', '109':'9', '108':'8', '107':'7', '106':'6', '105':'5', '104':'4', '103':'3', '102':'2'}
    for x in hand_list:
        card = str(x).rstrip('0')
        if card in replacement:
            card = replacement[card]
            res+=(card)
        else:
            print('Stop')
    return res

def get_combination(input):
    replacement = {'A':666, 'K':555, 'Q':444, 'J':333, 'T':222}
    counter = collections.Counter(input)
    res = []

    for char, count in counter.items():
        if char in replacement:
            char = replacement[char]
        else:
            char = '10'+char
        res.append([int(char)*10**(count), count])

    card_value_list = []
    for r in res:
        for count in range(0,r[1]):
            #card_value_list.append(r[0]*(10**(r[1])))
            card_value_list.append(r[0])
    card_value_list.sort(reverse=True)
    nice_hand = convert_to_hand(card_value_list)
    card_value_str = ''
    for x in card_value_list:
         tmp = str(x)
         card_value_str+=tmp
    card_value = int(card_value_str)


    if len(res) == 5:
        return ["High card", card_value, nice_hand]
    if len(res) == 4:
        return ["One pair", card_value, nice_hand]
    if len(res) == 3:
        for card in res:
            if card[1]==3:
                return ["Three of a kind", card_value, nice_hand]
            if card[1]==2:
                return ["Two pair", card_value, nice_hand]
    if len(res) == 2:
        for card in res:
            if card[1]==4:
                return ["Four of a kind", card_value, nice_hand]
            if card[1]==3:
                return ["Full house", card_value, nice_hand]
    if len(res) == 1:
        return ["Five of a kind", card_value, nice_hand]

def get_result(hands, combination, i):
    res = 0
    for hand in hands:
        if hand[2] == combination:
            #if combination == 'Full house':
            print(hand[3])
            res += hand[1]*i
            i+=1
    return res, i

def main():

    hands = []
    
    file_name = "Day 07\day07-prd.txt"
    file_data = parse_file(file_name)
    for f in file_data:
        x = f.split(' ')[0]
        y = int(f.split(' ')[1])
        z = get_combination(x)


        hands.append([z[1], y, z[0], z[2]])

    hands.sort()
    #print(hands)

    res_part_one = 0
    i = 1
    tmp, i = get_result(hands,'High card',i)
    res_part_one+=tmp
    print(tmp)
    tmp, i = get_result(hands,'One pair',i)
    res_part_one+=tmp
    print(tmp)
    tmp, i = get_result(hands,'Two pair',i)
    res_part_one+=tmp
    print(tmp)
    tmp, i = get_result(hands,'Three of a kind',i)
    res_part_one+=tmp
    print(tmp)
    tmp, i = get_result(hands,'Full house',i)
    res_part_one+=tmp
    print(tmp)
    tmp, i = get_result(hands,'Four of a kind',i)
    res_part_one+=tmp
    print(tmp)
    tmp, i = get_result(hands,'Five of a kind',i)
    res_part_one+=tmp
    print(tmp)


    
    res_part_two = 0


    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

#Part One: 

# 248755486 - nope
# 248806739 too high
# 249019601 too high
# 253201326
# 253201326
#Part Two: 