from random import randint

class Mancala():

    def __init__(self):
        """
        Initialize game board.
        Each game has
            - `board`: the current state of the game represented as a list.
            - `player_goals`: constant representing the indexes of the goals of the players.
        """

        sides = [[4 for i in range(6)] + [0] for i in range(2)]
        self.board = sides[0] + sides[1]

        self.player_goals = [6, 13]

    def player(self, state: list) -> int:
        """
        Returns the current player for state `state`.
        """
        # player 1 if more zeros on player 0's side, otherwise player 0
        return 1 if state[:self.player_goals[0]].count(0) > state[:self.player_goals[0] + 1:self.player_goals[1]].count(0) else 0

    def other_player(self, player: int) -> int:
        """
        Returns the player that is not the one passed in.
        """
        return 1 if player == 0 else 0

    def actions(self, state: list) -> list:
        """
        Returns a list of all legal actions [`i`, `i`, `i`, ...] in state `state`.
        """
        player = self.player(state)

        start = 0 if player == 0 else self.player_goals[0] + 1
        end = self.player_goals[0] if player == 0 else self.player_goals[1]
        
        # if the bucket is not empty you can take from it
        return [bn for bn, bv in enumerate(state[start:end]) if bv != 0]

    def terminal(self, state: list):
        """
        Return true if state `state` is terminal.
        """
        
        # if either side is empty the game is over
        if state[:self.player_goals[0]].count(0) == 6 or state[self.player_goals[0] + 1:self.player_goals[1]].count(0) == 6:
            return True

    def winner(self):
        return 2 if self.player_goals[0] == self.player_goals[1]
        return 0 if self.player_goals[0] > self.player_goals[1] else 1

    def result(self, state: list, action: int) -> tuple:
        """
        Return the resulting state and player as tuple `(state, player)` from taking action `action` in state `state`.
        """

        current_player = self.player(state)
        next_player = self.other_player(current_player)
        result = state[:]
        
        idx = 1

        for ln in range(result[action]):
            if action + idx >= len(state):
                idx = -action

            bucket_idx = action + idx

            # continue if opposing goal
            if bucket_idx == self.player_goals[next_player]:
                continue

            result[action + idx] += 1

            # if last stone lands in own goal, go again
            if ln + 1 == result[action] and bucket_idx == self.player_goals[current_player]:
                next_player = current_player

            idx += 1

        result[action] = 0

        return (result, next_player)

    """
    View section, seperate class later?
    """

    def print_state(self, state: list):
        """
        Prints the current `state` of the board.
        """

        # fix this lol

        print(state)

    def play(self, **kwargs):
        """
        Defaults to play against another human but you can pass in a `opponent` to play against a robot.
        """

        human = kwargs.get("human", randint(0, 1))
        opponent = kwargs.get("opponent", None)
        agent_battle = kwargs.get("agent_battle", False)

        opponent_name = opponent.get_name() if opponent else None

        while True:

            self.print_state(self.board)

            player = self.player(self.board)
            actions = self.actions(self.board)

            if not agent_battle and (not opponent or player == human):
                print(f"Player {player}'s Move.")

                while True:
                    action = int(input().strip()) - 1
                    
                    if not action in actions:
                        print('That place is already filled or invalid. Still your move.')
                    else:
                        break

            elif opponent:
                print(f"{opponent_name}'s Move.")

                action = opponent.choose_action(self.board)

                print(f"{opponent_name} distributed stones from bucket {action + 1}.")

            # update board
            self.board = self.result(self.board, action)

            # check if game over
            winner = player if self.terminal(self.board) else None 
            if winner:
                self.print_state(self.board)

                print("\nGAME OVER\n")
                print(f"Result is { "tie." if winner == 2 else f"player {winner + 1} won." }")

                break

        # kwargs make this hard                
        # if input("Play again?\n").lower() == "y":
        #     self.board = [4 for i in range(12)] + [0, 0]
        #     self.play(kwargs)

if __name__ == "__main__":
    mancala = Mancala()

    mancala.play()