#!/usr/bin/python3
def multiple_returns(sentence):
    lng = len(sentence)
    fir_char = sentence[0] if lng > 0 else "None"
    tupl = lng, fir_char
    return(tupl)
