from Verifier import *
from Counter import Counter

class Voter():
    __v_server = Verifier()
    __c_server = Counter()


    def cast_vote(self, vote):
        yes, no = self.__v_server.genrate_vote()
        print("User input {0}").format(vote)
        if vote == 1:
            self.__c_server.add_vote(yes, 1, self.__v_server)
        elif vote == 0:
            self.__c_server.add_vote(no, 0, self.__v_server)
        else:
            print "Invalid Input"



        # VotingList = {no: get_env1(), yes: get_env2()}
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