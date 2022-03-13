# Collection Datatypes

## Lists
1. Lists are ordered collections of items.
2. Lists are enclosed in square brackets([]).
3. Lists are indexed starting at 0.
4. Lists can contain any type of data.
5. Lists can be nested.
6. Lists can be empty.
7. Lists are mutable means that they can be changed.
8. Lists are iterable.
### Python List Methods
<ul>
<li>append() - to add an item to a list</li>
<li>extend() - to add all elements of a list to another list</li>
<li>insert() - to insert an item at a given index</li>
<li>remove() - to remove an item from a list</li>
<li>pop() - to remove an item at a given index</li>
<li>clear() - to remove all items from a list</li>
<li>copy() - returns a shallow copy of the list</li>
</ul>


example:
```
#creating a list
a = [1, 2, 3]
b = [4, 'five', 6.0]
c = ['seven', 8, 9.0,[10,11,12]]
d = []

#accessing elements in a list

print(a[0])
print(b[1])
print(c[3][1])

#negative indexing
print(a[-1])
print(b[-2])
print(c[-1][-1])

#slicing a list
print(a[0:2])
print(a[:])
print(b[1:])  
print(c[3][1:3])  

#change items of a list
a[0] = 'one'
print(a)

#add elements to a list

a = [1, 2, 3]
a.append(4)  #append adds an element to the end of the list, only one element
print(a)

new = [11,22,33]
a.extend(new) #extend adds a list to the end of the list, multiple elements
print(a)

f = [1,2,3]
g = [4,5,6]
h = f + g
print(h)

d = [1,2,3]
d.insert(1,4) #insert adds an element at a specific index
print(d)

#remove elements from a list
mylist = [1,2,3,4,5,6,7,8,9,10]
del mylist[0]
print(mylist)

mylist.remove(5)
print(mylist)

mylist.pop() #pop removes the last element of the list
print(mylist)

mylist.pop(0) #pop removes the element at a specific index

mylist.clear() #clear removes all elements from the list
print(mylist)


#list copy
list1 = [1,2,3]
list2 = list1
print(list1)
print(list2)
print(list1 is list2) #True because list1 and list2 point to the same list

#another way to copy a list
list1 = [1,2,3]
list2 = list1.copy()
print(list1)
print(list2)
print(list1 is list2) #False because list1 and list2 do not point to the same list

#loop through a list
mylist = [1,2,3,4,5,6,7,8,9,10]
for i in mylist:
    print(i)

print(len(mylist))

print(1 in mylist) #True
print(11 in mylist) #False
```


## Tuples
1. Tuples are ordered collections of items.
2. Tuples are enclosed in parenthesis(()).
3. Tuples are indexed starting at 0.
4. Tuples can contain any type of data.
5. Tuples can be nested.
6. Tuples are immutable means that they cannot be changed.

### Python Tuple Methods
<ul>
<li>count() - returns the number of times a specified value occurs in a tuple</li>
<li>index() - returns the index of the first occurrence of a specified value</li>
</ul>

example:    
```
#creating a tuple
a = (1, 2, 3)
b = (4, 'five', 6.0)
c = ('seven', 8, 9.0,[10,11,12])
d = ()
e = 3, 4, 5
print(a)
print(b)
print(c)
print(d)
print(e)

#creating a tuple with one item
f = (1,)
print(f)
g = ('hello',)  
print(g)

#accessing elements in a tuple
print(a[0])
print(b[1])
print(c[3][1])
#negative indexing
print(a[-1])
print(b[-2])
print(c[-1][-1])

#slicing a tuple
print(a[0:2])
print(a[:])
print(b[1:])
print(c[3][1:3])

#change items of a tuple
#a[0] = 'one' #TypeError: 'tuple' object does not support item assignment
#print(a)

#but
c[3][1] = 'eleven'
print(c)

#add elements to a tuple
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)

#remove elements from a tuple
t1 = (1,2,3)

del t1[0] #TypeError: 'tuple' object doesn't support item deletion

del t1
print(t1) #NameError: name 't1' is not defined

#loop through a tuple
mytuple = (1,2,3,4)
for i in mytuple:
    print(i)

#tuple methods

a = (1,2,3)
result = a.count(1)
print(result)
result = a.index(2)
print(result)

#tuple operations
t5 = (1,2,3)
print(2 in t5) #True
print(2 not in t5) #False

```


## Strings
1. Strings are ordered collections of characters.
2. Strings are enclosed in quotation marks('' or "" ).
3. Strings are indexed starting at 0.
4. Strings can be sliced.
5. Strings can be concatenated.
6. Strings can be repeated.
7. Strings are immutable means that they cannot be changed.
8. Strings can be used as dictionary keys.
### Escape Sequences
<ul>
<li>\n - new line</li>
<li>\t - tab</li>
<li>\\ - backslash</li>
<li>\' - single quote</li>
<li>\" - double quote</li>
</ul>

