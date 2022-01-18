import collections


def run():
    words_list = []

    with open("./98-0.txt", encoding="utf8") as file:
        for line in file:
            for word in line.split():
                words_list.append(word)

    stop_words = []
    
    with open("./stopwords", encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                stop_words.append(word)

    
    word_counter = {}

    for word in words_list:
        word = word.lower()
        word = word.replace("“", "")
        word = word.replace(",", "")
        if word not in stop_words:
            if word not in word_counter:
                word_counter[word] = 1
            else:
                word_counter[word] += 1

    top10 = collections.Counter(word_counter)

    for word, count in top10.most_common(10):
        print(word, ": ", count)

if __name__ == '__main__':
    run()