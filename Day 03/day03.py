# --- Day 3: Gear Ratios ---
import re
from typing import Literal


class Part_number:
    def __init__(self, value, line_num, start, end):
        self.value = value
        self.line_num = line_num
        self.start = start
        self.end = end
    


def parse_file(file_to_process, target: Literal['digits', 'symbols']):
    results = []
    with open(file_to_process, 'r') as file:
        for line_number, line_content in enumerate(file, start=0):
            if target == 'digits':
                res = re.findall(r'\d+', line_content)
            if target == 'symbols':
                res = re.findall(r'[^0-9.\n]', line_content)

            for value in res:
                start_position = line_content.index(value)
                end_position = start_position + len(value) - 1

                if target == 'symbols':
                    value = -1

                obj = Part_number(int(value), line_number, start_position, end_position)
                results.append(obj)

    return results

def check_nearby_fields(p):
    print(p)
    return True


def main():

    res_part_one = 0
    res_part_two = 0

    file_name = 'Day 03\day03-dev.txt'

    part_numbers = parse_file(file_name,'digits')
    symbols      = parse_file(file_name,'symbols')
    #check_nearby_fields(part_numbers[0],)


    for part in part_numbers:
        for symbol in symbols:
            if abs(part.line_num - symbol.line_num) <= 1:
                if symbol.start >= part.start - 1 and symbol.end <= part.end + 1:
                    res_part_one += part.value
                    #print(part.value)
                    continue

    print('----------------------------')
    print('Part One:', res_part_one)
    print('Part Two:', res_part_two)

if __name__ == '__main__':
    main()

#Part One: 2447
#Part Two: 56322