def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data

def parse_data(data):
    games = data.split(": ")[1].split("; ")

    # Parse each game into a dictionary
    result = []
    for game in games:
        d = {}
        for item in game.split(", "):
            count, color = item.split(" ")
            d[color] = int(count)
        result.append(d)

    return result

def is_game_possible(games):
    game_set =  {'red':  12, 'green':13, 'blue': 14}

    for game in games:
        if  ("red"   in game and game["red"]   > game_set["red"]  ) or \
            ("green" in game and game["green"] > game_set["green"]) or \
            ("blue"  in game and game["blue"]  > game_set["blue"] ):
            return False

    return True

def main():


    res_part_one = 0
    res_part_two = 0


    file_name = "Day 02\day02-prd.txt"
    file_data = parse_file(file_name)
    game_counter = 1
    for line in file_data:
        game = parse_data(line)
        if is_game_possible(game):
            res_part_one+=game_counter
        
        game_counter+=1

    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)

if __name__ == "__main__":
    main()

#Part One: 2447
#Part Two: 0