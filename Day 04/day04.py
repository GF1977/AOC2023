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


    for line in file_data:
        tmp_split = line.split('|')
        card_part_one = tmp_split[0].split(':')[1]
        card_part_two = tmp_split[1]

        elf_numbers = re.findall(r'\d+',card_part_one)
        win_numbers = re.findall(r'\d+',card_part_two)

        win_match = set(elf_numbers) & set(win_numbers)
        res_part_one += int(pow(2, win_match.__len__()-1))

    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)

if __name__ == "__main__":
    main()

#Part One: 20855
#Part Two: 