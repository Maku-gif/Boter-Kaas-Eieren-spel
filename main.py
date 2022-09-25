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
    
  else:
    print("Ongeldige keuze")

  menu()
  optie = int(input("Kies een optie"))
  
print ("Bedankt voor het opstarten van het spel en tot ziens!")
