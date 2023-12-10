# --- Day 5: If You Give A Seed A Fertilizer ---

import re
import timeit

class SeedMapping:
    def __init__(self, dst_range_start: int, src_range_start: int, range_len: int):
        self.dst_range_start = int(dst_range_start)
        self.src_range_start = int(src_range_start)
        self.range_len = int(range_len)

def get_intersection(a, b, x, y, dst):
    start_ab = min(a,b)
    start_xy = min(x,y)
    end_ab = max(a,b)
    end_xy = max(x,y)

    start = max(start_ab, start_xy)
    end = min(end_ab, end_xy)
    if start > end:
        return None
    else:
        minmin = min(start_ab, start_xy)
        return [start + dst - minmin , end - start]

def getMapping(result, map_name, source):
    maps = []
    for S in source:
        res = -1
        for X in result[map_name]:
            intersection = get_intersection(S[0],S[0] + S[1], X.src_range_start, X.src_range_start + X.range_len - 1, X.dst_range_start) 
            if intersection is not None:
                maps.append(intersection)
    result = maps
    return result


def getMapping_part_one(result, map_name, source):
    maps = []
    for S in source:
        res = -1
        for X in result[map_name]:
            if S >= X.src_range_start and S < X.src_range_start + X.range_len:
                res = X.dst_range_start + S - X.src_range_start
            if res < 0:
                res = S
            if res not in maps:
                maps.append(res)
    result = maps
    if len(maps) > 1:
        result = [m for m in maps if m not in source]
    return result

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
    #for mp in result['water-to-light map']:
    #    print(mp.dst_range_start, mp.src_range_start, mp.range_len)

    lowest_location = float('inf')

    seeds_two = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]

    #for S in seeds_two:
    seed = seeds_two
    soil_num = getMapping(result, 'seed-to-soil map', seed)
    #print(f'Seed: {seeds}  soil_num: {soil_num}')
    fert_num = getMapping(result, 'soil-to-fertilizer map', soil_num)
    #print(f'Seed: {soil_num}  fert_num: {fert_num}')
    water_num = getMapping(result, 'fertilizer-to-water map', fert_num)
    #print(f'Seed: {fert_num}  water_num: {water_num}')
    light_num = getMapping(result, 'water-to-light map', water_num)
    #print(f'Seed: {water_num}  light_num: {light_num}')
    temp_num = getMapping(result, 'light-to-temperature map', light_num)
    #print(f'Seed: {light_num}  temp_num: {temp_num}')
    hum_num = getMapping(result, 'temperature-to-humidity map', temp_num)
    #print(f'Seed: {temp_num}  hum_num: {hum_num}')
    loc_num = getMapping(result, 'humidity-to-location map', hum_num)
    #print(f'Seed: {temp_num}  loc_num: {loc_num}')
    print(f'Seed: {seed}  loc_num: {loc_num}')
    if min(loc_num) < lowest_location:
        lowest_location = min(loc_num)

    res_part_one = lowest_location
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