from random import randint
from time import sleep

class Round:
    """Round represents the rounds.
    
    Attributes:
        initial_round: A random choice between 1 and 2."""
    def __init__(self) -> None:
        self.__initial_round = randint(1,2)
        self.round = self.__initial_round
    
    def next(self) -> None:
        """Skips the round."""
        self.round += 1
        return

    def timer(self) -> None:
        """Prints a timer"""
        sleep(1)
        print("\n3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        return

    def separator(self) -> None:
        """Prints a separator line."""
        print("--------------------------------------------------")
    
