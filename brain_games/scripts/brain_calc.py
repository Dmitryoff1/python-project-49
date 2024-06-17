#!/usr/bin/env python

from brain_games.games.calc import generate_game_data, RULES_MESSAGE
from brain_games.logic.game_logic import run_game


def main():
    run_game(RULES_MESSAGE, generate_game_data)


if __name__ == '__main__':
    main()
