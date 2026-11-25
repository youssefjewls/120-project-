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
        "score": 0, # The score starts at 0.
        "lives": 3, # The player starts with 3 lives.
        "streak": 0, # The streak starts at 0.
        "speed_step": 0, # The speed step starts at 0.
        "next_life_at": 1000, # The player starts with 3 lives, and will gain an extra life at 1000 points.
    }
    return state # Returns the dictionary with the starting values of a new game.


def streak_multiplier(streak):
    """ (int) -> int

    Return the streak multiplier for the given streak. I based the streak multiplier off of a popular game called Guitar Hero.
    The streak is the number of consecutive catches. The streak multiplier is 1 for a streak of 0-9, 2 for a streak of 10-19, 3 for a streak of 20-29, and 4 for a streak of 30 or more.

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
    """
    if streak < 10:
        return 1
    elif streak < 20:
        return 2
    elif streak < 30:
        return 3
    else:
        return 4

def add_points(state, points):
    """ (dict, int) -> NoneType

    Add the given points to the game state and update the score and lives accordingly.

    >>> s = new_game()
    >>> s["lives"] = 2
    >>> add_points(s, 1000)
    >>> s["score"], s["lives"]
    (1000, 3)
    """
    state["score"] += points
    while state["score"] >= state["next_life_at"]:
        state["next_life_at"] += 1000
        if state["lives"] < 3:
            state["lives"] += 1

def lose_life(state):
    """ (dict) -> NoneType

    Lose a life, reset the streak to 0, and slow the game down by 2 speed steps.

    >>> s = new_game()
    >>> s["streak"] = 12
    >>> lose_life(s)
    >>> s["lives"], s["streak"]
    (2, 0)
    """
    state["lives"] -= 1 # Lose a life.
    state["streak"] = 0 # Reset the streak to 0 when a life is lost.
    state["speed_step"] = max(0, state["speed_step"] - 2) # Decreases the speed by a step of 2. Max is used to keep speed step from going below 0.