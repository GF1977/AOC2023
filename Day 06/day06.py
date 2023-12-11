import re
import timeit

def parse_file(file_to_process):
    with open(file_to_process, 'r') as f:
        time_list = f.readline().strip().split(':')[1].split()
        distance_list = f.readline().strip().split(':')[1].split()

    time_list = [int(time) for time in time_list]
    distance_list = [int(distance) for distance in distance_list]

    result = []
    for i in range(0, len(time_list)):
        result.append([time_list[i],distance_list[i]])

    return result

def get_winning_combination(time, dist):
    count_of_winning_combinations = 0
    for i in range(0, time + 1):
        current_distance = i * (time - i)
        if current_distance > dist:
            print (f'Time to hold button: {i} ms     Distance: {current_distance}')
            count_of_winning_combinations+=1

    return count_of_winning_combinations

def main():
    
    file_name = "Day 06\day06-prd.txt"
    race_list = parse_file(file_name)

    res_part_one = 1
    for race in race_list:
        print(race)
        x = get_winning_combination(time = race[0], dist = race[1])
        print(race, x)
        res_part_one *= x



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