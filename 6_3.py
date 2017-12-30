# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

python_glossary={'list':'collection of items in a particular order','tuple':'immutable list is called a tuple','if':'examine the\
current state of a program','variable':'use to store values','string':'series of characters'}
print ('LIST        :'+python_glossary['list'])
print ('TUPLE       :'+python_glossary['tuple'])
print ('IF          :'+python_glossary['if'])
print ('VARIABLE    :'+python_glossary['variable'])
print ('STRING      :'+python_glossary['string'])