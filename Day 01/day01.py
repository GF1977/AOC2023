def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data

def get_digits(s):
    digits = "".join(filter(str.isdigit, s))
    if digits == "":
        return 0
    
    return int(digits[0] + digits[digits.__len__() - 1])
        

def main():
    
    file_name = "Day 01\day01-dev.txt"
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