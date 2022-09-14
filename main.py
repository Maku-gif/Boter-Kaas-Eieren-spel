from bke import EvaluationAgent, start, can_win

class MijnS(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    return random.randint(1,500)

my_random_agent = MyRandomAgent()
start(player_o=my_random_agent, player_x = my_random_agent)