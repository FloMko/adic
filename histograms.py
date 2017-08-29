import random

class Dictogram(dict):
    def __init__(selff, iterable=None):
        # init constructor add element
        super(Dictogram, self).__init__()
        self.types = 0 # number unic key in distribution
        self.tokens = 0 # all number
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        # update distribution from dataset
        for item in iterable:
            if item in self:
                self[item] +=1
                self.tokens +=1
            else:
                self[item] = 1
                self.types += 1
                self.tokens += 1
    
    def count(self, item):
        # return count
        if item in self:
            return(self[item])
        return(0)

    def return_random_word(self):
        random_key = random.sample(self, 1)
        # another way 
        # random.choice(histogram.keys())
        return(random_key[0])

    def return_weighted_random_word(self):
        # generate pseudorandow number between 0 & (n-1)
        random_int = random.randint(0, self.tokens-1)
        index = 0 
        list_of_keys = self.keys()
        # display index, random_int
        for i in range(0, self.types):
            index += self[list_of_keys[i]]
            if (index > random_int):
                return(list_of_keys[i])
