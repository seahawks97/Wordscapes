from itertools import permutations

print('Instructions:\n'
      '1. Type the length of the word needed.\n'
      '2. Type the letters available (like this: a, b, c, d, e, ...).\n'
      '3. Type the given characters and their positions (like this: a1, b2, ...).\n')


def main():
    # Input for letters
    word_len = get_len()
    let_li = letters()

    # Given letters
    yn = input('Any letters given? (Y)es or (N)o: ').lower()
    if yn == 'y':
        given_lets, given_pos = givens()
    else:
        # Empty lists otherwise
        given_lets, given_pos = [], []

    # Gets all permutations of letter combinations of length word_len
    perms = list(permutations(let_li, word_len))
    # print(perms)
    print('\nPossible words:\n')

    # Confirm a permutation is valid by the given letters
    for tup in perms:
        good = True             # automatically good
        # If given letters exist
        for i in range(len(given_pos)):
            # Check the given position letter matches the given letter
            if tup[int(given_pos[i]) - 1] != given_lets[i]:
                good = False

        # Assemble word and print if valid
        if good:
            str_out = ''
            for l in tup:
                str_out += l
            print(str_out)

    # Keep the window up to view answers
    input('Press any button to quit.')


def get_len():
    """
    Gets the length of the word that you are trying to guess.
    :return: num, the length of the word
    :rtype num: int
    """
    while True:
        num = input('Length of word: ')
        try:
            num = int(num)
            return num
        except TypeError('Type an integer.\n'):
            pass


def letters():
    """
    Gets the letters you have in your hand that are available to play.
    :return let_li: letters in your hand
    :rtype let_li: list of 1-character long strings
    """
    let = input('Available letters: ').lower()
    let_li = let.split(', ')
    return let_li


def givens():
    """
    Gets the letters that have already been put in place.
    :return glets: given letters
    :rtype glets: list of 1-character long strings
    :return gpos: positions of letters
    :rtype gpos: list of 1-character long strings, converted into ints later
    """
    sel = input('Given characters and their positions (a1, b2, ...):\n').lower()
    sel_li = sel.split(', ')
    glets, gpos = [], []
    for i in range(len(sel_li)):
        glets.append(sel_li[i][0])
        gpos.append(sel_li[i][1])
    return glets, gpos


main()