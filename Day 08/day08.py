import timeit


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

    # i = 0
    # current_node = "AAA"
    len_inst = len(lr_instruction)
    # while current_node != "ZZZ":
    #     # print(current_node)
    #     if lr_instruction[i % len_inst] == "L":
    #         current_node = nodes[current_node][0]
    #     else:
    #         current_node = nodes[current_node][1]

    #     i += 1

    # res_part_one = i

    i = 0
    current_nodes = start_nodes
    end_of_cycle = False
    while not end_of_cycle:
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
# Part Two:
