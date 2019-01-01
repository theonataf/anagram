from database import connect


def search_for_anagram(word_to_check):
    """search the anagram of a word"""
    word_to_check = word_to_check.replace(" ","").upper()
    list_of_words = []
    adding_to_sql = ' AND word LIKE %s'
    letter_to_add = ()
    list_of_right_words = []
    sql = "SELECT word FROM words WHERE " \
        + "char_length(word)=char_length('{}')".format(word_to_check)

    for letter in word_to_check:
        sql += adding_to_sql
        letter_to_add += (f"%{letter}%",)

    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, letter_to_add)
            retrieve_words = cursor.fetchall()

            for word in retrieve_words:
                list_of_words.append(word[0])

            for words in list_of_words:
                if get_the_letter(word_to_check, words):
                    list_of_right_words.append(words)

                    if get_the_right_letter_num(word_to_check, list_of_right_words):
                        list_of_right_words.remove(words)

    return list_of_right_words


def get_the_letter(word, word_from_list):
    """This function checks if the word contains the right letters in the anagram (corrects the double letter pb)"""
    list_of_letters = []
    answer = bool
    for letter in word:
        list_of_letters.append(letter)
    for letters in word_from_list:
        if letters in list_of_letters:
            answer = True
        else:
            return False
    return answer


def get_the_right_letter_num(original_word, list_of_words_to_check):
    """Checks if the doubled letter is the right one"""
    word = ""
    for word in list_of_words_to_check:
        for letter in word:
            if original_word.count(letter) != word.count(letter):
                return True


def split_and_check(word_to_anagram):
    counter = 0
    i = 1000
    while counter < i:
        bunch_of_letters = word_to_anagram.replace(" ", "").upper()
        i = len(bunch_of_letters)
        turns = 0
        semi_word = ""
        other_part_of_the_word = bunch_of_letters
        while turns < i:
            semi_word += bunch_of_letters[turns]
            other_part_of_the_word = extract_one_letter(other_part_of_the_word)
            search_for_anagram(semi_word)
            if search_for_anagram(semi_word) and search_for_anagram(other_part_of_the_word):
                print(search_for_anagram(semi_word), search_for_anagram(other_part_of_the_word))
            turns += 1
        word_to_anagram = swipping_first_with_second(bunch_of_letters)
        counter += 1

    return "end"

def swipping_first_with_second(word_to_swipe):
    list_of_letters = []
    list_of_new_letters = []
    i = len(word_to_swipe)
    new_word = ""
    num = 1
    for letters in word_to_swipe:
        list_of_letters.append(letters)
    letter_to_save = list_of_letters[0]
    while num < i:
        list_of_new_letters.append(list_of_letters[num])
        num += 1
    list_of_new_letters.append(letter_to_save)
    for letter in list_of_new_letters:
        new_word += letter
    return new_word


def extract_one_letter(word_to_be_extracted):
    list_of_letters = []
    i = len(word_to_be_extracted)
    new_word = ""
    for letters in word_to_be_extracted:
        list_of_letters.append(letters)
    list_of_letters.pop(0)
    for letter in list_of_letters:
        new_word += letter
    return new_word







