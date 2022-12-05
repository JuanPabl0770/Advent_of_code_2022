
class RockPaperScissorsStrategyDealer:

    shape_points = {'X':1, 'Y':2, 'Z':3 }
    game_logic = {
        ('A','X'): 3,
        ('A','Y'): 6,
        ('A','Z'): 0,
        
        ('B','X'): 0,
        ('B','Y'): 3,
        ('B','Z'): 6,
        
        ('C','X'): 6,
        ('C','Y'): 0,
        ('C','Z'): 3
    }

    game_logic_p2 = {
        ('A','X'): 'Z',
        ('A','Y'): 'X',
        ('A','Z'): 'Y',
        
        ('B','X'): 'X',
        ('B','Y'): 'Y',
        ('B','Z'): 'Z',
        
        ('C','X'): 'Y',
        ('C','Y'): 'Z',
        ('C','Z'): 'X'
    }


    def follow_strategy(self, strategy):

        points = 0

        for line in strategy:
            turn = line.strip().split()
            points += self.get_points_from_turn(turn[0], turn[1])

        return points
    
    def get_points_from_turn(self, elf_play, round_outcome):
        player_play = self.game_logic_p2.get((elf_play,round_outcome))
        print(round_outcome, player_play)
        return self.shape_points.get(player_play) + self.game_logic.get((elf_play, player_play))



strategy_file = open('day02\input.txt', 'r')
strategy_dealer = RockPaperScissorsStrategyDealer()
print( strategy_dealer.follow_strategy( strategy_file ) )



