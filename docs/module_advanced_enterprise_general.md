# General enterprise questions

## Software engineering

### Architectures

#### What is n-tier (or multi-tier) architecture?

n-tier architecture is an architecture where the processing, data management, and presentation functions are physically and logically separated.

#### What are microservices? Advantages and disadvantages?

A microservice architecture is a variant of SOA, it arranges an application as a collection of loosely-coupled services independent of eachother.
The main advantages of a microservice architecrue are modularity and scalability.
And some disadvantages are increased complexity,more difficult debugging and testing and more complex deployment.

#### What is Separation of Concerns?

Seperation of Concerns(SoC)is a software development concept that separates an application or a software into different sections, or concerns, where each concern has a different purpose.

#### What is a layered design and why is it important in enterprise applications?

A layered software design is one in which when the call relationships among different modules are represented graphically,
it would result in a tree-like diagram with clear layering. In the layered design, the modules are arranged in the hierarchy of layers.
presentation layer
business layer
persistence layer
database layer

#### What is Dependency Injection?

Dependency injection is basically providing the dependencies that an object needs instead of having it construct them itself.
It's a very useful technique for testing, since it allows dependencies to be mocked or stubbed out.

#### What is the DAO pattern? When and how to implement?

The Data Access Object (DAO) pattern is a structural pattern that allows us to isolate the application/business layer from the persistence layer (usually a relational database but could be any other persistence mechanism) using an abstract API.

#### What is SOA? When to use?

service-oriented architecture (SOA) is an architectural style that focuses on discrete services instead of a monolithic design.
A form of SOA is the microservice architecture.

### Testing

#### What are unit test, integration test, system test, regression test, acceptance test? What is the major difference between these?

Unit testing is a type of software testing which is done on an individual unit or component to test its corrections. Typically, Unit testing is done by the developer at the application development phase.

Integration testing is a type of software testing where two or more modules of an application are logically grouped together and tested as a whole. The focus of this type of testing is to find the defect on interface, communication, and data flow among modules.

System testing is types of testing where tester evaluates the whole system against the specified requirements.
It involves testing a complete application environment in a situation that mimics real-world use, such as interacting with a database, using network communications, or interacting with other hardware

Regression testing is testing of unchanged features of the application to make sure that any bug fixes, adding new features, deleting, or updating existing features, are not impacting the working application.

Acceptance testing is a type of testing where client/business/customer test the software with real time business scenarios.
The client accepts the software only when all the features and functionalities work as expected.

#### What is code coverage? Why is it used? How you can measure?

Code coverage is a software testing metric that determines the number of lines of code that is successfully validated under a test procedure.
A coverage percentage is calculated by (Number of lines of code executed by tests/Total number of lines of code in a component) \* 100

#### What does mocking mean? How would you do it 'manually' (i. e. without using any fancy framework)?

Mocking means creating a fake version of an external or internal service that can stand in for the real one, helping your tests run more quickly and more reliably.
When your implementation interacts with an object's properties, rather than its function or behavior, a mock can be used.
We can create mock classes manually using polymorphism.

#### What is a test case? What is an assertion? Give examples!

A test case is a set of actions performed on a system to determine if it satisfies software requirements and functions correctly.
An assertion is basically just a Boolean expression that is evaluated by a test.
For example:

        Assert.AreEqual(expected, actual)

#### What is TDD? What are the benefits?

Test driven development is a development process where tests are written before code. New code is only written if a test fails.
Fewer bugs and errors are the primary benefit of the TDD approach.
Also TDD produces a higher overall test coverage and, therefore to a better quality of the final product.

#### What are the unit testing best practices? (Eg. how many assertion should a test case contain?)

Proper unit tests should fail for exactly one reason, meaning they should containt only one assertion.

#### What is arrange/act/assert pattern?

Arrange(inputs and targets):
the arrange act assert pattern is a pattern for writing tests.
arrange steps should set up the test case like preping a database,login to a web service or any other setup needed.

Act(on the target behavior):
Act steps should cover the main thing to be tested.
Like calling a function or method, calling a REST API, or interacting with a web page.

Assert(expected outcomes):
The act steps produce a response.
Assert steps verify if the response from the act step pass or fail.

