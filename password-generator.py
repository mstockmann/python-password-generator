import random

def capitalize(word):
    random_capitalized_word = []
    for c in word:
        capital = bool(random.getrandbits(1))
        if capital:
            c = c.capitalize()
        random_capitalized_word.append(c)
    return ''.join(random_capitalized_word)

def main():
    """
    This script generates pseudo-random password of
    1. Random generated characters from list_of_characters.txt
    2. Random generated password from https://github.com/dwyl/english-words

    """

    # User defined input
    password_style = int(input("Make my password from:\n1. Random Characters\n2. Shuffling words\nAnswer: "))
    try:
        if password_style == 1:
            length_of_password = int(input("Input length of password: "))
        elif password_style == 2:
            length_of_password = int(input("Input no of words in password: "))
    except ValueError as ve:
        length_of_password = 10  

    # load list of words
    if password_style == 1:
        file_path = "list_of_characters.txt"
    elif password_style == 2:
        file_path = "English_words_list.txt"
    with open(file_path, 'r', encoding='utf-8') as file:
        word_list = [line.replace('\n', '') for line in file]

    password = []
    for i in range(0,length_of_password,1):
        # randomize order of characters
        random.shuffle(word_list)

        # randomize capital
        character = capitalize(random.choice(word_list))
        password.append(character)
    password = ''.join(password)
    print("This is your pseudo-random generated password:\n\n\t\t%s\n" % password)

if __name__ == "__main__":
    main()