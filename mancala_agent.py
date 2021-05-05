from random import choice

from mancala import Mancala

class MancalaAgent(Mancala):

    def __init__(self, **kwargs):
        """
        Parameters here...
        """
    
    def get_name(self) -> str:
        return "Mancala Agent"
    
    def get_move(self, state: list, player: int) -> int:
        return choice(self.actions(state, player))

        
