# Programming Basics questions

## Computer science

### Data structures

#### What is the purpose of a list (array in some programming languages) data structure? Name some methods of it!
a list is used to store and ordered collection of items,list elements can be any data type. 
some methods of lists:pop(),sort(),append(),count(),remove()
#### What is the difference between a list/array and a set?
the elements in a set ar immutable,set elements don't have indexes and there can't be duplicate elements in a set
#### What is the purpose and methods of a dictionary/map data structure?
a dictionary holds pairs of values (key + value) since python 3.7 dictionaries are an ordered data structure(insertion ordered). 
some example methods:get(),fromkeys(),pop(),keys(),items()

### Algorithms

#### Fibonacci sequences. Write a method (or pseudo code), that generates the Fibonacci sequences.
        def fibonacci(length):
            numlist = [0, 1]
            for index in range(2, length):
                numlist.append(numlist[index - 1] + numlist[index - 2])
            return numlist

#### How do you find a max value in a list/array if you can’t use any built-in functions?
Initialize a variable named "max" with the first item of the array.
Iterate through the list.
If an item of the list is greater than the max variable: assign the value of that item to the max variable.
    
    def max(values_list):
        max = values_list[0]
        for i in values_list:
            if max < values_list[i]:
                max = values_list[i]
        return max

#### How do you find the average of values in a list/array if you can’t use any built-in functions?
Divide the sum of list items by the length of the list
         def average(value_list):
            return sum(value_list) / len(value_list)
#### What do we call an *in-place* sort?
a sorting algorithm that doesnt use additional memory space and produces the output in the same memory space that contains the data
#### Explain an algorithm which sorts a list!
initialize two lists(greater and lower)
if the length of the list to sort is less than 1: return the list
initialize pivot variable with the last element of our list as its value
iterate through the items in the list
if the item is greater than our pivot variable, add it to the greater list
if its lower than our pivot, add it to the lower list
sort the greater and lower list with the same   method, add our pivot in the middle and return the concatenated list
    
    def quicksort(sequence):
        greater = [] 
        lower = []  # initialize two lists(greater and lower)
        if len(sequence) < 1:
            return sequence     #if the length of the list to sort is less than 1: return the list
        pivot = sequence.pop()  #initialize pivot variable with the last element of our list as its value
        for item in sequence: #iterate through the items in the list
            if item > pivot: 
                greater.append(item)  #if the item is greater than our pivot variable, add it to the greater list
            else:
                lower.append(item)  #if its lower than our pivot, add it to the lower list
        return quicksort(lower) + [pivot] + quicksort(greater) #sort the greater and lower list with the same   method, add our pivot in the middle and return the concatenated list
### Programming paradigms - procedural

#### What is the call stack?
a stack of the called methods in the program in order of them being called(first in last out)
#### What is “Stack overflow”?
a stack overflow is when the call stack pointer exceeds the stack bound.
Meaning the program attempts to use more memory than is available for the stack.
#### What are the main parts of a function?
definition("def") that marks the start of a function and function name
arguments(optional)
docstring(optional)
function body
return statement(optional)

### Programming languages - Python  
#### How do you use a dictionary in Python?
#### What does it mean that an object is immutable in Python?
an object being immutable means it can't be modified in memory.
#### What is conditional expression in Python?
an expression that executes a block of code based on the given condition being true or false
#### What are different types of arguments in Python?
default arguments.
keyword arguments.
positional arguments.
arbitrary arguments.
#### What is variable shadowing? (context: variable scope)
shadowing is when a variable is declared within a certain scope with the same name as a variable in an outer scope
#### What can happen if you try to delete/drop/add an item from a List, while you are iterating over it in Python?
if you delet a list item while iterating over the list the deleted item will simply be removed from the list.
if you add an item it gets added to the list and will be iterated over like the other items
#### What is the "golden rule" of variable scoping in Python (context: LEGB)? What is the lifetime of variables?
the LEGB rule determines the order in wich python looks up variable names.
when a variable is referenced python will look that name up sequentially in the local, enclosing, global, and built-in scope, giving the first occurence of it or an error if it's not found.

