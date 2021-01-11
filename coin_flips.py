# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
    number = input(5)
    recordlist = []
    heads = 0
    tails = 0
    for amount in range(number):
        flip = random.randomint(0,1)
        if (flip == 0):
            print("heads")
        else:
            print("tails")
            recordlist.append(tails)
    print(str(recordlist))
    print(str(recordlist.count("heads")) + str(recordlist.count("tails")))
   
coin_flips()

# print(coinFlips(2)) 
# => ["HH", "HT", "TH", "TT"]