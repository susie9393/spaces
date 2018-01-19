# spaces
import numpy as np
import random as rn

def Spaces(no_rolls):

        # initialise an array to record number of times each space is landed on
        freq = np.zeros(14)

        # s denotes space landed on, 1 <= s <= 14
        s = 0

        # a counter has been set up to perform a check on total number of squares landed on
        count = 0

        for n in range(no_rolls):

                dice1 = rn.randint(1,6)
                dice2 = rn.randint(1,6)
                moves = dice1 + dice2

                s+=moves

                if s > 14:
                        s-=14

                if s == 4:
                        freq[s-1]+=1
                        count+=1
                        s = 10

                if s == 7 and (dice1 == 6 or dice2 == 6):
                        freq[s-1]+=1
                        count+=1
                        s = 1

                if s == 10 and moves%2==0:
                        freq[s-1]+=1
                        count+=1
                        s = 5

                freq[s-1]+=1

        if np.sum(freq)==200+count:
                return freq
        else:
                print "Error"

def Average(iterations):

        total = []

        for i in range(iterations):
                freq = Spaces(200)
                total.append(freq)

        freq = np.mean(np.array(total), axis = 0)

        print np.around(freq)

Average(10)
