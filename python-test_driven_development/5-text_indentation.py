#!/usr/bin/python3
"""Module to print text with indentation."""

def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', or ':'.
    
    Args:
        text (str): Input text.
    
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i], end="")
            print("\n")
            i += 1
            # Skip any spaces immediately after the punctuation
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        print(text[i], end="")
        i += 1
