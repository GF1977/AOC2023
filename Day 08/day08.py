import timeit
import math

def parse_file(file_to_process: str) -> list[str]:
    with open(file_to_process, mode="r") as file:
        data = file.read().split("\n")
    return data


def parse_map_node(line: str):
    parts = line.split("=")
    name = parts[0].strip()
    neighbours = parts[1].strip().strip("()").split(",")
    left_node = neighbours[0].strip()
    right_node = neighbours[1].strip()

    return name, left_node, right_node


def find_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    divisors.append(n)
    return sorted(divisors)
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def solve_diophantine(a, b, c):
    gcd, x, y = extended_gcd(a, b)
    if c % gcd != 0:
        return None  # No solution
    x *= c // gcd
    y *= c // gcd
    dx = b // gcd
    dy = a // gcd
    solutions = [(x + i * dx, y - i * dy) for i in range(-abs(c // dx), abs(c // dy) + 1)]
    return solutions

def solve_part_one(nodes: dict, current_node: str, lr_instruction: str):
    i = 0
    len_inst = len(lr_instruction)
    while current_node[-1] != 'Z':
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
    file_data = parse_file(file_name)

    nodes = {}
    start_nodes = []
    lr_instruction = ""
    for n, line in enumerate(file_data):
        if n == 0:
            lr_instruction = line
            continue
        if line == "":
            continue
        name, left_node, right_node = parse_map_node(line)
        nodes[name] = [left_node, right_node]
        if name[-1] == "A":
            start_nodes.append(name)

    res_part_one = solve_part_one(nodes, 'AAA', lr_instruction)
    print(res_part_one)

    i = 0
    current_nodes = start_nodes
    end_of_cycle = False

    print(find_divisors(922939))
    print(find_divisors(19637))
    print(find_divisors(12643))
    print(extended_gcd(19637,12643))
    #qqq =solve_diophantine(19637, -12643, 922939)
    #print(qqq)

    
    #current_nodes = [current_nodes[0]]
    res = []
    part_two = 1
    for current_node in current_nodes:
        r = solve_part_one(nodes, current_node, lr_instruction)
        res.append(r)
        part_two *= int(r)
        print(part_two)
        
    gcd = find_gcd(res)
    part_two = part_two/(gcd**6)
    print(res)
    print(int(part_two))
    return


    while True:
        #print(current_nodes, lr_instruction[i % len_inst])

        tmp_nodes = []
        for current_node in current_nodes:
            if lr_instruction[i % len_inst] == "L":
                tmp_nodes.append(nodes[current_node][0])
            else:
                tmp_nodes.append(nodes[current_node][1])
        current_nodes = tmp_nodes

        end_of_cycle = True
        for node in current_nodes:
            if node[-1] != "Z":
                end_of_cycle = False
                break
        if end_of_cycle == True:
            print(i)
            #i = 0
        i+=1


    res_part_two = i

    print("----------------------------")
    print("Part One:", 0)
    print("Part Two:", res_part_two)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

# Part One: 19637
# Part Two: 8811050362409
