from typing import List

import regex as re
from word2number import w2n


def is_symbol(char: str):
    return char != '.' and not char.isalnum() and not char.isspace()


def is_star(char: str):
    return char == '*'


def is_valid_part_number(char_2d_array: List[List[str]], i: int, start_j: int, end_j: int) -> bool:
    min_j = start_j - 1 if start_j > 0 else start_j
    max_j = end_j + 1 if end_j < len(char_2d_array[0]) - 1 else end_j

    if start_j > 0:
        adj_char = char_2d_array[i][min_j]
        if is_symbol(adj_char):
            print(adj_char)
            return True  # symbol

    if end_j < len(char_2d_array[i]) - 1:
        adj_char = char_2d_array[i][max_j]
        if is_symbol(adj_char):
            print(adj_char)
            return True  # symbol

    # check previous row
    if i > 0:
        for j in range(min_j, max_j + 1):
            adj_char = char_2d_array[i - 1][j]
            if is_symbol(adj_char):
                print(adj_char)
                return True  # symbol

    # check next row
    if i < len(char_2d_array) - 1:
        for j in range(min_j, max_j + 1):
            adj_char = char_2d_array[i + 1][j]
            if is_symbol(adj_char):
                print(adj_char)
                return True  # symbol

    return False


def populate_star_map(star_map, char_2d_array: List[List[str]], i: int, start_j: int, end_j: int, part_number):
    min_j = start_j - 1 if start_j > 0 else start_j
    max_j = end_j + 1 if end_j < len(char_2d_array[0]) - 1 else end_j

    if start_j > 0:
        adj_char = char_2d_array[i][min_j]
        if is_star(adj_char):
            print(part_number)
            star_map[(i, min_j)].append(part_number)

    if end_j < len(char_2d_array[i]) - 1:
        adj_char = char_2d_array[i][max_j]
        if is_star(adj_char):
            print(part_number)
            star_map[(i, max_j)].append(part_number)

    # check previous row
    if i > 0:
        for j in range(min_j, max_j + 1):
            adj_char = char_2d_array[i - 1][j]
            if is_star(adj_char):
                print(part_number)
                star_map[(i - 1, j)].append(part_number)

    # check next row
    if i < len(char_2d_array) - 1:
        for j in range(min_j, max_j + 1):
            adj_char = char_2d_array[i + 1][j]
            if is_star(adj_char):
                print(part_number)
                star_map[(i + 1, j)].append(part_number)


def process_engine_schematic():
    char_2d_array = []
    with open('day3-input.txt', 'r') as file:
        for line in file:
            # Remove newline character at the end of each line
            line = line.rstrip()
            # Convert the line into a list of characters
            char_list = list(line)
            # Append the list of characters to the 2D array
            char_2d_array.append(char_list)

    lines_count = len(char_2d_array)
    line_length = len(char_2d_array[0])
    part_sum = 0

    for i in range(lines_count):
        is_part_number = False
        current_part_number = 0
        part_number_start_index = -1
        for j in range(line_length):
            if char_2d_array[i][j].isdigit():
                current_part_number = 10 * current_part_number + int(char_2d_array[i][j])
                if is_part_number is False:
                    is_part_number = True
                    part_number_start_index = j
            else:
                if is_part_number is True:
                    part_number_end_index = j - 1
                    print(str(current_part_number) + ' ' + str(part_number_start_index) + ' ' + str(
                        part_number_end_index))
                    if is_valid_part_number(char_2d_array, i, part_number_start_index, part_number_end_index):
                        part_sum += current_part_number

                is_part_number = False
                current_part_number = 0
                part_number_start_index = -1

        if is_part_number is True:
            part_number_end_index = line_length - 1
            if is_valid_part_number(char_2d_array, i, part_number_start_index, part_number_end_index):
                part_sum += current_part_number

    return part_sum


def process_engine_schematic_2():
    char_2d_array = []
    star_map = {}
    with open('day3-input.txt', 'r') as file:
        for line in file:
            # Remove newline character at the end of each line
            line = line.rstrip()
            # Convert the line into a list of characters
            char_list = list(line)
            # Append the list of characters to the 2D array
            char_2d_array.append(char_list)

    lines_count = len(char_2d_array)
    line_length = len(char_2d_array[0])
    part_sum = 0

    for i in range(lines_count):
        for j in range(line_length):
            star_map[(i, j)] = []

    for i in range(lines_count):
        is_part_number = False
        current_part_number = 0
        part_number_start_index = -1
        for j in range(line_length):
            if char_2d_array[i][j].isdigit():
                current_part_number = 10 * current_part_number + int(char_2d_array[i][j])
                if is_part_number is False:
                    is_part_number = True
                    part_number_start_index = j
            else:
                if is_part_number is True:
                    part_number_end_index = j - 1
                    populate_star_map(star_map, char_2d_array, i, part_number_start_index, part_number_end_index,
                                      current_part_number)

                is_part_number = False
                current_part_number = 0
                part_number_start_index = -1

        if is_part_number is True:
            part_number_end_index = line_length - 1
            populate_star_map(star_map, char_2d_array, i, part_number_start_index, part_number_end_index,
                              current_part_number)

    for i in range(lines_count):
        for j in range(line_length):
            if len(star_map[(i, j)]) == 2:
                part_sum += star_map[(i, j)][0] * star_map[(i, j)][1]


    print(star_map)
    return part_sum


if __name__ == '__main__':
    print(process_engine_schematic_2())
