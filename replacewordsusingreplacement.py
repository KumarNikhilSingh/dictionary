def replace_words(text, replacements):
    for words, new_words in replacements.items():
        text = text.replace(words, new_words)
    return text
text = "Hello world this is a test"
replacements = {"Hello": "Hi", "world": "Earth", "test": "experiment"}
modified_text = replace_words(text, replacements)
print(modified_text)    