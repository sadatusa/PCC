# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

python_glossary={'list':'collection of items in a particular order','tuple':'immutable list is called a tuple','if':'examine the\
current state of a program','variable':'use to store values','string':'series of characters'}
for py_words,meaning in python_glossary.items():
    print(py_words.title()+' : '+meaning)