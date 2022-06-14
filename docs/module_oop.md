# OOP questions

## Software design

### Error handling

#### What does 'fail fast' mean in terms of exception handling? Why is it a good practice?
fail fast means stopping the program the moment any unexpected error occurs.

## Computer Science

### Data structures

#### How to find the middle element of singly linked list in O(n)?
Two-Pass: Find the length of the linked list and return the (length/2)th node.

One-Pass: Use two pointers, the 2nd pointer should traverse twice as fast at the first pointer.
when the 2nd pointer reaches the end of the linked list, the 1st pointer will be at the middle of the linked list.

#### Given an array of integers going from 1 to 100 (both inclusive) there is a duplicated entry. How to find it?
add up all the elements of the list and compare it to the sum of numbers from 1 to 100. the difference between the two will be the duplicate number.
#### What is a linked list? How to find if a linked list has a loop?
A linked list is a linear data structure in which the elements are not connected directly but rather they are connected by pointers.
the fastest way to find a loop in a linked list is to: 
Traverse linked list using two pointers.
Move one pointer(slow_p) by one and another pointer(fast_p) by two.
If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t have a loop.
#### What is the Big O time complexity of the common operations in an ArrayList, LinkedList, HashMap? And of a bubble sort, quicksort, finding items in a Binary Search tree?
Arraylist:
Add:O(1), worst case it's O(n).
Remove:O(n).
Get:O(1).

LinkedList:
Add:O(1).
Remove:O(n).
Get:O(n).

HashMap:
Add:O(1).
Get:O(1).
Remove:O(1).

#### How does HashMap work?
HashMap is a data structure that stores key-value pairs.
The key is used to access the value.
The key is hashed to get the index of the value.
The value is stored in an array at the index of the hash.
#### Why is it important for keys in a map to have an immutable type? (Consider String for example.)
To make sure that the hash of the key remains constant.

### Database

#### How can you connect your application to a database server? What are the possible ways?
You can connect to a database server using the JDBC driver.
#### What do you know about database normalization?
Database normalization is the process of structuring a relational database in accordance with a series of so-called normal forms in order to reduce data redundancy and improve data integrity.
### Other

#### What is a garbage collector, in a nutshell?
A garbage collector is a process that cleans up memory by removing unused objects.

## Programming paradigms

### Procedural

#### What is casting? What is the difference between up vs downcasting?
Casting is the process of converting one type of object to another type of object.
Upcasting is the process of converting a subclass object to a superclass object.
Downcasting is the process of converting a superclass object to a subclass object.
#### Which order should we catch the exceptions? Why?
When catching exceptions you want to always catch the most specific first and then the most generic last.
This helps you to avoid the possibility of catching a more general exception than the one you actually want to catch.

### Object-oriented

#### What is a class?
A class is a blueprint for an object.
#### What is an object?
An object is an instance of a class.
#### What is a constructor?
A constructor is a special method that is called when an object is created.
#### Do we require parameter for constructors?
No.
#### What is an interface?
An interface is a completely abstract class that defines the behavior of a class.
#### What are access modifiers?
Access modifiers are used to control the access of variables and methods(public,private,protected and default is package private).
#### What is data hiding?
Data hiding is the process of hiding data by using private and protected modifiers.
#### Can a static method use non-static members?
No. Non-static members can't be accessed from a static method.
#### What is the difference between hiding a static method and overriding an instance method?
Hiding a static method of a superclass looks like overriding an instance method of a superclass.
When we override an instance method, we get the benefit of run-time polymorphism bit when we override a static method we do not.

#### Define the following terms: Instantiation, Attribute, Method
Instantiation: The process of creating an object from a class.
Attribute: A property of an object.
Method: a block of code which only runs when it is called.
#### Could we access a static variable (or method) from a non-static method? Why?
We can't. Static variables and methods can only be accessed from a static context.
#### Could we access a non-static variable (or method) from a static method? Why?
We can't. Non-static variables and methods can only be accessed from a non-static context.
#### How many instances you have of a static variable of a given class?
There is only one instance of a static variable of a given class.
#### Why is it not a good practice to write a lot of static methods?
It makes testing harder.
Since static methods belong to the class and not a particular instance, mocking them becomes difficult and dangerous.
Also static methods remain in the memory for a log time and its garbage collection takes long time. We don't have control on destroying or creating of Static variables. Excessive usage of static variables can result in the memory overflow.
#### What are the features of static attributes and static methods of a class? What are the benefits, when to use them?
The static variable can be used to refer to the common property of all objects
A static method can be invoked without the need for creating an instance of a class.
A static method can access static data member and can change the value of it.

#### What is the ‘this’ reference?
The ‘this’ reference is a reference to the current object.
#### What are base class, subclass and superclass?
Base class: The class which is the superclass of the other classes.
Subclass: The class which is the subclass of the other classes.
Superclass: The class which is the superclass of the other classes same as Base class.
#### Draw an object oriented family (as entities, with relations) on the whiteboard.
...
#### Difference between overloading and overriding?
Overloading is the process of creating multiple methods with the same name but different signatures.
#### What are the Object Oriented Principles? Explain the concepts with realistic examples!
The principles are:
1. Encapsulation: Hiding the data from the outside world.
2. Inheritance: The ability to create new classes from existing classes.
3. Polymorphism: The ability to use the same method name in different ways.
4. Abstraction: The process of hiding the details of a class.

