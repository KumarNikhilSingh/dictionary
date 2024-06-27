def remove_duplicate_words(sentence):
    words = sentence.split()
    result = []
    seen = set()
    for word in words:
        if word.lower() not in seen:
         seen.add(word.lower())
         result.append(word)
    return ' '.join(result)
sentence = "This is a test test sentence with duplicate duplicate words"
print(remove_duplicate_words(sentence))    