import os
import sys
import argparse

def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data


def get_digits(s):
    digits = "".join(filter(str.isdigit, s))
    if digits.__len__() > 0:
        res = digits[0] + digits[digits.__len__() - 1]
    else:
        res = None
    
    return int(res)

def main():
    
    file_name = "Day 01\day01-prd.txt"
    file_data = parse_file(file_name)

    res_part_one = 0
    for line in file_data:
        calibration_values = get_digits(line)
        res_part_one += calibration_values

    
    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", 2)

if __name__ == "__main__":
    main()