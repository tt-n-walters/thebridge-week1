import requests
import os
import nltk.corpus


if not os.path.exists("sherlock_holmes.txt"):
    print("Downloading file...")
    response = requests.get("https://resources.nicowalters.repl.co/sherlock_holmes")

    print("Saving file...")
    file = open("sherlock_holmes.txt", "w", encoding="utf-8")
    file.write(response.text)
    file.close()
    print("Finished creating file.")
else:
    print("File already exists. Not downloading.")


file = open("sherlock_holmes.txt", "r", encoding="utf-8")
sherlock = file.read()
file.close()

sherlock = nltk.corpus.state_union.raw()

print("Number of characters:", len(sherlock))
words = sherlock.split()
print("Number of words:", len(words))


# Converting all words to the same case
lowercase_words = []
for word in words:
    word = word.lower()
    lowercase_words.append(word)


# Removing punctuation
punctuation = ",.()-_?!:;’‘”“—"
cleaned_words = []
for word in lowercase_words:
    word = word.strip(punctuation)
    cleaned_words.append(word)
    


word_counts = {}
for word in cleaned_words:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] = word_counts[word] + 1


def word_count(word):
    count = word[1]
    return count


count_list = sorted(word_counts.items(), reverse=True, key=word_count)
for i in range(100):
    print(count_list[i])

