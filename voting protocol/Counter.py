from Storage import Storage
from Verifier import Verifier
import pickle


class Counter:
    verify_server = Verifier()
    storage = Storage()
    #global yes
    #yes = 0
    #global no
    #no = 0



    def add_vote(self, envelop, vote, verifier):

        if vote == 0 or vote ==1:

            parts = envelop.split("_")
            share_common = parts[1]
            print("Share Common {0} ").format(share_common)
            self.storage.write_share(share_common)
            self.storage.write_voter(vote)
            self.storage.result()
            verifier.verify(vote)
            #self.verify_server.decrypt(vote)
        else:
            print("Invalid vote")
        #yes, no = pickle.load(open("votesCount.pickle", "rb"))
        # yes =""
        # no =""
        # new = self.verify_server.verifyVote(verifyVote=vote)
        # print new

        #if new == 0:
        #    global no
        #    no += 1
        #    print "Yes count : " + str(yes) + "No count : " + str(no)
        #elif new == 1:
        #    global yes
        #    yes += 1
        #    print "Yes count : " + str(yes) + "No count : " + str(no)
        #else:
        #    print "inavalid vote"
       # pickle.dump((yes, no), open("votesCount.pickle", "wb"))

# import Voter
#
#
# def update_counts():
#     """
#     Updates/maintains self.counts (see above for description)
#     """
#     counts = []
#     # computes [<# 1st place votes>, <# 2nd place votes>, ...]
#     for (candidate, votes) in zip(self.names, self.votes_by_candidate()):
#         counter = {}
#         for i in xrange(1, self.N_candidates + 1):
#             counter[i] = 0  # don't use defaultdict: we need all keys
#         for vote in votes:
#             if vote is not None:  # don't count abstentions
#                 counter[vote] += 1
#
#
# counts.append([count for (rank, count) in sorted(counter.iteritems())])
#      # now keep things sorted: the 3 lists are sorted from
#         # weakest candidate to strongest candidate
#         (counts,votes_by_candidate,names) = zip(*sorted(zip(counts,self.votes_by_candidate(),self.names)))
#         # we want to store votes by ballot, not by candidate:
#         self.votes = zip(*votes_by_candidate)
#         self.counts = counts
# self.names = names