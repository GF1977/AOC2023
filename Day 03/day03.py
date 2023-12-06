# --- Day 3: Gear Ratios ---
import re

class Part_number:
    def __init__(self, value, line_num, start, end):
        self.value = value
        self.line_num = line_num
        self.start = start
        self.end = end

def parse_file(file_to_process):
    results_digit = []
    results_symb = []
    
    with open(file_to_process, 'r') as file:
        for line_number, line_content in enumerate(file, start=0):
            results_digit.extend(find_matches(line_content, r'\d+', line_number))
            results_symb.extend(find_matches(line_content, r'[^0-9.\n]', line_number))
    
    return results_digit, results_symb

def find_matches(line_content, pattern, line_number):
    matches = re.finditer(pattern, line_content)
    results = []
    
    for match in matches:
        start_position = match.start()
        end_position = match.end() - 1
        value = match.group()
        results.append(Part_number(value, line_number, start_position, end_position))
    
    return results

def main():
    res_part_one = 0
    res_part_two = 0
    file_name = 'Day 03\day03-dev.txt'
    part_numbers,symbols = parse_file(file_name)

    for symbol in symbols:
        for part in part_numbers:
            if abs(part.line_num - symbol.line_num) <= 1:
                if abs(symbol.start - part.start) <= 1 or abs(symbol.start - part.end) <= 1: 
                    res_part_one +=int(part.value)
                    part.value = 0

    print('----------------------------')
    print('Part One:', res_part_one)
    print('Part Two:', res_part_two)

if __name__ == '__main__':
    main()

#Part One: 529618
#Part Two: 