### Python String Methods
<ul>
<li>len() - returns the length of a string</li>
<li>lower() - returns a lowercased string</li>
<li>upper() - returns a uppercased string</li>
<li>str() - returns a string representation of an object</li>
<li>format() - returns a formatted string</li>
<li>replace() - returns a string where a specified value is replaced with a specified value</li>
<li>split() - returns a list where a string has been split at each occurance of a specified value</li>
<li>join() - returns a string where a list has been joined by a specified value</li>
<li>find() - returns the index of the first occurance of a specified value</li>
<li>count() - returns the number of times a specified value occurs in a string</li>
<li>startswith() - returns a Boolean value indicating whether the string starts with a specified value</li>
<li>endswith() - returns a Boolean value indicating whether the string ends with a specified value</li>
<li>isdigit() - returns a Boolean value indicating whether the string contains only digits</li>
<li>isalpha() - returns a Boolean value indicating whether the string contains only letters</li>
<li>isalnum() - returns a Boolean value indicating whether the string contains only alpha-numeric characters</li>

</ul>

example:    
```
#creating a string
a = 'hello'
b = "hello"
c = "Don't worry about apostrophes"
f = '''This is a long string that is made up of
        several lines and non-printable characters
        such as tabs and line feeds, etc.
        '''
print(a)
print(b)
print(c)
print(f)


#accessing elements/characters in a string

a = 'hello'
print(a[0])
print(a[4])

#negative indexing
print(a[-1])
print(a[-2])

#slicing a string
print(a[0:2])
print(a[:])

#change items of a string
a[0] = 'H' #TypeError: 'str' object does not support item assignment
print(a)

#delete items of a string
a = 'hello'
del a[0] #TypeError: 'str' object doesn't support item deletion
print(a)

#concatenate strings
a = 'hello'
b = 'world'
c = a + b
print(c)

#iterate through a string
a = 'hello'
for i in a:
    print(i)

#check if string is in a string
s = 'hello'
print('h' in s) #True

#escape sequences/characters
a = 'hello\nworld'
print(a)

b = 'hello\tworld'
print(b)

c = 'hello\\world'
print(c)

#string methods
#format()
a = 'hello'
b = 'world'

print('{} {}'.format(a,b))
print('{1} {0} {1}'.format(a,b))


```
## Sets
1. Sets are an unordered collection of unique elements.
2. Sets are enclosed in curly braces({}).
3. Sets elements are not indexed.
4. Sets are mutable - they can be changed with the help of methods.


### Python Set Methods
<ul>
<li>add() - adds an element to a set</li>
<li>udpate() - updates a set by adding elements from another set</li>
<li>remove() - removes an element from a set</li>
<li>discard() - removes an element from a set if it is a member</li>
<li>pop() - removes and returns an arbitrary set element</li>
<li>clear() - removes all elements from a set</li>
<li>union() - returns a set containing the union of sets</li>
<li>intersection() - returns a set containing the intersection of sets</li>
<li>difference() - returns a set containing the difference between two or more sets</li>
<li>issubset() - returns a Boolean value indicating whether the set is a subset of a specified set</li>
<li>issuperset() - returns a Boolean value indicating whether the set is a superset of a specified set</li>
</ul>

example:    
```
#creating a set
a = {1,2,3,3,4,5,5}
b = {4,'five',6}
c = {'seven',8,9.0}

l = [1,2,3,3,4,5,5]
s = set(l)
print(s)

s1 = set() #creating an empty set


#add, update set
s1.add(1)
s1.add(2)
s1.add(3)
print(s1)

s1.update([4,5,6])
print(s1)

#removing elements from a set

s1.remove(1)
print(s1)

s1.discard(2)
print(s1)

s1.pop()
print(s1)
s1.clear()
print(s1)

#iterate through a set

s2 = {1,2,3,4,5,6}
for i in s2:
    print(i)

# check if an element is in a set
s2 = {1,2,3,4,5,6}
print(1 in s2) #True
print(7 in s2) #False

```
## Dictionaries
1. Dictionaries are unordered collections of unique keys and values.
2. Dictionaries are enclosed in curly braces({}).
3. Dictionaries are mutable.
4. Keys must be unique in a dictionary.
5. Keys are immutable.
6. Values can be any type, including other dictionaries.


### Python Dictionary Methods
<ul>
<li>get() - returns the value of a specified key</li>
<li>items() - returns a list containing a tuple for each key value pair</li>
<li>keys() - returns a list containing the dictionary's keys</li>
<li>values() - returns a list of all the values in the dictionary</li>
</ul>


example:    
```
#creating a dictionary
a = {}
b = {'one':1, 'two':2, 'three':[3,4,5]}

l = [(1,'python'),(3,'c++'),(2,'java')]
d = dict(l)
print(d)

#accessing elements in a dictionary

person = {'name':'John', 'age':30, 'country':'Norway'}
print(person['name'])
print(person['age'])
print(person['country'])

name = person.get('name')
age = person.get('age')
country = person.get('country')
print(name)
print(age)
print(country)

#update, add items in a dictionary

person['name'] = 'Jane'  #change
person['age'] = 31
person['country'] = 'USA'
person['city'] = 'New York'  #add
print(person)

#delete items in a dictionary
result = person.pop('city')
print(result)
print(person)

del person['age']
print(person)

person.clear()
print(person)

#iterate through a dictionary

numbers = {'one':1, 'two':2, 'three':3}
for key in numbers:
    print(key)

for key, value in numbers.items():
    print(key, value)

for key in numbers.keys():
    print(key)

for value in numbers.values():
    print(value)

```
