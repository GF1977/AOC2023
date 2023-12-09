# --- Day 5: If You Give A Seed A Fertilizer ---

import re
import timeit

class SeedMapping:
    def __init__(self, dst_range_start: int, src_range_start: int, range_len: int):
        self.dst_range_start = dst_range_start
        self.src_range_start = src_range_start
        self.range_len = range_len




def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data

def main():
    
    file_name = "Day 05\day05-dev.txt"
    file_data = parse_file(file_name)
    seeds = {}

    result = {}
    for line in file_data:
        if "seeds:" in line:
            seeds = list(map(int, line.split(":")[1].split()))
            continue
        if line == '':
            continue
        if ':' in line:
            name, values = line.split(':')
            continue
        data = line.split(' ')
        X = SeedMapping(data[0], data[1], data[2])
        if name not in  result:
            result[name] ={X}
        else:
            result[name].add(X)

    #print(result)
    #for mp in result['fertilizer-to-water map']:
    #    print(mp.dst_range_start, mp.src_range_start, mp.range_len)

    for seed in seeds:
        print(seed)



    res_part_one = 0
    res_part_two = 0


    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

#Part One: 
#Part Two: 