The lifetime of variables inside a function is as long as the function executes, they are destroyed after the function returns or terminates.
Global variables live from when the module is imported until the end of the application - unless the variable is explicitly deleted.
Built-in variables live from the start of the interpreter until the code exits.
#### If you need to access the iterator variable after a for loop, how would you do it in Python?
#### What type of elements can a list contain in Python?
#### What is slice operator in Python and how to use?
#### What arithmetic operators (+,*,-,/) can be used on lists in Python? What do they do?
#### What is the purpose of the in and not in membership operators in Python?
#### What does the + operator mean when used with strings in Python?
#### Explain f strings in Python?
#### Name 4 iterable types in Python!
#### What is the difference between list/set/dictionary comprehension and a generator expression in Python?
#### Does the order of the function definitions matter in Python? Why?
#### What does unpacking mean in Python?
#### What happens when you try to assign the result of a function which has no return statement to a variable in Python?

## Software engineering

### Debugging

#### What techniques can you use while debugging a program in Python?
#### What does step over, step into and step out mean while using the debugger?
#### How can you start to debug a program from a certain line using the debugger?

### Version control

#### What are the advantages of using a version control system?
#### What is the difference between the working directory, the staging area and the repository in git?
#### What are remote repositories in git?
#### Why does a merge conflict occur?
#### Through what series of commands could you put a new file into a remote repository connected to your existing local repository?
#### What does it mean atomic commits and descriptive commit messages?
#### What’s the difference between git and GitHub?

## Software design

### Clean code

#### What does clean code mean?
code that is easy to understand and easy to change.
variable and function names are easy to understand
methods are small and only have single responsibility
doesn't contain any dead or duplicate code


#### What steps do we usually do during a clean code refactoring?
rename variables and functions if their names aren't easy to understand.
extract duplicate code to seperate functions.
extract complicated expressions into seperate variables to make them easier to understand.
make sure our codes functionality is unchanged
### Error handling

#### What is exception handling?
The mechanism of handling unexpected errors a program so that the program's execution flow isn't interrupted.

#### What are the basics of exception handling in Python?
Exceptions can be handled with a try statement.
The code which may raise an exception is placed inside the try clause. The code that runs in case of an exception is written in the except clause.
So we can choose what operations to perform if an exception occurs

#### In which case should we catch an exception? Why?
We should only catch an exception if we know how to handle it 

#### What can/should we do with an exception in the ‘except’ block?

#### What does the else and finally statement do in a try-except block in Python?
the else statement runs if the code in the try block didn't raise any errors.
the finally statement always runs.
## Software Development Methodologies

#### What is the main goal of a retrospective meeting?
To reflect on what worked and what didn't work during a project. 
As to not repeat the same mistakes.

## Programming environment

### Unix

#### What is UNIX and what is Linux?
Unix is a family of OSes derived from the original at&t unix
Linux is a family of OSes derived from unix
#### What do we call the shell in Linux?
an interface that allows the user to run commands
#### What does root means in a Linux environment?
root refers to the root user that has access to all commands and files or the root directory of a drive
#### How do you access your personal files in Linux?
navigate to the /home/username folder
#### How can you install an application in Linux?
apt-get install
#### What is package management in Linux, what are repositories?
Package management is a way of installing, updating, removing software from repositories
A repository(repo) is a storage location for software packages
#### How do you navigate in the filesystem with the command line?
you can change directories with the cd command
#### What does the following commands do: mkdir, rm, cat, cp, touch?
mkdir:makes a new directory
rm:removes a file
cat:create or edit a file with content
cp:copies files and directories
touch:create a file without content
#### How can you look up what does a command do in Linux if you have no internet connection?
help [command] or man -k [command] or info [command]
#### What does the following commands do: head, tail, more, less?
head outputs the first 10 lines of a file or the first n lines if -n is used
tail outputs the last 10 lines of a file or the last n lines if -n is used
more outputs the contents of a file and lets you navigate the file by lines(enter) or by pages(spacebar)
less is similiar to the more command but allows you to navigate with arrow keys

#### How do you download a file from internet using the terminal?
use the wget [url] or curl [url] command
