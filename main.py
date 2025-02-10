from replit import clear
from art import logo

print(logo)
players = {}
end = False
while not end: 
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  players[name] = bid

  choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if choice == 'yes':
    clear()
  else:
    end = True
winner = ""
max_bid = 0

for key in players:
  if players[key] > max_bid:
    max_bid = players[key]
    winner = key

print(f"The winner is {winner} with a bid of ${max_bid}")
