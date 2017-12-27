class Storage:

    voter_counter = dict()
    share_counter = dict()


    def get_share(self, key):
        if key in self.share_counter:
            return self.share_counter[key]
        return 0

    def write_share(self, share_common):

        if share_common in self.share_counter :
            self.share_counter[share_common] = self.share_counter[share_common] + 1
        else:
            self.share_counter[share_common] = 1

    def get_voter(self, key):
        if key in self.voter_counter:
            return self.voter_counter[key]
        return 0

    def result(self):

        print("Yes: {0}, No: {1}").format(self.get_voter(1), self.get_voter(0))

        for k in self.share_counter:
            print("{0}: {1}").format(k,self.share_counter[k])

    def write_voter(self, vote):

        if vote in self.voter_counter :
            self.voter_counter[vote] = self.voter_counter[vote] + 1
        else:
            self.voter_counter[vote] = 1
