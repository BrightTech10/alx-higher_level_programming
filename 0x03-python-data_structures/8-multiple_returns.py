#!/usr/bin/python3

if __name__ != "__main__":
    def multiple_returns(sentence):
        str_len = len(sentence)

        if sentence == "":
            first_char = None
        else:
            first_char = sentence[0][0]
        _tuple = str_len, first_char
        return _tuple
