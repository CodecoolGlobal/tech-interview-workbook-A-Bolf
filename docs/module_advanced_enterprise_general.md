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
A coverage percentage is calculated by (Number of lines of code executed by tests/Total number of lines of code in a component) * 100
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
#### What is a UML diagram? What kind of diagram types do you know?
#### What is a UML class diagram? What are the typical elements?
#### What kind of design patterns do you know? Bring at least 3 examples.
#### What is the purpose of the Iterator Pattern?
#### What do you know about the SOLID principles?
#### How would you separate data storage code and business logic code (which uses stored data) in an application?

## Computer science

### Data Structures
#### What is the difference between Stack and Queue data structure?
#### What is a graph? What are simple graphs? What are directed graphs? What are weighted graphs?
#### What are trees? What are binary trees? What are binary search trees?
#### How can you store graphs in programs? What are the advantages/disadvantages per each?
#### What are graph traversal algorithms? What is BFS, how does it work? What is DFS, how does it work?
#### How does dictionary work?
#### Why is it important for keys in a hashmap to have an immutable type? (Consider string for example.)

### Algorithms
#### What is QuickSort? Describe the main logic of this sorting algorithm.

## Software design

### Security

#### What is OAuth2?
#### What is Basic Authentication?
#### What is CORS, why it’s needed in browsers?
#### How can you initialize a CSRF attack?
#### What is JWT used for? Where to store it on client side?

### Threaded programming

#### When do you need to use threads in an application?
#### What is a daemon thread?
#### What is the difference between concurrent and parallel execution of code?
#### What is the most important problem developers are faced when using threads?
#### In what kind of situations can deadlocks occur?
#### What are possible ways to prevent deadlocks from occurring?
#### What does critical section or critical region mean in the context of concurrent programming?
