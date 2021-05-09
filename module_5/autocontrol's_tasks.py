def is_spam_words(text, spam_words, space_around=False):
    l_text = text.split()
    spam_words = spam_words.casefold()
    if space_around:
        pass
    for word in l_text:
        if word.casefold() in spam_words:
            print(word)




is_spam_words('ddebil sobaka dikaya', 'debil')






