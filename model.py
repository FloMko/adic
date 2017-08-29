from histograms import Dictogram
import random
from collections import dequie

def generate_random_start(model):
    # to generateany random word first
    # return random.choise(model.keys())

    # right start word
    if 'END' in model:
        seed_word = 'END'
        while seed_word == 'END':
            seed_word = model['END'].return_weighted_random_word()
        return(seed_word)
    return(random.choice(model.keys()))

def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]
    for i in range(0, length):
        current_dictogram = markov_model[current_word]
        random_weighted_word =  current_dictogram.return_weighted_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return(' '.join(sentence) + '.')
    return(sentence)

