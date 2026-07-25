# Word Frequency Counter By Sarjyant

text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""


def word_frequency(text):
    text = text.lower().replace(".", "").replace(",", "")
    words = text.split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    top3 = []
    for i in range(3):
        highest_word = ""
        highest_count = 0
        for word, count in frequency.items():
            if count > highest_count and word not in [w for w, c in top3]:
                highest_word = word
                highest_count = count
        top3.append((highest_word, highest_count))

    return top3


print("Top 3 words:")
for word, count in word_frequency(text):
    print(word, "—", count, "times")