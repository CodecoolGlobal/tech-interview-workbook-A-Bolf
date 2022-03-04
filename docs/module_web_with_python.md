# Web with Python questions

## Software design

### Clean code

#### Point out 5 suggestions, how to format an SQL query!
Use consistent casing for your queries.
Use the AS keyword for creating aliases to make the code more readable.
Use indentation for better readability.
Use a new line for each separate query.
Use a new line for each separate column after a comma.
#### What layers can you name in a simple web application?
Front end(client-side)
Back end (server-side)

### Error handling
#### What error can occur, when an array does not have an element on the requested index?
We get an IndexError exception.
#### What is the “finally” block, and how would you use it?
The finally block can be used after a try except block. The code inside the finally block will always execute after catching the exception.
#### Why should we catch special exception types?
Because we should only catch exceptions that we except to be thrown and know how to handle.

### Security
#### What is SQL injection? How to protect an application against it?
an sql injection is a vulnerability that allows an attacker to run sql queries on your server by typing those queries into input fields in your web app.
you can protect an application from sql injections by sanitizing sql queries before they are ran on your server.
#### What is XSS? How to protect an application against it?
Cross-site scripting is a vulnerability that allows an attacker to send browser side scripts to other end users using the same web app.
By default jinja2 escapes all html code to prevent XSS attacks.
#### How to properly store passwords?
The best way to store passwords is to not store them at all and rather just store a hash of the password.
#### What is HTTPS?
Hypertext Transfer Protocol Secure is the TLS encrypted version of HTTP.
#### What is encryption and decryption?
Encryption is the process of turning plain-text into ciphertext using an encryption algorithm.
Decryption is the reverse of the proccess. Using the encryption key to decypher the ciphertext into plain-text.
#### What is hashing?
Hashing is the proccess of turning a string of any length into a fixed length hash by passing it through one or more one way mathematical functions.
#### What is the difference between encryption and hashing? When would you use which?
The main difference between encryption and hashing is reversibility. encrypted data can be decrypted if we have the encryption key but hashing is one way only,
hashing is generally used for storing passwords and encryption is mostly used for sending data that needs to be readable by the recipient.
#### What encryption methods do you know?
TLS,AES,SERPENT,TWOFISH
#### What hashing methods do you know?
MD-5,SHA-1/2/3,bcrypt
#### How/where would you store sensitive data (like db password, API key, ...) of your application?
I would store hashes of sensitive data in an sql database.
## Computer science

### Algorithms

#### What is the difference between Stack and Queue data structure?
Both are containers of objects. the main difference is that objects in a stack are inserted and removed using the last in first out principle.
objects in a queue are inserted and removed using the first in frist out principle
#### What is BubbleSort? Describe the main logic of this sorting algorithm.
bubble sort repeatedly steps through a list, compares adjacent elements and swaps them if they are in the wrong order. This is repeated until the list is sorted.

#### Explain the process of finding the maximum and minimum value in a list of numbers!
Initialize a variable named "max" with the first item of the array.
Iterate through the list.
If an item of the list is greater than the max variable: assign the value of that item to the max variable.
    
    def max(values_list):
        max = values_list[0]
        for i in values_list:
            if max < values_list[i]: //reverse the < sign to get the min value from the array
                max = values_list[i]
        return max

#### Explain the process of calculating the average value in an array of numbers!
Divide the sum of list items by the length of the list

        def average(value_list):
            return sum(value_list) / len(value_list)

#### What is Big O complexity? Explain time and space complexity!
The big o notation is used to describe how the run time or space requirement of an algorithm grows in relation to the input size.
time complexity describes the amount of time needed to run the algorithm in relation to the input size.
space complexity describes the amount of space needed to run the algorithm in relation to the input size.
#### Explain the process of calculating the average value in a list of numbers!
Divide the sum of list items by the length of the list

        def average(value_list):
            return sum(value_list) / len(value_list)

