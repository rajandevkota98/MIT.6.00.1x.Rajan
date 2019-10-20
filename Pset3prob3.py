def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    new = string.ascii_lowercase
    for letter in lettersGuessed:
        new = new.replace(letter,'')
    return new