import timeit
import math


def parse_file(file_to_process: str):
    with open(file_to_process, mode="r") as file:
        data = file.read().split("\n")
    
    all_nodes = {}
    a_only_nodes = []
    lr_instruction = ""
    for n, line in enumerate(data):
        if n == 0:
            lr_instruction = line
            continue
        if line == "":
            continue
        name, left_node, right_node = parse_map_node(line)
        all_nodes[name] = [left_node, right_node]
        if name[-1] == "A":
            a_only_nodes.append(name)
    return lr_instruction, all_nodes, a_only_nodes


def parse_map_node(line: str):
    parts = line.split("=")
    name = parts[0].strip()
    neighbours = parts[1].strip().strip("()").split(",")
    left_node = neighbours[0].strip()
    right_node = neighbours[1].strip()

    return name, left_node, right_node


def solve_part_one(nodes: dict, current_node: str, lr_instruction: str):
    i = 0
    len_inst = len(lr_instruction)
    while current_node[-1] != "Z":
        # print(current_node)
        if lr_instruction[i % len_inst] == "L":
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        i += 1
    return i


def find_gcd(numbers):
    gcd = numbers[0]
    for num in numbers[1:]:
        gcd = math.gcd(gcd, num)
    return gcd


def main():
    file_name = "Day 08\\day08-prd.txt"
    lr_instruction, nodes, start_nodes = parse_file(file_name)
    res_part_one = solve_part_one(nodes, "AAA", lr_instruction)

    res = []
    res_part_two = 1
    current_nodes = start_nodes
    for current_node in current_nodes:
        r = solve_part_one(nodes, current_node, lr_instruction)
        res.append(r)
        res_part_two *= int(r)

    gcd = find_gcd(res)
    res_part_two = int(res_part_two / (gcd**5))

    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

# Part One: 19637
# Part Two: 8811050362409