### Procedural
#### How the CASE condition works in SQL?
The case condition works like a switch-case statement
it checks through the conditions one by one and returns the values associated with the condition if it evaluates to true
if none of the conditions return true it returns the value in the else clause.
if none of the conditions are true and there is no else clause it returns NULL.
#### How the switch-case condition works in JavaScript?
The switch expression is evaluated once.
The value of the expression is compared with the values of each case, if there is a match code associated with the condition is executed
if none of the conditions match it executses the code in the default block
#### How to achieve a switch-case-like structure in Python?
By using the match-case statement introduced in python 3.10
#### Explain variable scoping in Python!
There are 4 types of variable scope in python.
Local scope:Local scope variables can only be accessed within its block.
Global scope:The variables that are declared in the global scope can be accessed from anywhere in the program.
Enclosing scope: A scope that isn’t local or global comes under enclosing scope for example a variable declared in a function accessed from another function nested inside the initial function.
Built-in scope:The widest scope in python. if an identifier isn't found in the other scopes python looks it up in the built-in scope.
#### What’s the difference between const and var in JavaScript?
const declarations are block scoped and cant be updated or re-declared
var declerations are global scoped when not declared inside a function.
var declarations can be updated and re-declared.
#### How the list comprehension looks like in Python?
example:

        comprehension=[x for x in list if x>5] //will contain all elements of list that are greater than 5
#### How the “ternary expression” looks like in Python?
example:

        x = 1 if [condition] else 2
if the condition is true the value of x will be 1, if its false the value of x will be 2
#### How the ternary expression looks like in JavaScript?
        condition ? true:false
#### How to import a function from another module in Python?
        from module import function_name
#### How to import a function from another module in JavaScript?
export the function from the module first:

    export function functionName(){
        pass
    }
    
then import it:

    import {functionName} from 'filePath'

### Functional
#### What is recursion?
the process of a function calling itself
#### Write a recursive function which calculates the Fibonacci numbers!
    n1, n2 = 0, 1
    def fibonacci(n1, n2, count=0, first=True, terms=10):
    if first:
        print(n1)
    print(n2)
    next_num = n1 + n2
    n1 = n2
    n2 = next_num
    count += 1
    if count != terms:
        fibonacci(n1, n2, count, False)
#### How to store a function in a variable in Python?
    variable=function
you can call it like:

    variable()
#### List the ways of defining a callable logical unit in JavaScript!
#### What is an event listener? How to attach one?
an event listener is an object that handles events and executes a function when a specified event occurs
attaching:

    Element.addEventListener()
#### How to trigger an event in JavaScript?
You can trigger an event by doing basically anything on a webpage like clicking, moving the mouse etc.
#### What is a callback function? Tell some examples of its usage.
A function passed to another function which is called after the first function is executed(can be synchronous or asynchronous)
async callbacks use .then()
#### What is a Python decorator? How does it work? Tell some examples of its usage.
a decorator is a function that takes another function as an argument and returns yet another function
#### What is the difference between synchronous and asynchronous execution?
synchronous execution is when all code is executed line by line.
asynchrounous execution means that some parts of the code can run in parallel with other parts of the code.
## Programming languages

### SQL

#### How can you connect your application to a database server? What are the possible ways?
in the case of a Flask project you can connect to a database with psycopg2's connect() function
#### When do you use the DISTINCT keyword in SQL?
You use the DISTINCT keyword when you don't want to retrieve duplicate values from a column
#### Talk about the behavior/goal of these base SQL clauses: WHERE, GROUP BY, HAVING, ORDER BY?
WHERE is used to filter results,data is only retrieved if the condition in the WHERE clause is true
GROUP BY is used to arrange identical data into groups
HAVING works like the WHERE clause but it's used for aggregate functions
ORDER BY is uesd to order the results of a query by a column(ascending or descending)
#### What are aggregate functions in SQL? Give 3 examples.
aggregate functions perform calculations on a set of values and return a single value
examples:

    AVG() --returns the average of values
    SUM() --returns the sum of values
    COUNT() --counts the number of values
#### What kind of JOIN types do you know in SQL? Could you give examples?
INNER JOIN Returns records that have matching values in both tables
LEFT JOIN Returns all records from the table on the left side of the equation, and the matched records from the right table
RIGHT JOIN Returns all records from the table on the right side of the equation, and the matched records from the left table
FULL JOIN returns all records when there's a match in either table
#### What are the constraints in sql?
SQL constraints are used to specify rules for the data in a table
Constraints are used to limit the type of data that can go into a table
Constraints can be applied to columns or whole tables
#### What is a cursor in SQL? Why would you use one?
A cursor is an object that can retrieve data from a result set one row at a time
#### What are database indexes? When to use?
an index is a pointer to data in a table
Similiar to indexes in actual libraries
#### What are database transactions? When to use?
Transactions should be used when you want your operations to either fully execute or fully fail so it can't be "half complete".
#### What kind of database relations do you know? How to define them?
there are 3 types of database relations
one-to-one:a record in table1 relates to one record in table2
one-to-many: a record in table1 relates to more than one records in table2
many-to-many: more than one record in table1 relates to table2 records, and more than one record in table2 is related to more than one record in table1(for example: at a company each project can involve more than one employee and each employee can be working on more than one project )

