# --- Day 5: If You Give A Seed A Fertilizer ---
import timeit

class SeedMapping:
    def __init__(self, dst_range_start: int, src_range_start: int, range_len: int):
        self.dst_range_start = int(dst_range_start)
        self.src_range_start = int(src_range_start)
        self.range_len = int(range_len)

def get_intersection(obj_start, obj_range, map):
    start = max(obj_start, map.src_range_start)
    end = min(obj_start + obj_range, map.src_range_start + map.range_len)
    if start > end:
        return None
    else:
        return [start + (map.dst_range_start - map.src_range_start), end - start - 1]

def get_mapping(result, map_name, source):
    global_map = []
    for S in source:
        maps = []
        for map in result[map_name]:
            intersection = get_intersection(obj_start = S[0], obj_range = S[1], map = map) 
            if intersection is not None:
                maps.append(intersection)
        if len(maps) == 0:
            maps.append(S)
        global_map += maps
    return global_map

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

def parse_data(file_data):
    seeds = []
    mapping_name = []
    result = {}

    name = None
    for line in file_data:
        if "seeds:" in line:
            seeds = list(map(int, line.split(":")[1].split()))
        elif line.strip() == '':
            continue
        elif ':' in line:
            name, values = line.split(':')
            result[name] = set()
            mapping_name.append(name)
        else:
            data = list(map(int, line.split()))
            result[name].add(SeedMapping(data[0], data[1], data[2]))
            
    return seeds, result, mapping_name


def main():
    
    file_name = "Day 05\day05-prd.txt"
    file_data = parse_file(file_name)
    seeds, result, mapping_name = parse_data(file_data)

    tmp_res_one = seeds
    tmp_res_two = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]
    for name in mapping_name:
        tmp_res_one = getMapping_part_one(result, name, tmp_res_one)
        tmp_res_two = get_mapping(result, name, tmp_res_two)


    lowest_location = float('inf')
    for l_n in tmp_res_two:
        if l_n[0] < lowest_location:
            lowest_location = l_n[0]

    res_part_one = min(tmp_res_one)
    res_part_two = lowest_location

    if res_part_two != 56931769:
        print(" Noooooooooooooooooooooooooooooooooooooo !")

    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

#Part One: 486613012
#Part Two: 56931769