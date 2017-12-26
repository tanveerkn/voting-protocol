from Voter import Voter
import random

import time


class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


with Timer() as t:
    for no in range(10):
        start = time.clock()
        new_voter = Voter()
        new_voter.cast_vote(random.randint(0, 1))
        end = time.clock()
        print('For each Voter time taken is %.03f sec.' % float(end - start))
print('Whole process took %.03f sec.' % t.interval)



# from Verifier import get_env1,get_env2
#
# votersList = []
# for voter in range(10):
#     votersList.append(voter())
# #
# # x_1=0
# # x_2=1
# # VotingList={x_1: get_env1(), x_2:get_env2()}
# def voter():
#     voter = input("Enter 0 or 1: ")
#     voter = int(voter)
#     if (voter is 0):
#         print("voter has chosen envelope 1")
#         return get_env1()
#     else:
#         print("voter has chosen envelope 2")
#         return get_env2()