#### You have a table with an “address” field which contains data like “3525, Miskolc, Régiposta 9.” (postcode, city, street name and address). How would you query all records related to Miskolc?
    SELECT *
    FROM TABLE 
    WHERE address like '%Miskolc%';
#### How would you keep track of what kind of data has changed after an UPDATE or DELETE operation in a table?
You can return the record that were changed using the RETURNING clause
### HTML & CSS

#### What’s the difference between XML, XHTML and HTML?
HTML is an SGML based markup language while XHTML is an XML based markup language
html is case insensitive,XHTML can be case sensitive
XHTML is more strict
XHTML requires that there be an end tag to every start tag and all nested tags must be closed in the right order.
#### How to include a JavaScript file in a webpage?
by adding a script tag to the html file.

    <script src="file_path/filename.js"></script>
#### How to include a CSS file in a webpage?
by adding a link tag to the html file

    <link rel="stylesheet" type="text/css" href="file_path/filename.css">
#### How to select an element using its id in CSS?
    #id{}
#### How to select elements using their class in CSS?
    .class{}
#### How to select elements which have the ‘alpha’ and ‘beta’ classes in CSS?
    .alpha.beta{}
#### How to select all list items in all ordered lists on the page in CSS?
    ol li {}
#### How to select elements using their attributes in CSS?
    [attribute]{}
#### What are UX and UI?
UX stands for User eXperience it describes how a person feels while interacting with an application
UI stands for User Interface it's anything the user can interact with while using the application
#### Please list some points that an application should fulfill to have good UX.
Ease of use
Being useful to the user,meeting the user's needs
Easy to navigate
consistency
Have safeguards like confirmation dialogs when doing meaningful tasks(deleting data,spending money etc.)
#### What is XML, XSLT, DTD?
XML is a markup language like html but without pre defined tags, instead you can define your own tags.
XSLT is used to transform XML documents into XHTML documents, or into other XML documents
DTD (Document Type Definition): A DTD defines the structure and the legal elements and attributes of an XML document
#### What is the difference between HTML and XML?
HTML displays data and describes the structure of a webpage, XML stores and transfers data.
HTML has pre defined tags while xml does'nt
html is case insensitive while xml is case sensitive
### Javascript

#### What is javascript?
A scripting language for implementing complex features on a web page
javascript is an implementation of the ECMAScript specification
#### When to use AJAX? Bring examples of its usage.
Any time we want to asynchronously download data in the background we should use AJAX
#### What is DOM and how to manipulate it from Javascript?
DOM is the document object model, the model of elements on a webpage.
it can be manipulated with javascript by changin element attributes or removing/adding elements
#### What are events and how/why to use them in Javascript?
events that occur when the user or the browser manipulates a page.
events can be used to make a web page interactive(making it react to specific events)
#### What is event bubbling/capturing? How would you use it?
Event bubbling and capturing are two ways of event propagation in the DOM, when an event occurs in an element inside another element, and both elements have handles for that event.
With bubbling, the event is first captured and handled by the innermost element and then propagated to outer elements.
With capturing, the event is first captured by the outermost element and propagated to the inner elements.

#### What is JSON and how do we use it?
JavaScript Object Notation is a data interchange format
it's commonly used to transmit data objects that consist of key:value pairs.

## Software engineering

### Version control

#### What type of branching strategy would you use?
 I prefer to use feature branching
#### What would you do if you find a bug on the production code (master branch)?
create a fix branch from master, fix the bug and create a pull request
#### How can you move changes from one branch to another in GIT?
if the changes are not commited you can stash them, checkout the other branch and then pop the stashed changes
if the changes are commited then create a new branch, then checkout the first branch and reset the commited changes with git reset --hard head^n (n being the number of commits to reset)
#### How does a VCS help with code reviews?
a vcs helps you identify who wrote the code you're reviewing and what the changes are exactly
#### What is your favorite git command? Why?
combination of:
git stash
git checkout -b
git stash apply
because I have a bad habit of starting work on the master branch
#### What does remote/local mean in Git? 
it indicates wether a branch is on your machine(local) or on a remote server

