import random
from bke import EvaluationAgent, start, can_win 
from bke import MLAgent, is_winner, opponent, train, save, load, RandomAgent, train_and_plot 

class MyAgent(MLAgent):
  def evaluate(self, board):
    if is_winner(board, self.symbol):
        reward = 1
    elif is_winner(board, opponent[self.symbol]):
        reward = -1
    else:
      reward = 0
    return reward
class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    return random.randint(1,500)
class MijnSpeler(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = 1
    if can_win(board, opponent_symbol):
      getal = getal - 1000
    return getal


def menu():
  print("--------------------------------------------------------")
  print("*** WELKOM BIJ HET SPELLETJE Boter-Kaas-Eieren ***")
  print("--------------------------------------------------------")
  print("[1] Tegen een domme tegenstander spelen")
  print("[2] Tegen een slimme tegenstander spelen")
  print("[3] Tegen een ander persoon spelen")
  print("[4] Train je tegenstander")
  print("[5] Plot een validatiegrafiek")
  print("[6] Uitleg over hyperparameters")
  print("[7] Verlaat het spel")
menu()
optie = int(input("Kies een optie:"))

while optie != 7:
    if optie == 1:
      my_random_agent = MyRandomAgent()
      start(player_o = my_random_agent)

    if optie == 2:
      mijn_speler = MijnSpeler()
      start(player_x = mijn_speler)
      
    if optie == 3:
      start()

    if optie == 4:
      my_agent = MyAgent()
      train(my_agent, 3000)
      save(my_agent, 'MyAgent_3000')
      my_agent = MyAgent()
      my_agent = load('MyAgent_3000')
      my_agent.learning = True
      start(player_x=my_agent)

    if optie == 5:     
      random.seed(1)
      random_agent = RandomAgent()
      my_agent = load('MyAgent_3000')
      train_and_plot(
        agent=my_agent,
        validation_agent= random_agent,
        iterations=20,
        trainings=100,
        validations=1000)
      my_agent = MyAgent(alpha=0.1, epsilon=0.8)

    if optie == 6:
      print("------------------------------------------------------------------")
      print("Alpha:")
      print("hiermee kan je bepalen hoe snel de 'agent' nieuwe kennis over oude kennis zal kiezen en/of zal gebruiken. De agent staat hierbij standaard op 1.0. Als dit floatinggetal hoog is, zal de agent eerder nieuwe kennis proberen te vergaren dan oude kennis.")

      print("Ëpsilon:")
      print("hiermee kun je bepalen hoe snel de 'agent' nieuwe kennis wilt opdoen. De agent staat standaard op 0.1. Als dit floatinggetal hoog is, zal de agent eerder meer willekeurige acties uitvoeren dan al bekende zetten.")

    else:
      print("Ongeldige keuze")

    menu()
    optie = int(input("Kies een optie:"))
print("Bedankt voor het spelen en tot ziens!")


