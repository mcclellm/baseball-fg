# -*- coding: utf-8 -*-
"""
# MATLAB Tutorial for 12.335/835
# Written by Michael McClellan
# Some material adapted from Sarvesh Garimella
#  and inspired by lectures from 12.012/444
# 20 September 2016


This tutorial is best viewed using the Spyder GUI as part of the standard
Python 2.7 installation using Anaconda (continuum.io)

"""

# The Layout of Spyder/Python

'''
Welcome to Spyder, Anaconda, and Python!
Before we get started...
let's get acquainted with the Spyder layout
'''

#Any lines that start with # are notes and will not be executed
#You can "comment out" multiple lines using the '''/''' notation above
#You can also see that ''' and """ are interchangeable if used in pairs,
#... but that you cannot open with one type and close with another

'''
You can highlight lines and execute only those lines by
selecting them and using command+enter (likely Ctrl+enter in Windows)

Output will appear in the iPython console window
'''

print 'The Spyder window consists of a few workspaces:'
print '*The Current Folder directory tree at the top'
print "*The Editor, where you're currently running commands" #note the use of double quotes to use the apostrophe without interrupting

print '*The Console, where the visible output from commands appear'
print('*The Variable Explorer, where variables and data structures appear') #print() can also be called with the string as an input

'''
You'll notice that whitespace (tabs, spaces, carriage returns) between
lines in the code don't matter. Whitespace within commands, however, will
almost always matter!
'''

'''
## Basic Math
# https://en.wikibooks.org/wiki/Python_Programming/Basic_Math

# As written above, the workspace will contain all of your variables and
# data structures (cells, matrices, arrays, etc.)

# Variables are relatively simple. You can name them and assign them
# values. Best practice is to start variable names with uppercase letters
# if they are long; this differentiates them from functions, which begin
# generally with lowercase letters.

THE MOST IMPORTANT THING TO REMEMBER ABOUT PYTHON:
This is a zero-based language, meaning that 0 is the first element in lists
and the right-hand bound of ranges is NOT inclusive. More about this later.

'''

x = 3

y = 4
z=2 # Again, whitespace doesn't matter in these cases

x #this should show the value of x in the console as an output
print y #prints the value of y to the console (not an "output" line)
print(z) #same as above

a=1;b=1.5;c=1.75;
# You can even have multiple entries on the same line as long as they are
# separated by semicolons

# Look over to the Explorer, and you'll see all the variables

Product = x*y*z #This should multiply the variables
Added = a + b + c #This should add the variables

y/z # This will appear in the Console, and since no variable was
    # assigned to this operation, it will not get saved.
    # Even if you don't want to save it, you can always use new "dummy"
    # variables if needed, that get overwritten (such as var=y/z)

'''
Python has some interesting division rules. Integers are divided to return
an integer that is rounded down (the remainder/modulus is removed)
'''

div1 = 3/2 #this should equal 1
div2 = 3.0/2 #this should equal 1.5 since 3.0 is a floating point number
div3 = float(3)/int(2) #again, since a float is involved, it should be 1.5
div4 = float(int(3.0)/int(2.0)) #this should be equal to 1.0, the integer division made into a float


Square = Product**2
Unsquare = Square**(0.5)

'''
# This uses the built-in exponent. To use functions like sqrt, you need to
import the math library.
'''

import math

print math.sqrt(Square) # Is this equal to "Unsquare"?


'''Logical/Boolean Operations
# http://www.tutorialspoint.com/python/python_basic_operators.htm

# In general, MATLAB uses built-in True and False
You can also use numbers: 1=True and 0=False to indicate boolean operations
'''

a = 2; b = 3; c = 4;

# Use = to assign variables, == to test if two values are equal

print 'a==2?'
a == 2 #(this will return "True")
print 'a==b?'
a == b #(this will return "False")

# Use < (less than), > (greater than) <=, >=, and != (not equal to)
print 'c<=4?'
c <= 4
print 'b!=9?'
b != 9

# Use a combination of parentheses, & (and), | (called a "pipe", or) to get
# complex logical statements

print '(a == 2) & (b ~= c)?'
(a == 2) & (b != c) #both statements in parenthese are true, T&T returns T

print '(c == 2) | (b>=3)?'
(c == 2) | (b>=3) #one statement is true, F|T returns T

print '(c == 2) & (b>=3)?'
(c == 2) & (b>=3) #the same statement except with and, F&T returns F


