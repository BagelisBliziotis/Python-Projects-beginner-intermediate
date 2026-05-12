import art

print(art.logo)
check = True
players_bids = {}

while check:
    name = input("What is your name?: ")
    bid  = int(input("What is your bid?: $"))
    question = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if question == "no":
        check = False
    players_bids[name] = bid
    print("\n"*100)
    winner = name

for key in players_bids:
    if players_bids[winner] < players_bids[key]:
        winner = key
winning_bid = players_bids[winner]

print(f"The winner is {winner} with a bid of ${winning_bid}")

