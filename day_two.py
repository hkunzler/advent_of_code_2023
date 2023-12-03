import math

with open('day_two_input_data.txt', 'r') as f:
    data = f.read()
    data = data.split('\n')


def get_formatted_games(game_data):
    games = []
    for game in game_data:
        game_id, *color_data = game.strip().split(':')

        if game_id:
            rounds = []
            for color_data in color_data[0].split(';'):
                color_pairs = {}
                for color in color_data.split(','):
                    items = color.strip().split()
                    if len(items) == 2:
                        count, color_name = items
                        color_pairs[color_name] = color_pairs.get(color_name, 0) + int(count)
                rounds.append(color_pairs)

            games.append({'Game': game_id, 'Rounds': rounds})

    return games


def get_min_needed_colors(games):
    min_amount = {}
    for game in games:
        rounds = game['Rounds']
        min_colors = {}
        for each_round in rounds:
            for color, count in each_round.items():
                min_colors[color] = max(min_colors.get(color, 0), count)
        min_amount[game['Game']] = min_colors
    return min_amount


def get_possible_games(all_games, color_options):
    games = []
    for game in all_games:
        rounds = game['Rounds']

        if all(color in color_options and each_round[color] <= color_options[color]
               for each_round in rounds for color in each_round):
            games.append(game['Game'])

    return games


formatted_games = get_formatted_games(data)

current_color_options = {
    'red': 12,
    'green': 13,
    'blue': 14
}

possible_games = get_possible_games(formatted_games, current_color_options)

possible_game_id_sum = sum(int(game.split(' ')[1]) for game in possible_games)

min_colors_needed = get_min_needed_colors(formatted_games)

game_power = {game: math.prod(min_colors_needed[game].values()) for game in min_colors_needed}

sum_of_game_power = sum(game_power.values())

print('Sum of the game ids of the possible games: ', possible_game_id_sum)

print('Sum of the power of the minimum set of cubes: ', sum_of_game_power)