''' Lists
# http://www.tutorialspoint.com/python/python_lists.htm

# You can save data in many formats! Not everything has to be an integer or
# a single floating-point number.

# Brackets denote a list, which will consist of one dimension

To do much more with lists, you will want the numpy library, which will be
imported using the "np" shorthand
'''

import numpy as np

Va = [1,2,3] #Separating by commas makes columns
Vb = [7,8,9]

Vc = np.multiply(Va,Vb)

#There are lots of limits to what lists can do, so let's use numpy arrays,
#which can have multiple dimensions

Vc = np.array(Va)
Vd = np.array(Vd)

SizeVc = Vc.size #one value indicating the number of elements
SizeVb = Vd.shape #the tuple indicating the sizes of dimensions, (3,)
Vc == Vd #This compares the two arrays element-wise
                                  

# If you want a vector with sequential numbers, you can use the following
# notation: range(x,y) or range(x,y,interval);

Vg = range(2,6) #this gets [2 3 4 5] NOTE THAT THE UPPER BOUND IS NOT INCLUDED
Vh = range(2,6,2) #this gets [2 4]
#range() only uses integers. Use np.arange to get floats
Vi = np.arange(10.0,0,-1.5) #this gets [10 8.5 7 5.5 4 2.5 1]

#These are especially helpful for time indices that may have regular
#periods (daily? weekly?)



''' More Numpy '''
# http://docs.scipy.org/doc/numpy-dev/user/quickstart.html


#You can make 'matrices' by nesting lists

Ma = [[1,2,3],[4,5,6],[7,8,9]] #commas for new columns, semicolons for new rows
Mb = np.array(Ma)

Mc = np.dstack((Ma,Mb)) #stack in the "depth" third dimension
Md = np.vstack((Ma,Mb)) #stack in the vertical (second) dimension
Me = np.hstack((Ma,Mb)) #stack in the horizontal (first) dimension

print Mc.shape
print Md.shape
print Me.shape

# You can also use the more general concatenate along any Nth dimension
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html

'''You can also slice arrays to get pieces of them'''

Slice1 = Mc[0,:,:] #This "slice" takes the top row of Md, producing a 1x3x3
print Slice1.shape
Slice2 = Mc[:,1:,:] #This slice is the second and third column
                     #(note zero is first element, 1 is second...)
                    # AND that right bound is not included; 3x2x2

print Slice2.shape

#If the dimension is sufficiently large, you can omit an upper bound
#index, such that Mc(:,1:3,:) and Md(0:,1:,:) are the same

Mzero = np.zeros((3,3,3)) #this creates a 3x3x3 matrix with all entries=0
Mone = np.ones((3,3,3)) #this creates a 3x3x3 matrix with all entries=1

# Let's add these to the third dimesion ("depth") of Mf
Mf = np.concatenate((Mzero,Mone),axis=2) #this makes Mf 3x3x6
print Mf.shape

#You can do lots of mathematical operations on matrices and vectors, though
#we won't be doing many of those in this class.

#If a dimension ever gets down to one entry, you can "squeeze" it to remove
#those singleton dimensions

Mgiant = np.ones((3,1,3)) #this produces an 8-dimensional array that
                                 #only contains information in 3 dimensions
print Mgiant.shape

Msqueezed = np.squeeze(Mgiant) #removes those dimensions to get 10x3x5 array
print Msqueezed.shape

#You can also use boolean logical statements to call parts of arrays that
#satisfy a quality

V1 = range(1,10)

#Getting out logical pieces of arrays isn't quite as easy as in MATLAB
#Both of these methods use "list comprehension"
# http://www.secnetix.de/olli/Python/list_comprehensions.hawk


V3 = [i for i in V1 if i >= 5] #this returns an array with ONLY the elements > 5
V4 = [i >=5 for i in V1] #this returns an array with logicals, each statement Mx>5

                                 
## Strings
# http://www.mathworks.com/help/matlab/characters-and-strings.html

# Matrices aren't good for storing all types of data, especially strings

# Strings are sets of characters ('char' type of variable), enclosed within
# single quotes, like 'text'

Str1 = 'text' #technically, 1x4 'char' vector
Str2 = 'words' #similarly, 1x5 'char' vector

# You can't make a matrix using these strings. But you can combine them
# using strcat or using brackets.

Str3 = Str1+Str2 # this makes one string, 'textwords'
print Str3
Str4 = Str1+'abc'+Str2
print Str4
Str5 = Str1+' '+Str2
print Str5

