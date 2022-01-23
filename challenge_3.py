'''Given a word, search it into a text and return how many times it is 
   in the text. The text  and the word should be parameters of a function.
'''


def word_finder(text, word):
    counter = 0
    for my_word in text:
        if word.lower() == my_word.lower():
            counter += 1
    return counter


my_text = ("Of, course, sky of gods, I'm off, and OF course I have gloves of cotton, Of.").replace(",", "").replace(".", "")
my_text_list = my_text.split()


print(word_finder(my_text_list, "of"))
    