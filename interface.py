from matching_words import search_for_anagram, split_and_check
import time

def main():

    new_word = input("type a word or words to anagram:\n")
    print(search_for_anagram(new_word))
    split_and_check(new_word)

start_time = time.perf_counter()
main()
stop_time = time.perf_counter() - start_time
print(stop_time)