Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> person = {'first_name': 'shainila','last_name': 'yousuf','age': 18,'city': 'karachi'}
>>> print(person['first_name'])
shainila
>>> print(person['last_name'])
yousuf
>>> print(person['age'])
18
>>> print(person['city'])
karachi
>>> # 6.2
>>> favorite_numbers = {'a': 42,'b': 23,'c': 7,'d': 1000000,'e': 0,}
>>> num = favorite_numbers['a']
>>> print("a's favourite number is " + str(num) + ".")
a's favourite number is 42.
>>> num = favourite_numbers['b']
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    num = favourite_numbers['b']
NameError: name 'favourite_numbers' is not defined
>>> num = favorite_numbers['b']
>>> print("b's favorite number is " + str(num) + ".")
b's favorite number is 23.
>>> num = favorite_numbers['c']
>>> print("c's favorite number is " + str(num) + ".")
c's favorite number is 7.
>>> num = favorite_numbers['d']
>>> print("d's favorite number is " + str(num) + ".")
d's favorite number is 1000000.
>>> glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }
>>> word = 'string'
>>> print("\n" + word.title() + ": " + glossary[word])

String: A series of characters.
>>> word = 'comment'
>>> print("\n" + word.title() + ": " + glossary[comment])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print("\n" + word.title() + ": " + glossary[comment])
NameError: name 'comment' is not defined
>>> print("\n" + comment.title() + ": " + glossary[comment])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print("\n" + comment.title() + ": " + glossary[comment])
NameError: name 'comment' is not defined
>>> word = 'comment'
>>> print("\n" + word.title() + ": " + glossary[word])

Comment: A note in a program that the Python interpreter ignores.
>>> word = 'list'
>>> print("\n" + word.title() + ": " + glossary[word])

List: A collection of items in a particular order.
>>> word ='loop'
>>> print("\n" + word.title() + ": " + glossary[word])

Loop: Work through a collection of items, one at a time.
>>> word ='dictionary'
>>> print("\n" + word.title() + ": " + glossary[word])

Dictionary: A collection of key-value pairs.
>>> 