# If you need to convert a number to a string, there are many built-in
# functions http://www.pitt.edu/~naraehan/python2/data_types_conversion.html

str(675) #this returns a string '675'. You can't do math with strings
float('891') #this returns a number 891, which can have operations done

#There are LOTS of helpful libraries built into Anaconda that you can use.

#If you're ever unsure, the documentation is great--google "X python" and
#you'll almost certainly find the function to achieve X

#Here are some functions you may want to know:

int(9.8) #use the int() function to remove the non-integer part (round "down")
round(-3.1) #round toward closest whole number

#lots of other functions are in the "math" library
# https://docs.python.org/2/library/math.html


''' Input/Output (I/O) '''
#https://www.tutorialspoint.com/python/python_files_io.htm

# In this class, we'll be importing data from different instrumentation. It
# won't always come in forms that Python can instantly read!

# Import the test data file (in CSV, comma-separated values, format)

filename = 'test.csv' #make sure that you're in the right directory above
    #you can check your directory by typing "pwd" in the console

data = np.genfromtxt(filename, delimiter=',')
#The numpy function "genfromtxt" works well, as does the built-in csv library

# We'll look at some of these examples when we have some actual data

## Graphics and Plots
'''Matplotlib works well for us!'''
# http://matplotlib.org/
# http://matplotlib.org/users/pyplot_tutorial.html

# We'll go over graphics and plots in more detail later in this course.
# Here are the basics of plotting in Python:

# Plot data from the section above by creating a figure() placeholder and
# filling it with a plot()

import matplotlib.pyplot as plt
plt.plot(data[:,0],data[:,1]) #plot the first column as x-axis, second as y
plt.ylabel('Fun Numbers')
plt.show()

#This plot doesn't look *amazing* with the default settings.
# Instead, plot data as red points with a connecting line (using linespecs)
plt.plot(data[:,0],data[:,1],'r--') #plot the first column as x-axis, second as y
plt.ylabel('Fun Numbers')
plt.show()

#The dotted red line also doesn't look amazing, but you can play around!
# http://matplotlib.org/users/pyplot_tutorial.html#controlling-line-properties

# This time, let's introduce some more complex plotting options.
# You can modify the plot by calling functions such as
# plt.title(), plt.xlabel(), etc.

# Fabricate a data set
V = np.arange(1,9,0.1)
U = np.arange(9,1,-0.1)

# Concatenate vectors and take some averages and standard deviations
H = np.concatenate((V,U))
M = np.mean(H)
S = np.std(H)

eH = np.exp(H);
sH = np.sin(H);

plt.plot(H,sH) #plot the first column as x-axis, second as y
plt.ylabel(r'Awesomeness$_{xyz}$') #use LaTeX-like formatting to get sub/super
plt.title('Awesome Plot')
plt.xlabel(r'Monkey seconds$^{-2}$')
plt.axis([1, 9, -1, 1]) #xmin, xmax, ymin, ymax
plt.savefig('fun.png') #this saves the plot as a graphic
plt.show()


#more LaTeX-like commands can be found at http://matplotlib.org/users/mathtext.html


## Programming

# Not surprisingly, you can do a bunch of programming and control flow

# "while" structures do something until the statement is no longer true
clock = 10
while clock>0:
    print clock #this just displays the variable
    clock = clock - 1; #you can also type "clock -= 1"
 #there is no explicit end command, unlike MATLAB

# Be careful with things that are "while true": they will keep going
# forever!

# "for" loops iterate for a set number of time
item = ['a','b','c','d','e','test','value','fxn','loop','for']
for L in range(0,10):
    print item[L] #print out the L-th string in the cell "item"
    
#if/elif/else examine many logical statements to decide what to do
hello = 'bonjour'

if hello=='welcome':
    print('greeting is in English')
elif hello == 'bonjour':
    print('greeting is in French')
else:
    print('greeting is in other language')
    
#try changing the variable "hello" and run the block above again
    

#try/except can allow MATLAB to continue if something throws an error

#xx = 45 #this is undefined to see what will happen
try:
    print 'the number is %f' % xx # #f is a float number, \n is new line
except:
    print('you did not define the variable xx!')

#try defining xx and see what happens!



# You can also break control flow statements with the following:

'''
break: ends the for or while loop
continue: pass to the next iteration of a for loop
pass: put into a loop section to skip the entire thing

return: if a function is running, return to the home script with a value for the variable
'''


# Try combining different flow control types in nested groups!



## Analysis

# We'll have a class dedicated to data analysis
# Stay tuned for more information!

