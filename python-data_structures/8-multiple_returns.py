#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.
    Args:
        sentence: the input string
    Returns:
        A tuple with the length and first character of the string
        If the sentence is empty, the first character is None
    """
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
