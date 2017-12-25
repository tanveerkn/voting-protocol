import random
from bson import ObjectId
import pickle
import cPickle as pickle
from passlib.hash import sha512_crypt as CryptContext
from paillier_gmpy2 import *


priv, pub = generate_keypair(128)
uid = ObjectId()

class Verifier:
    __verifiers = []

    env1=None
    env2=None
    share_common = None
    env1_hash = None
    env2_hash = None

    # reading from a file
    def __init__(self):
        print("")
        #output=open("verfierData.pickle", "rb")
        #self.__verifiers = pickle.load(output)

    # writing to a file
    def __add__voter(self, vote):
        print("")
        #self.__verifiers.append(vote)
        #pickle.dump(self.__verifiers, open("verfierData.pickle", "wb"))

    def genrate_vote(self):

        A=15
        a_1 = 0
        a_2 = 1
        self.share_common = -(random.randint(1, 1000))
        share_0 = -(self.share_common*A)
        share_1 = share_0 + 1


        env1 = str(encrypt(pub,0)) +'_'+ str(encrypt(pub,share_0))+'_'+ str(uid)

        self.env1_hash = CryptContext.hash(env1)

        env2 = str(encrypt(pub,1)) +'_'+ str(encrypt(pub,share_1)) +'_'+ str(uid)

        self.env2_hash = CryptContext.hash(env2)

        self.__add__voter((env1, 0))

        self.__add__voter((env2, 1))

        return env1, env2


    def verify(self, vote):

        env_counter1 = str(encrypt(pub, vote)) + '_' + str(encrypt(pub, self.share_common)) + '_' + str(uid)

        env_counter1_hash = CryptContext.hash(env_counter1)

        if env_counter1_hash == self.env1_hash or self.env2_hash:
            print("verified")
        else:
            print("vote not counted")

    def decrypt(self,vote):
        V_id=str(decrypt(priv,pub,vote))
        print(V_id)
        return V_id





    #def verifyVote(self, verifyVote):
    #    vote = [vote[1]
    #    for vote in self.__verifiers
    #        if CryptContext.verify(vote[0], verifyVote)]
    #    return vote[0] \
    #        if len(vote) > 0 else -1




# import random
# from bson import objectid
# import pickle
# from passlib.hash import sha512_crypt as CryptContext
# # from
# a_1 = 0
# a_2 = 1
# env1=None
# env2=None
#
# def verifier():
#     share_common = (random.randint(1, 1000))
#     share_0 = -share_common
#     share_1 = share_0 + 1
#     x=objectid()
# def encryption(self):
#     uid = self.x
#     env1 = str(enc(0)) + str(enc(self.share_0)) + str(uid)
#     env2 = str(enc(1)) + str(enc(self.share_1)) + str(uid)
# def sig_gen(self):
#     CryptContext.encrypt(env1)
#     CryptContext.encrypt(env2)
# def sig_ver(self):
#     CryptContext.verify(password, 'password')
# def decryption(self):
# def get_env1():
#     return env1
# def get_env2():
#     return env2
#
# def attr_ver(self):
