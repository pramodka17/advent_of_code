import regex as re
from word2number import w2n


def process_game_input():
    color_map = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    game_id_sum = 0

    with open('day2-input.txt', 'r') as file:
        for line in file:
            game_split = line.strip().split(':')
            game_id = int(game_split[0][5:])
            draws = game_split[1].strip().split(';')

            valid_game = True
            for draw in draws:
                balls = draw.strip().split(',')
                for ball in balls:
                    splits = ball.strip().split()
                    count = int(splits[0])
                    color = splits[1].lower()

                    if color not in color_map.keys():
                        valid_game = False
                        break

                    if count > color_map.get(color):
                        valid_game = False
                        break

                if not valid_game:
                    break

            if valid_game:
                game_id_sum += game_id
                print(game_id)

    return game_id_sum


def process_game_input_for_power():
    power_sum = 0

    with open('day2-input.txt', 'r') as file:
        for line in file:
            game_split = line.strip().split(':')
            draws = game_split[1].strip().split(';')

            valid_game = True
            color_map = {
                "red": 0,
                "green": 0,
                "blue": 0
            }

            for draw in draws:
                balls = draw.strip().split(',')
                for ball in balls:
                    splits = ball.strip().split()
                    count = int(splits[0])
                    color = splits[1].lower()

                    if color not in color_map.keys():
                        valid_game = False
                        break

                    if count > color_map.get(color):
                        color_map[color] = count

                if not valid_game:
                    break

            if valid_game:
                power_sum += color_map["red"] * color_map["green"] * color_map["blue"]

    return power_sum


if __name__ == '__main__':
    print(process_game_input_for_power())
