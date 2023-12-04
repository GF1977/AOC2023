def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data

def parse_data(data):
    s = data.split(": ")[1];
    # Split the string into games
    games = s.split("; ")

    # Parse each game into a dictionary
    result = []
    for game in games:
        d = {}
        for item in game.split(", "):
            count, color = item.split(" ")
            d[color] = int(count)
        result.append(d)

    return result

    

def main():
    game_set =  {
        'red':  12,
        'green':13,
        'blue': 14
    }

    file_name = "Day 02\day01-dev.txt"
    file_data = parse_file(file_name)
    game_counter = 1
    for line in file_data:
        res = parse_data(line)
        print(game_counter, res)
        game_counter+=1

    res_part_one = 0
    res_part_two = 0


    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)

if __name__ == "__main__":
    main()
