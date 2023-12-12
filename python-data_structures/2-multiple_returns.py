def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        return (0, None)
    
    # Return a tuple with the length and the first character
    return (len(sentence), sentence[0])

# Test case
sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
