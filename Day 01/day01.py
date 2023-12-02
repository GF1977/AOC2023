import os
import sys
import argparse

def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data

def main():
    
    file_name = "Day 01\day01.txt"
    file_data = parse_file(file_name)
    print(file_data)
    print("----------------------------")
    print("Part One:", 1)
    print("Part Two:", 2)

if __name__ == "__main__":
    main()