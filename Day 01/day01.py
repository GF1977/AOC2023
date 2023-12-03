import re

def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data

def get_digits(s):
    digits = "".join(filter(str.isdigit, s))
    if digits == "":
        return 0
    
    return int(digits[0] + digits[digits.__len__() - 1])
        
def normalize_line(s):
    calibration_dict = [("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9"), ("zero", "0")]
    position = s.__len__()
    first_word = ""
    first_num = 0
    word_was_found = False
    for word, nummer in calibration_dict:
        position_new = s.find(word)
        if position_new < position and position_new >= 0: 
            position = position_new
            first_word = word
            first_num = nummer
            word_was_found = True
            

    if word_was_found:
        s = re.sub(first_word, first_num, s)
        return s

    return s

def normalize_line_back(s):
    calibration_dict = [("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9"), ("zero", "0")]
    position = s.__len__()
    first_word = ""
    first_num = 0
    for i in range(len(s)-1):
        for word, nummer in calibration_dict:
            position_new = s.find(word,s.__len__()-i-5)
            if position_new < position and position_new >= 0: 
                position = position_new
                first_word = word
                first_num = nummer
                s = re.sub(first_word, first_num, s)
                return s

    return s



def replace_first_digit(s):
    calibration_dict = [("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9")]
    for i in range(len(s)-1):
        for word, nummer in calibration_dict:
            #if s.__len__() > i+word.__len__():
                substring = s[i:i+word.__len__()]
                if word == substring:
                    s = re.sub(word, nummer, s)
                    return s
        if any(char.isdigit() for char in substring):
            return s
        

    return s

def replace_last_digit(s):
    calibration_dict = [("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9")]
    for i in range(len(s)):
        for word, nummer in calibration_dict:
            #if (s.__len__() - i - word.__len__())>=0:
                substring = s[-word.__len__()-i:]
                substring = substring[0:word.__len__()]
                if word == substring:
                    s = re.sub(word, nummer, s)
                    return s
        if any(char.isdigit() for char in substring):
            return s
        
    return s

def super_new(s):

    calibration_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

    best_first_word = ""
    best_last_word = ""
    best_first_position = s.__len__()
    best_last_position = 0

    for word in calibration_dict:
        matches = [match.start() for match in re.finditer(word, s)]
        if matches.__len__() == 0:
            continue
        
        if matches[0] < best_first_position:
            best_first_position = matches[0]
            best_first_word = word
    
    if best_first_word in calibration_dict:
        nummer = calibration_dict[best_first_word]
        s = re.sub(best_first_word, nummer, s)


    for word in calibration_dict:
        matches = [match.start() for match in re.finditer(word, s)]
        if matches.__len__() == 0:
            continue

        if matches[matches.__len__()-1] > best_last_position:
            best_last_position = matches[matches.__len__()-1]
            best_last_word = word

    if best_last_word in calibration_dict:
        nummer = calibration_dict[best_last_word]
        s = re.sub(best_last_word, nummer, s)

    return s
        


def main():
    
    file_name = "Day 01\day01-prd.txt"
    file_data = parse_file(file_name)

    res_part_one = 0
    res_part_two = 0
    res_part_x = 0

    for line in file_data:
        calibration_values = get_digits(line)
        res_part_one += calibration_values


    calibration_values = 0
    for line in file_data:
        normalized_line = super_new(line)
        #normalized_line = normalize_line_back(normalized_line)
        calibration_values_sol1 = get_digits(normalized_line)
        res_part_x+=calibration_values_sol1

        new_s1 = replace_first_digit(line)
        new_s2 = replace_last_digit(new_s1)
        calibration_values = get_digits(new_s2)
        res_part_two += calibration_values

        if calibration_values_sol1 != calibration_values:
            print(line, normalized_line,calibration_values_sol1, new_s2, calibration_values) 
        
        


    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)
    print("Part X:", res_part_x)

if __name__ == "__main__":
    main()


# 55346 too low
# 55351 nooo
# 55352 too low
# 55356 no
# 55357 no
# 55359 too high