---
tags:
  - notes
  - natural-language-processing
  - y2023
  - programming-1-2
---
# Natural Language Processing
## Output
We can use a function to display text and symbols to the screen 
We use the `print`() function to display output

```python
print("Your text goes in here.")
```

Task 
## [[Headers]]

# Comments

Comments are pieces of text that are not interpreted by Python
This means that the text is ignored.
We use the hash symbol (#) to make comments

```python
#This is a comment
```

> Task
> 1. In input_and_output.py1
> 	1. Put the header
> 	2. Write in some comments

# Input
We grab information from the user using the `input`().
When we run the function, it does two things:
1. It **waits** for the user to write something or nothing
2. The user presses **Enter/Return** to indicate that they're finished

```python
input()

input(<prompt>) # prints out the prompt then waits
```

# Variable
Variables allow us to **store** info for the time that out app 
is running.

```python
favourite_food = input ("What is your favourite food?")
```

favourite_food --> name of the variable
= --> **assignment operator**
input() --> value
# [[Strings]]

## Naming 
What you can do:
1. name them with letters, numbers, underscores
2. names **should** start with a lowercase lett

## Naming 

What you can do:
1. name them with letters, numbers, underscores
2. names **should** start with a lowercase letter
What you can't do
1. you **can't** name them with spaces or symbols
2. you **can't** name them with certain names that are reserved
	1. e.g. if, while, for, ...

A good name is something like this:

```python
date_of_birth
fave_food
student_number
```
Bad names are like this:
```python
Favourite_food
a
num
aa
aaa
aaaa
```

# Design

*The design process* is the steps that we take when we create a solution to a problem.

There are four steps in our design process

## 1. Design our Algorithm in English (or any human language)
An *Algorithm* is a sequence of steps to solve a problem.
In this class, before we start ANY programming, we write out steps in English.

## 2. Translate our Algorithm from English to Python
We'll translate out algorithm into "proper" Python.

## 3. Test out Python Algorithm
Check if it works *syntactically*. In other words, we check to see if it BREAKS
Check if it works *syntactically*. In other words, we ask does our algorithm actually solve the problem.

# Lists
A list in Python is a collection of items

# Creating A List
To make a list, we use brackets [] to surround our list
We separate out the items using ,

```python
some_list = ["John", "Tim", "Sara"]
```


# Access Elements in a List
We can grab things from lists using the bracket notation
In our example above, if I wanted to access "Tim", I would do the following

```python
some_list[1]#'Tim'
some_list[2]#'Sara'
some_list[-1]#'Sara'
some_list[-2]#'Tim'


```

Inside the brackets, we say the *index* of the value we want.
Python uses 0-*index* counting, which means we start counting at 0.

# Modules
Modules are bits of code that we can use in Python 
These bits of code aren't automatically included, so we need to import them
into our code
