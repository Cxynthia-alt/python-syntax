def print_upper_words(chars, must_start_with):
    '''Given a list of words, print out each word on a separate line, but in all uppercase.
      it only prints words that start with the letter ‘e’
      pass in a set of letters, and it only prints words that start with one of those letters.
    '''
    for char in chars:
      for num in must_start_with:
        if char[0] == num:
          print(char.upper())
          break


# print(print_upper_words('hello'))
# print(print_upper_words('ello'))
print(print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],must_start_with={"h", "y"}))
