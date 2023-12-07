import re

def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data

def main():
    
    file_name = "Day 04\day04-prd.txt"
    file_data = parse_file(file_name)

    res_part_one = 0
    res_part_two = 0

    cards_pile = {}

    for line_number, line in enumerate(file_data, start=1):
        if  line_number not in cards_pile:
            cards_pile[line_number] = 1
        tmp_split = line.split('|')
        card_part_one = tmp_split[0].split(':')[1]
        card_part_two = tmp_split[1]

        elf_numbers = re.findall(r'\d+',card_part_one)
        win_numbers = re.findall(r'\d+',card_part_two)

        win_match = set(elf_numbers) & set(win_numbers)
        winners_count = win_match.__len__()
        res_part_one += int(pow(2, win_match.__len__()-1))

        current_line_value = cards_pile[line_number]
        for i in range(line_number + 1, line_number + winners_count + 1):
            if i not in cards_pile:
                cards_pile[i] = current_line_value + 1
            else:
                cards_pile[i] = cards_pile[i] + current_line_value

    res_part_two = sum(cards_pile.values())

    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)

if __name__ == "__main__":
    main()

#Part One: 20855
#Part Two: 