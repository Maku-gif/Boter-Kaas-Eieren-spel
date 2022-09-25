def menu():
  print("*** WELKOM BIJ HET SPELLETJE Boter-Kaas-Eieren***")
  print("--------------------------------------------------------")
  print("Om tegen een domme tegenstander te spelen, toets [1]")
  print("Om tegen een slimme tegenstander te spelen, toets [2]")
  print("Om tegen een andere speler te spelen, toets [3]")
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
    
  else:
    print("Ongeldige keuze")

  menu()
  optie = int(input("Kies een optie"))
  
print ("Bedankt voor het opstarten van het spel en tot ziens!")



































































#import random
 
#from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot
 
 
#class MyAgent(MLAgent):
    #def evaluate(self, board):
       # if is_winner(board, self.symbol):
       #     reward = 1
        #elif is_winner(board, opponent[self.symbol]):
          #  reward = -1
        #else:
        #    reward = 0
 #       return reward
    
    
#random.seed(1)
 
#my_agent = MyAgent()
#random_agent = RandomAgent()
 
#train_and_plot(
 #   agent=my_agent,
  #  validation_agent=random_agent,
   # iterations=25,
    #trainings=50,
    #validations=1000)
# my_agent = MyAgent(alpha=0.2, epsilon=0.9)