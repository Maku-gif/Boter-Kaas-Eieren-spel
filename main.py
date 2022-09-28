def menu():
  print("*** WELKOM BIJ HET SPELLETJE Boter-Kaas-Eieren ***")
  print("--------------------------------------------------------")
  print("Om tegen een domme tegenstander te spelen, toets [1]")
  print("Om tegen een slimme tegenstander te spelen, toets [2]")
  print("Om tegen een ander persoon te spelen, toets [3]")
  print("Om je tegenstander te trainen, toets [4]")
  print("Om een validatiegrafiek te plotten toets [5]")
  print("Om het spel te verlaten, toets [6]")
menu()
optie = int(input("Kies een optie"))

while optie != 6:
    if optie == 1:
      import random
      from bke import EvaluationAgent, start
      class MyRandomAgent(EvaluationAgent):
        def evaluate(self, board, my_symbol, opponent_symbol):
          return random.randint(1,500)
      my_random_agent = MyRandomAgent()
      start(player_o = my_random_agent)

    if optie == 2:
      from bke import EvaluationAgent, start, can_win
      class MijnSpeler(EvaluationAgent):
        def evaluate(self, board, my_symbol, opponent_symbol):
          getal = 1
          if can_win(board, opponent_symbol):
             getal = getal - 1000
          return getal
      mijn_speler = MijnSpeler()
      start(player_o = mijn_speler)

    if optie == 3:
      from bke import start
      start()

    if optie == 4:
      from bke import MLAgent, is_winner, opponent, train, save
      class MyAgent(MLAgent):
        def evaluate(self, board):
          if is_winner(board, self.symbol):
              reward = 1
          elif is_winner(board, opponent[self.symbol]):
              reward = -1
          else:
              reward = 0
          return reward
      my_agent = MyAgent()
      train(my_agent, 3000)
      save(my_agent, 'MyAgent_3000')

      from bke import MLAgent, is_winner, opponent, train, load, start
      class MyAgent(MLAgent):
        def evaluate(self, board):
          if is_winner(board, self.symbol):
              reward = 1
          elif is_winner(board, opponent[self.symbol]):
              reward = -1
          else:
              reward = 0
          return reward
      my_agent = MyAgent()
      my_agent = load('MyAgent_3000')
      my_agent.learning = False
      start(player_x=my_agent)

    if optie == 5:
      from bke import MLAgent, is_winner, opponent, load, validate, RandomAgent, plot_validation
      class MyAgent(MLAgent):
        def evaluate(self, board):
          if is_winner(board, self.symbol):
              reward = 1
          elif is_winner(board, opponent[self.symbol]):
              reward = -1
          else:
              reward = 0
          return reward
      my_agent = load('MyAgent_3000')
      my_agent.learning = False
      validation_agent = RandomAgent()
      validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
      plot_validation(validation_result)
  
    else:
      print("Ongeldige keuze")

    menu()
    optie = int(input("Kies een optie"))
print("Bedankt voor het spelen en tot ziens!")










