#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [i for i in num_list if (i%2 == 0)]
    return even_numbers

def make_exclamation(sentence_list):
    new_list = [word + "!" for word in sentence_list ]
    return new_list


make_exclamation(["Hello", "I'm doing great", "Python is fun"])