# --- Day 3: Gear Ratios ---
import re
from typing import Literal


class Part_number:
    def __init__(self, value, line_num, start, end):
        self.value = value
        self.line_num = line_num
        self.start = start
        self.end = end

def brut_parsing(file_to_process):
    result = []
    with open(file_to_process, 'r') as file:
        for line_number, line_content in enumerate(file, start=0):
            c_position = 0
            for c in line_content:
                if c.isdigit() == False and c != '.' and c != '\n':
                    x = Part_number(c,line_number,c_position,c_position)
                    result.append(x)
                c_position+=1
    return result

def brut_parsing2(file_to_process):
    result = []
    with open(file_to_process, 'r') as file:
        for line_number, line_content in enumerate(file, start=0):
            value = 0
            value_start = -1
            for c_pos, c in enumerate(line_content, start = 0):
                if c.isdigit():
                    value = value * 10 + int(c)
                    if value_start < 0:
                        value_start = c_pos
                else:
                    if value > 0:
                        x = Part_number(value,line_number,value_start,c_pos-1)
                        result.append(x)
                        value_start = -1
                        value = 0
    return result





def parse_file(file_to_process, target: Literal['digits', 'symbols']):
    results = []
    with open(file_to_process, 'r') as file:
        for line_number, line_content in enumerate(file, start=0):
            if target == 'digits':
                res = re.findall(r'\d+', line_content)
            if target == 'symbols':
                res = re.findall(r'[^0-9.\n]', line_content)

            last_position = 0 
            for value in res:
                start_position = line_content.index(value, last_position)
                end_position = start_position + len(value) - 1
                last_position = end_position + 1

                obj = Part_number(value, line_number, start_position, end_position)

                results.append(obj)

    return results

def check_nearby_fields(p):
    print(p)
    return True


def main():

    res_part_one = 0
    res_part_two = 0

    file_name = 'Day 03\day03-prd.txt'

    part_numbers = parse_file(file_name,'digits')
    symbols      = parse_file(file_name,'symbols')
    xx = brut_parsing(file_name)
    pp = brut_parsing2(file_name)

    for i in range(0, pp.__len__()):
        if int(part_numbers[i].value) != int(pp[i].value) or part_numbers[i].line_num != pp[i].line_num or part_numbers[i].start != pp[i].start or part_numbers[i].end != pp[i].end:
            print("problem")


    for part in pp:
        for x in xx:
            #if part.value == 0:
            #    continue
            if abs(part.line_num - x.line_num) <= 1:
                if x.start >= part.start - 1 and x.end <= part.end + 1:
                    res_part_one +=int(part.value)
                    #print(part.value)
                    #part.value = 0
                    #break

    for symbol in symbols:
        for part in part_numbers:
            if abs(part.line_num - symbol.line_num) <= 1:
                if abs(symbol.start - part.start) <= 1 or abs(symbol.start - part.end) <= 1: 
                    res_part_two +=int(part.value)
                    #print(part.value)
                    part.value = 0
                    



    print('----------------------------')
    print('Part One:', res_part_one)
    print('Part Two:', res_part_two)

if __name__ == '__main__':
    main()

#Part One: 
# 544697 too high
# 529657 too high
# 287122 too low
# 529172 nope
# 375848 nope

#Part Two: 