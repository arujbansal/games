import string

word = "shark"
word = word.lower()
word_dict = {}
vowels = ['a', 'e', 'i', 'o', 'u']


def word_dict_creater(word, dictionary):
    """
    Adds the letters of the word in the format: key = index position, value = letter.
    Removes all consonants
    """
    for i, l in enumerate(word):
        dictionary[i] = l
    for i, v in dictionary.items():
        if v not in vowels:
            dictionary[i] = "_"
    return dictionary


def strike(text):
    """
    Adds a strikethrough to a letter
    """
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


def vowels_strike(letter_list):
    """
    Strikes off vowels from the list of letters
    """
    for i, l in enumerate(letter_list):
        if l.lower() in vowels:
            letter_list[i] = strike(l)
    return letter_list


def mod(letter_list, letter):
    """
    Strikes a letter guessed by the user.

    """
    for i, l in enumerate(letter_list):
        if l.lower() == letter.lower():
            letter_list[i] = strike(l)
    return letter_list


def letter_remover_dict(dictionary, word, letter):
    """
    Replaces an empty letter in the dictionary with a guessed letter.
    """
    for i, l in enumerate(word):
        if letter == l.lower():
            dictionary[i] = letter
    return dictionary


def replay():
    """
    Asks the user if he wants to play again.
    """
    choice = input("Do you want to play again? [Y/n]:\n")
    return choice[0].lower() == 'y'


# Setting up the game
while True:
    hangman_stages = [
                            '''
                                *---------*
                                     |   |
                                         |
                                         |
                                         |
                                         |
                                ==========
                            ''',
                            '''
                                *---------*
                                     |   |
                                     O   |
                                         |
                                         |
                                         |
                                ==========
                            ''',
                            '''
                                *---------*
                                     |   |
                                     O   |
                                     |   |
                                         |
                                         |
                                ==========
                            ''',
                            '''
                                *---------*
                                     |   |
                                     O   |
                                    /|   |
                                         |
                                         |
                                ==========
                            ''',
                            '''
                                *---------*
                                     |   |
                                     O   |
                                    /|\  |
                                         |
                                         |
                                ==========
                            ''',
                            '''
                                *---------*
                                     |   |
                                     O   |
                                    /|\  |
                                    /    |
                                         |
                                ==========
                            ''',
                            '''
                                *---------*
                                     |   |
                                     O   |
                                    /|\  |
                                    / \  |
                                         |
                                ==========
                            '''
                    ]

    letters = [i for i in string.ascii_uppercase]
    vowels_strike(letters)
    word_dict_creater(word, word_dict)
    guesses = 6
    not_in_word = []
    print(f"You have {guesses} guesses. One guess is subtracted every time you enter a wrong letter.")
    print(hangman_stages[guesses])
    # Actual loop now
    while guesses != 0:
        print("\n")        
        print(" ".join(word_dict.values()))
        print("\n")
        print("Available Letters:")
        print(" ".join(letters))
        print("\n")
        letter = input("Enter a letter:\n")
        print("\n" * 50)
        if letter.lower() in word and letter.lower() not in vowels:
            print(hangman_stages[guesses])
            mod(letters, letter)
            letter_remover_dict(word_dict, word, letter)
        elif letter in not_in_word:
            print(hangman_stages[guesses])
            print("You have already tried that letter...")
        elif letter in vowels:
            print(hangman_stages[guesses])
            print("That's a vowel!")
        elif letter.isdigit():
            print(hangman_stages[guesses])
            print("That's a number!")
        else:
            mod(letters, letter)
            guesses -= 1
            print(hangman_stages[guesses])
            print(f"Oops! That letter isn't in the word...\nRemaining guesses: {guesses}")
            not_in_word.append(letter)
        if "".join(word_dict.values()) == word:
            print(" ".join(word_dict.values()))
            print("".join(word_dict.values()))
            print("\n")
            print("Yep. You got it right. Game Over!")
            print("\n")
            break
    if not replay():
        break
