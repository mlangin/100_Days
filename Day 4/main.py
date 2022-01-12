import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
p = int(input())
ai = random.randint(0, 2)
if p == 0:
    print("Player chooses Rock.")
elif p == 1:
    print("Player chooses Paper.")
else:
    print("Player chooses Scissors.")

if ai == 0:
    print("Computer chooses Rock.")
elif ai == 1:
    print("Computer chooses Paper.")
else:
    print("Computer chooses Scissors.")

if p == 0 and ai == 0:
    print("\nTie. Both picked Rock.")
elif p == 1 and ai == 1:
    print("\nTie. Both picked Paper.")
elif p == 2 and ai == 2:
    print("\nTie. Both picked Scissors.")
elif p == 0 and ai == 2:
    print("\nPlayer wins. Rock beats Scissors.")
elif p == 2 and ai == 0:
    print("\nComputer wins. Rock beats Scissors.")
elif p == 0 and ai == 1:
    print("\nComputer wins. Paper beats Rock.")
elif p == 1 and ai == 0:
    print("\nPlayer wins. Paper beats Rock.")
elif p == 1 and ai == 2:
    print("\nComputer wins. Scissors beats Paper.")
elif p == 2 and ai == 1:
    print("\nPlayer wins. Scissors beats Paper.")