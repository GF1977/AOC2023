def parse_file(file_to_process):
    file = open(file_to_process, mode='r')
    data: list[str] = file.read().split('\n')
    return data


def main():

    res_part_one = 0
    res_part_two = 0

    file_name = 'Day 02\day02-prd.txt'
    file_data = parse_file(file_name)

    print('----------------------------')
    print('Part One:', res_part_one)
    print('Part Two:', res_part_two)

if __name__ == '__main__':
    main()

#Part One: 2447
#Part Two: 56322