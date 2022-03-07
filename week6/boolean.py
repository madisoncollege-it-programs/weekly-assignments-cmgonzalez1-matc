#!/usr/bin/env python3

#[Lab-Python] Boolean Logic Basics
#Christian Gonzalez

#True and True
print(bool(1 == 1) and (1 == 1)) 

#False and True
print(bool(1 == 0) and (1 == 1))

#1 == 1 and 2 == 1
print(bool(1 ==1) and (2 == 1))

#0
print(bool(0))

#""
print(bool(""))

#0.0
print(bool(0.0))

#not 0
print(bool(not 0))

#'test' == 'test'
print(bool('test' == 'test'))

#1 == 1 or 2 != 1
print(bool(1 == 1 or 2 != 1))

#True and 1 == 1
print(bool(1 == 1 and 1 ==1))

#False and 0 != 0
print(bool( 1 == 0 and 0 != 0))

#True or  1 == 1
print(bool(1 == 1 or 1 == 1))

#'test' != 'testing'
print(bool('test' == 'testing'))

#'test' == 1
print(bool('test' == 1))

#1 == 1 and not ('testing' == 1 or 1 == 0)
print(bool(1 == 1 and not ('testing' == 1 or 1 == 0)))

#'chuncky' == 'bacon' and not (3 == 4 or 3 == 3)
print(bool('chuncky' == 'bacon' and not (3 == 4 or 3 == 3)))

#3 == 3 and not ('testing' or 'Python' == 'Fun')
print(bool(3 == 3 and not ('testing' == 'testing' or 'Python' == 'Fun')))