#### What is method overloading?
Method overloading is the process of creating multiple methods with the same name but different signatures.
#### What is method overriding?
Method overriding is the process of creating a method in a subclass that overrides the same method in the superclass.
#### Explain how object oriented languages attempt to simplify memory management for Programmers.
By using a garbage collector to make memory management automatic and the language memory safe.
#### Explain the “Single Responsibility” principle!
The principle states that a class should have only one reason to change(Should only have a single purpose/action).
#### What is an object oriented program? Explain, show.
An object oriented program is a program that is written in an object oriented manner,keeping in mind the principles of OOP.
#### How do you make a class immutable? What do you need to watch out for?
The class must be declared as final so that child classes can’t be created.
Data members in the class must be declared private so that direct access is not allowed.
Data members in the class must be declared as final so that we can’t change the value of it after object creation.
A parameterized constructor should initialize all the fields performing a deep copy so that data members can’t be modified with an object reference.
Deep Copy of objects should be performed in the getter methods to return a copy rather than returning the actual object reference)


#### How many instances can be created for an abstract class?
An abstract class cannot be instantiated.
## Programming languages

### Java

#### What is autoboxing and unboxing?
Autoboxing is the process of converting primitive data types to object data types.
Unboxing is the process of converting object data types to primitive data types.
#### If you have a variable, that shall store a positive whole number between 0 and 200, what primitive type would you use to store it?
int
#### What is the "golden rule" of variable scoping in Java? What is the lifetime of variables?
The golden rule is that a variable declared in a block is in scope inside the block in which it is declared, but it is not accessible outside of this block.
The lifetime of variables is the time during the variable stays in memory and is not garbage collected.
 #### What is the purpose of the ‘equals()’ method?
The purpose of the ‘equals()’ method is to compare two objects and return true if they are equal.
#### What is the difference between '==' and 'equals()'?
== is used for reference comparison. It compares only the reference of the objects.
equals() is used for value comparison. It compares the value of the objects.
#### What does the ‘static’ keyword mean?
The ‘static’ keyword is used to declare a variable or method as static meaning that it can be accessed without instantiating the class it belongs to.
#### Why is the main() method declared as static? Explain.
The main() method is static so that JVM can invoke it without instantiating the class. This also saves the unnecessary wastage of memory which would have been used by the object declared only for calling the main() method
#### What is the default access modifier in a class?
package private
#### What is the JVM?
The JVM is the Java Virtual Machine wich is used to run java class files.
#### What is the difference between the JRE and the JDK?
The JRE is the Java Runtime Environment and the JDK is the Java Development Kit.
#### What is the difference between long and Long?
long is a primitive type and Long is a class(thus it inherits the Object class).
#### Can a long store bigger numbers than a Long?
No.
#### What kind of packages do you know under java.util.* ? Bring at least 3 examples.
List,ArrayList,LinkedList,HashMap,HasheSet...
#### What are the access modifiers in Java? Which one could we use for class?
public, private, protected, package private(default)
#### Can an “enum” contain methods in Java? Explain.
Yes. An “enum” can contain methods, usually to get the value associated with the enum literal.
#### When would you use a private/protected/public attribute? What is the difference?
Private attribute is used to restrict the access to the class.
Protected attribute is used to restrict the access to the class and its subclasses.
Public attribute lets the class be accessed by any other class.
Package private attribute is used to restrict the access only to classess in the same package.
#### How do you prevent developers from subclassing a class?
You can use the final keyword in the class declaration.
#### How do you prevent developers from overriding a method in a subclass?
You can use the final keyword in the method declaration.
#### How do you prevent developers from changing the value of a variable?
You can use the final keyword in the variable declaration.
#### Think about money ;) How would you store a currency value, that shall support decimal parts? Think it through again, and try to think outside of the box!
Using a BigDecimal object.
Alternatively you can use the Joda-Money library.
#### What happens if you try to call something, that you have no access to, because of data hiding?
The compiler will throw an error like: method() has private access in class.
#### What happens if you try to delete/drop an item from an array, while you are iterating over it?
You can't delete items from an array, you can only change their reference to null
#### What happens if you try to delete/drop/add an item from a List, while you are iterating over it?
A ConcurrentModificationException will be thrown.
#### What happens if you try to add an item to the end of an array, while you are iterating over it?
You cant add items to the end of an array as it's size is fixed.
#### If you need to access the iterator variable after a for loop, how would you do it?
declare the iterator variable outside the for loop.
#### Which interfaces extend the Collection interface in Java. Which classes?
List,Set,Queue,Map interfaces extend the Collection interface.
ArrayList,LinkedList,HashSet,HashMap,TreeSet,TreeMap classes implement the Collection interface.
#### What is the connection between equals() and hashCode()? How are they used in HashMap?
If two objects are equal(according to equals() method) then the hashCode() method should return the same integer value for both the objects
In HashMap, hashCode() is used to calculate the bucket and therefore calculate the index. 
HashMap uses equals() to compare the key whether they are equal or not.
#### What is the difference between checked exceptions and unchecked exceptions? Could you bring example for each?
Checked exceptions are exceptions that are checked at compile time. If some code within a method throws a checked exception, then the method must either handle the exception or it must specify the exception using the throws keyword. 
for example: IOexception.
Unchecked exceptions are the exceptions that are not checked at compile time for example: 
dividing by zero throws java.lang.ArithmeticException: / by zero