### DevOps

#### What is continuous integration? Why is CI important?

Continuous integration is a DevOps software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run
CI is important because it allows developers to merge their code in smaller steps, thus makes merging easier.

#### Why are tests important in the CI workflow?

Most of the changes in a CI pipeline are small. Test automation alleviates much of the manual testing that comes with small changes and enables the team to continually deliver a steady stream of small changes that have been thoroughly tested.

#### Name some software that help the CI workflow!

Docker,Github Actions,Azure pipelines

#### What is Continuous Delivery?

Continuous delivery is a software development practice where code changes are automatically prepared for a release to production

#### What is Continuous Deployment?

Continuous deployment is a strategy in software development where code changes to an application are released automatically into the production environment

#### What is DevOps?

DevOps is a set of practices that combines software development (Dev) and IT operations (Ops). It aims to shorten the systems development life cycle and provide continuous delivery with high software quality.

### Software Methodologies

#### What kind of software-lifecycle models do you know?

Waterfall model:
The waterfall model is a continuous software development model in which development is seen as flowing steadily downwards (like a waterfall) through the steps of requirements analysis, design, implementation, testing (validation), integration, and maintenance.

Agile model:
Agile methodology is a practice which promotes continues interaction of development and testing during the lifecycle of any project. In the Agile method, the entire project is divided into small incremental builds. All of these builds are provided in iterations, and each iteration lasts from one to three weeks.

Big bang model:
Big bang model is focusing on all types of resources in software development and coding, with no or very little planning. The requirements are understood and implemented when they come.

#### What is a UML diagram? What kind of diagram types do you know?

A UML diagram is a diagram based on the Unified Modelin Language, it's meant to represent a system with it's main actors,roles and actions to make the workings of the system easier to understand.
UML diagram types include:
Class diagrams,Use case diagrams,Component diagrams and Communication diagrams among others.

#### What is a UML class diagram? What are the typical elements?

Class diagrams are the blueprints of a system. You can use class diagrams to model the objects that make up the system, to display the relationships between the objects and the actions of the objects.

#### What kind of design patterns do you know? Bring at least 3 examples.

Builder:
Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

Singleton:
Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

Factory:
Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

#### What is the purpose of the Iterator Pattern?

The main idea of the Iterator pattern is to extract the traversal behavior of a collection into a separate object called an iterator.
In addition to implementing the algorithm itself, an iterator object encapsulates all of the traversal details, such as the current position and how many elements are left till the end.

#### What do you know about the SOLID principles?

SOLID stands for:

Single-responsiblity Principle: A class should have one and only one reason to change, meaning that a class should have only one job.

Open-closed Principle: Objects or entities should be open for extension but closed for modification.
This means that a class should be extendable without modifying the class itself.

Liskov Substitution Principle: Every subclass or derived class should be substitutable for their base or parent class.

Interface Segregation Principle: A client should never be forced to implement an interface that it doesn’t use, or clients shouldn’t be forced to depend on methods they do not use.

Dependency Inversion Principle: Entities must depend on abstractions, not on concretions. High-level module must not depend on the low-level module, but they should depend on abstractions.

#### How would you separate data storage code and business logic code (which uses stored data) in an application?

You can separate business logic from data access using the dao pattern for example.

## Computer science

### Data Structures

#### What is the difference between Stack and Queue data structure?

the main difference is that a stack works on the FILO(first in last out) principle, while a queue works on the FIFO(first in first out) principle.

#### What is a graph? What are simple graphs? What are directed graphs? What are weighted graphs?

A Graph is a data structure consisting of vertices and edges.

Weighted graphs:graphs whose edges or paths have values. All the values seen associated with the edges are called weights.

Simple Graph:An undirected unweighted without loops or multiple edges.

Directed Graph:A graph with directional vertices.

#### What are trees? What are binary trees? What are binary search trees?

a tree is a hierarchical data structure that consists of nodes connected by edges.

binary tree:A tree with at most 2 child nodes

Binary search trees are defined by 3 characteristics:
The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.

#### How can you store graphs in programs? What are the advantages/disadvantages per each?

Edge lists
One simple way to represent a graph is just a list, or array, of edges. To represent an edge, we just have an array of two vertex numbers.

