def print_upper_words(words, starting_letter):
    ''' Takes an array. Returns each word as upper case only'''
    for word in words:
        # Below conditional needs to be converted to accept a set
        if word.start(starting_letter):
            print(word.upper())