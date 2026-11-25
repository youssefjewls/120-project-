# ------------------------------------------
# Atom Catcher - CHE120 Final Project
# University of Waterloo, Ontario
#
# Group members:
#   - Emerson Eliuk
#   - Kiera Yoon
#   - Umar Rawther
#   - Youssef Elgendy
#
# game_state.py | score, lives, streak and difficulty.
# Written by: Umar Rawther (UR)
# ------------------------------------------

# This file is plain Python (no pygame), so it can be tested on its own with:
#     python -m doctest game_state.py -v


def new_game():
    """ () -> dict

    Return a dictionary holding the starting values of a new game: the
    score, lives, streak and speed step.

    Keeping everything that changes during the game in one dictionary means
    main.py doesn't need lots of separate variables, and starting a new game
    resets everything at once.

    """
    # Sets up the starting values of a new game in a dictionary.
    state = {
        "score": 0,
        "lives": 3,
        "streak": 0,
        "speed_step": 0,
    }
    return state # Returns the dictionary with the starting values of a new game.


def streak_multiplier(streak):
    """ (int) -> int
    
    >>> streak_multiplier(0)
    1
    >>> streak_multiplier(9)
    1
    >>> streak_multiplier(10)
    2
    >>> streak_multiplier(25)
    3
    >>> streak_multiplier(500)
    4

    Return the streak multiplier for the given streak. I based the streak multiplier off of a popular game called Guitar Hero.
    The streak is the number of consecutive catches. The streak multiplier is 1 for a streak of 0-9, 2 for a streak of 10-19, 3 for a streak of 20-29, and 4 for a streak of 30 or more.
    """
    if streak < 10:
        return 1
    elif streak < 20:
        return 2
    elif streak < 30:
        return 3
    else:
        return 4