Adjacency matrices
For a graph with n vertices, an adjacency matrix is a n\*n matrix of 0s and 1s, where the entry in row i and column j is 1 only if the edge (i,j) is in the graph.

Adjacency lists
Representing a graph with adjacency lists combines adjacency matrices with edge lists. For each vertex i i ii, store an array of the vertices adjacent to it.

#### What are graph traversal algorithms? What is BFS, how does it work? What is DFS, how does it work?

Breadth first search:From a selected start node, explore all nodes on the same depth before moving on to the next depth level.

Depth first search: From a selected starting node,exploring each branch as far as possible before backtracking.

#### How does dictionary work?

dictionary or hash map,hash table:
A hash table uses a hash function to compute a hash code into an array of buckets or slots, from which the value can be found. During lookup, the key is hashed and the resulting hash indicates where the value is stored.

#### Why is it important for keys in a hashmap to have an immutable type? (Consider string for example.)

Because changing the value of the key changes the hashcode as well then if you try to look up the same object in the dictionary it won’t be found because its hash value is different.

### Algorithms

#### What is QuickSort? Describe the main logic of this sorting algorithm.

Quicksort is an in place sorting algorithm.
it goes like this:
initialize two lists(greater and lower)
if the length of the list to sort is less than 1: return the list
initialize pivot variable with the last element of our list as its value
iterate through the items in the list
if the item is greater than our pivot variable, add it to the greater list
if its lower than our pivot, add it to the lower list
sort the greater and lower list with the same method, add our pivot in the middle and return the concatenated list

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

## Software design

### Security

#### What is OAuth2?

OAuth 2.0, which stands for “Open Authorization”, is a standard designed to allow a website or application to access resources hosted by other web apps on behalf of a user.

#### What is Basic Authentication?

basic access authentication is a method for an HTTP user agent(usually a web browser) to provide a user name and password when making a request.

#### What is CORS, why it’s needed in browsers?

Cross-origin resource sharing is a mechanism that allows restricted resources on a web page to be requested from another domain outside the domain from which the first resource was served.
It's needed to prevent XS(cross-site) attacks.

#### How can you initialize a CSRF attack?

the main steps of a csrf attack:

Identifying and exploring the vulnerable website for functions of interest that can be exploited

Building an Exploit URL(for example:"https://myfriendlybank.com/account/transfer?amount=15000&accountNumber=4567876")

Creating an Inducement for the Victim to open the Exploit URL(for example:including the exploit URL in HTML image elements)

#### What is JWT used for? Where to store it on client side?

JWT is an open standard used to share security information between two parties(client and server).
Use cookies to store JWT tokens – always secure, always httpOnly, and with the proper same site flag.

### Threaded programming

#### When do you need to use threads in an application?

You should use multithreading when you want to perform heavy operations without stopping the flow of the program.
Example in UIs where you do a heavy processing in a background thread but the UI is still active.

#### What is a daemon thread?

A Daemon thread(background thread in c#) is a background service thread which runs as a low priority thread and performs background operations like garbage collection.

#### What is the difference between concurrent and parallel execution of code?

Concurrency means that an application is making progress on more than one task at the same time.

Parallelism means that an application splits its tasks up into smaller subtasks which can be processed in parallel.

#### What is the most important problem developers are faced when using threads?

the most important problem is synchronization, as multi threading can cause deadlocks if not properly in sync.
We say that a set of processes or threads is deadlocked when each thread is waiting for an event that only another process in the set can cause.

#### In what kind of situations can deadlocks occur?

The four necessary conditions for a deadlock situation to occur are mutual exclusion, hold and wait, no preemption and circular set.

Mutual Exclusion: Only one process can use a resource at any given time

Hold and wait: A process is holding at least one resource at a time and is waiting to acquire other resources held by some other process.

No preemption: The resource can be released by a process voluntarily,after execution of the process.

Circular Wait: A set of processes are waiting for each other.

#### What are possible ways to prevent deadlocks from occurring?

Deadlocks can be prevented by preventing on of the 4 required conditions listed above.

#### What does critical section or critical region mean in the context of concurrent programming?

a block of code that accesses a shared resource and can't be executed by more than one thread at the same time.
