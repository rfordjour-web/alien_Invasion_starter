"""
Lab Name: Game Stats
Author: Rosemond Fordjour
Purpose: defines the behavior and properties of a single bullet,
 including its size, speed, position, and how it moves on the screen.
 Date: November 30, 2025

"""





class GameStats:
    """Track statistics for the game."""

    def __init__(self, ship_limit):
        self.ships_left = ship_limit  