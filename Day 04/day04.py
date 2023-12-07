import re

def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data

def main():
    
    file_name = "Day 01\day04-prd.txt"
    file_data = parse_file(file_name)

    res_part_one = 0
    res_part_two = 0


    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)

if __name__ == "__main__":
    main()

#Part One: 
#Part Two: 