### DevOps

#### Why is it good to use a package manager software?
because it makes it easy to install and manage packages
#### Why is it good to use a virtual environment for a project?
because you can organize your packages much better and know exactly the packages you need to run your code incase someone else needs to run it on their machine

### Networks

#### What kind of HTTP status codes do you know?
200-okay
404-not found
500-internal server error
302-found(redirection)
405-method not allowed
#### What is a API?
application programming interface
it's a set of functions that allows applications to access data and interact with external services.
#### What is REST API?
a REST API is an API that conforms to the REST(REpresentational State Transefer) architectural style.
#### What is JSON? When to use?
avaScript Object Notation is a data interchange format
it's commonly used to transmit data objects that consist of key:value pairs.
#### What is TCP/IP? What layers does it define, what are they responsible for?
TCP/IP refers to the internet protocol suite. A set of protocols used on the internet and similiar networks.
The TCP/IP model consists of 4 layers:
link layer:Responsible for handling the physical side of the connection(network cables,wireless network,network interfaces etc.)
internet layer:Responsible for the flow and routing of network traffic.
transport layer: provides a reliable data connection between communicating devices
and the application layer: allows the user to access and interface with the network(email,messagging apps,browsers etc.)
#### What’s the difference between TCP and UDP?
TCP is connection oriented while UDP is a connectionless protocol
TCP is slower but more reliable because it acknowledges any packets sent with an ACK packet and also requires setting up a stable connection using a TCP 3way handshake before data can be sent.
TCP also uses error checking with a crc32 checksum and re-send any corrupted data.
UDP doesn't require any of those reliability measures. It simply sends the data continously, making it much faster.
#### How does an HTTP Request look like? What are the most relevant HTTP header fields?
An HTTP request consists of 
    A Request-line
    Header fields
    An empty line indicating the end of the header fields
    and sometimes a message-body

the most relevant headers are:
Method 
Host
Path 
HTTP version 
Headers (optional) 
Query String (optional)
Body (optional)
#### How does an HTTP Response look like? What are the most relevant HTTP header fields?
An HTTP response contains:

A status line.
A series of HTTP headers, or header fields.
A message body, which is usually needed.

#### What is DNS? How does it work?
DNS is a naming system used to identify computers through the internet.
DNS records store a computers public IP associated with it's domain name.
When a user tries to acces a server using a URL a request is sent to the dns server with the domain name.
The server resolves the domain name and returns the IP address associated with the domain name so the user's computer can connect to the server.
#### What is a web server?
A web server is a computer that stores web server software and the components of a website(html,css,js etc. files)
#### Explain the client-server architecture.
the client-server architecture is a centralized architechure.
In a client-server architecture the central server hosts, delivers and manages most of the resources and services to be consumed by the client.
#### What would you use a session for?
sessions are used to store data for individual users against a unique ID. This can be used to store data between page requests
#### What would you use a cookie for?
to identify users as they navigate through different pages of a website,and to identify returning users.

## Software Development Methodologies

#### What kind of software development methodologies do you know? What are the main features of these?
Waterfall method:The waterfall method is a rigid linear model that consists of sequential phases, each phase must be complete before the other phase starts
Agile development: 
Only work on the most important tasks at any given point in time
Break tasks into small tasks for individuals to work on
Catch up for about 10-20 minutes every morning on progress
#### What are the SCRUM roles?
There are 3 roles in scrum: 
Product Owner
Development Team
Scrum Master
#### What are the SCRUM ceremonies?
there are 5 scrum ceremonies or events
    Sprint Planning.
    Daily Scrum.
    The Sprint.
    Sprint Review.
    Sprint Retrospective.
    
#### What are the SCRUM artifacts?
the main scrum artifacts are 
product backlog(what to do), 
sprint backlog(what to do in the current sprint), 
product increment(what got added to the product)
#### What is the main goal of a retrospective meeting?
 For the team members to discuss among themselves about how the work went during the last sprint so that better ways can be found to meet the project's goals
#### Explain, when would you recommend to use the waterfall methodology?
Waterfall should be used when:
The project has strict  requirements
Requirements and project scope are known and won't change
Budget and timelines are fixed
