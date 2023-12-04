with open('day_three_input_data.txt', 'r') as f:
    map_area = f.read()
    map_area = map_area.split('\n')
    map_area = [list(row) for row in map_area]


def get_special_chars(char=None):
    special_chars = ['*', '#', '+', '$', '%', '&', '@', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', '=', '-', '_',
                     '^', '~', '`', ':', ';', ',', '|', '/']
    return [(row, col) for row in range(len(map_area))
            for col in range(len(map_area[row]))
            if map_area[row][col] == char or (not char and map_area[row][col] in special_chars)]


def find_multi_digit_number(pos, horizontal=True):
    row, col = pos
    start, end = col if horizontal else row, col if horizontal else row

    if horizontal:
        while start > 0 and map_area[row][start - 1].isdigit():
            start -= 1
        while end + 1 < len(map_area[row]) and map_area[row][end + 1].isdigit():
            end += 1
    else:
        while start > 0 and map_area[start - 1][col].isdigit():
            start -= 1
        while end + 1 < len(map_area) and map_area[end + 1][col].isdigit():
            end += 1

    return start, end


def get_full_number_at_pos(pos):
    row, col = pos

    start_col, end_col = find_multi_digit_number(pos)
    if start_col != end_col:
        return ''.join(map_area[row][start_col:end_col + 1])

    start_row, end_row = find_multi_digit_number(pos, horizontal=False)
    if start_row != end_row:
        return ''.join(map_area[row][col] for row in range(start_row, end_row + 1))

    if map_area[row][col].isdigit():
        return map_area[row][col]

    return None


def get_pos_of_adjacent_numbers(pos):
    adjacent_numbers = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def is_valid_position(row, col):
        return 0 <= row < len(map_area) and 0 <= col < len(map_area[row])

    for row_offset, col_offset in directions:
        row, col = pos[0] + row_offset, pos[1] + col_offset
        if is_valid_position(row, col) and map_area[row][col].isdigit():
            number = get_full_number_at_pos((row, col))
            if number and number not in adjacent_numbers:
                adjacent_numbers.append(number)

    return adjacent_numbers


def get_all_adjacent_numbers():
    adjacent_numbers = []

    for special_char_pos in get_special_chars():
        adjacent_numbers.extend(get_pos_of_adjacent_numbers(special_char_pos))

    return adjacent_numbers


all_adjacent_numbers = get_all_adjacent_numbers()

adjacent_number_values = [int(num) for num in all_adjacent_numbers if num is not None]

filtered_parts = list(filter(lambda x: len(x) == 2, list(map(get_pos_of_adjacent_numbers, get_special_chars('*')))))

product_of_two_filtered_parts = [int(num[0]) * int(num[1]) for num in filtered_parts]

print('Sum of all part numbers: ', sum(adjacent_number_values))

print('Sum of all gear ratios: ', sum(product_of_two_filtered_parts))