#### What is Error in Java and how does it relate to Exception?
An error is a subclass of Throwable that tells that something serious problem is existing and a reasonable Java application should not try to catch that error.
#### When does 'finally' block run? What it is used for? Could you give an example from your projects when you would use 'finally'?
When a try block is finished, the finally block will run regardless if an exception is thrown or not.
for example it can be used to close a file or a database connection.
#### What is the largest number you can work with in Java?
The max value of int in java is 2147483647.
BigInteger however can store numbers up to a value of 9223372036854775807.

#### When you use method overriding, can you change the access level of the method, from protected to public? Why?When you use method overriding, can you change the access level of the method, from public to protected? Why?
You can change the access level of the method but it cannot lower the access level of the method.
No. See above.
#### Can the main method be overridden? Explain your answer!
the main method can be overloaded but not overriden because it's a static method.
#### When you use method overriding, can you throw fewer exceptions in the subclass than in the parent class? Why?
Yes you can throw fewer exceptions but you can't throw more exceptions that are not declared in the parent class.
#### When you use method overriding, can you throw more exceptions in the subclass than in the parent class? Why?
No you can't throw more or broader exceptions that are not declared in the parent class.
#### What does "final" mean in case of a variable, method or a class?
final variables have a constant value and can't be changed, final methods can't be overridden, final classes can't be subclassed.
#### What is the super keyword?
The super keyword is used to refer to the parent class.
#### What are “generics”? When to use? Show examples.
Generics are a way to define a class or method that can be used with different types.
for example: List<GenericType> list = new ArrayList<>();
they are used when you want to use a class or method with different types.
#### What is the benefit of having “generic” containers?
Stronger type checks at compile time.
Elimination of casts.
#### Given two Java programs on two different machines. How can you communicate between the two? What are the possible ways?
You can use the serialization technique to serialize the objects and then send them over the network.
You can use Terracotta, or network Sockets to communicate between the two machines.
#### What is an annotation? What can be annotated and how? Show examples.
Annotations are used to add extra information to a class, method or variable.
for example: @Override

### C&#35;

#### Explain the purpose of IL and how does it relate to CLR?
#### What does “managed code” mean?
#### What is an assembly?
#### What is the difference between an EXE and a DLL?
#### What is the difference between `dotnet build` and `dotnet restore`?
#### What is strong-typing versus weak-typing? Which is preferred? Why?
#### What is a namespace?
#### Explain sealed class in C#?
#### What is explicit vs. implicit conversion? Give examples of both of them.
#### Is a struct stored on the heap or stack?
#### Can a struct have methods?
#### Can DateTimes be null?
#### List out the differences between Array and ArrayList in C#?
#### How is the using() pattern useful? What is IDisposable? How does it support deterministic finalization?
#### How can you make sure that objects using dedicated resources (database connection, files, hardware, OS handle, etc.) are released as early as possible?
#### Why to use keyword “const” in C#? Give an example.
#### What is the difference between “const” and “readonly” variables in C#?
#### What is a property in C#?
#### List out two different types of errors in C#?
#### What is the difference between “out” and “ref” parameters in C#?
#### Can we override private virtual method in C#?
#### What's the difference between IEquatable and just overriding Object.Equals()?
#### Explain the differences between public, protected, private and internal. Explain access modifier – “protected internal” in C#!
#### What’s the difference between using `override` and `new` keywords when defining method in child class?
#### Explain StringBuilder class in C#!
#### How we can sort the array elements in descending order in C#?
#### Can you use a value type as a generic type argument in C#? For example when implementing an interface like (IEquatable).
#### What are Nullable Types in C#?
#### Conceptually, what is the difference between early-binding and late-binding?
#### What is delegate, event, callback, multicast delegate?
#### What is enum in C#?
#### What is null-conditional operator?
#### What is null-coalescing operator?
#### What is serialization?
#### What is the difference between Finalize() and Dispose() methods?
#### How do you inherit a class from another class in C#?
#### What is difference between “is” and “as” operators in C#?
#### What are indexers in C# .NET?
#### What is the difference between returning IQueryable<T> vs. IEnumerable<T>?
#### What is LINQ? Explain the idea of extension methods.
#### What are the advantages and disadvantages of lazy loading?
#### How to use of “yield” keyword? Mention at least one practical scenario where it can be used?
#### What are attributes in C#? Give some examples of usage of them.
#### By what mechanism does NUnit know what methods to test?
#### What is the GAC? What problem does it solve?
#### What is the largest number you can work with in C#?
