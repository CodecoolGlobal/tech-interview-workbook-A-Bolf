# Enterprise module (C# branch)

## ASP.NET Core

### What Is the difference between .NET Core and .NET Standard? How do they relate to “classic” .NET?

.NET Core is the latest .NET implementation. It’s open source and available for multiple OSes.

.NET Standard is the set of fundamental APIs (base class library or BCL) that all .NET implementations must implement. By targeting .NET Standard, you can build libraries that you can share across all your .NET apps, no matter on which .NET implementation or OS they run.

### What is ASP.NET MVC?

ASP.NET MVC 5 is a web framework based on Model-View-Controller (MVC) architecture.

### Can you explain Model, Controller and View in MVC?

Model: Model represents the shape of the data. A class in C# is used to describe a model.(Model represents the data)

View: View in MVC is a user interface. View display model data to the user and also enables them to modify them.(View is the User Interface)

Controller: The controller handles the user request. Typically, the user uses the view and raises an HTTP request, which will be handled by the controller. The controller processes the request and returns the appropriate view as a response.(Controller is the request handler)

### Explain the page lifecycle of MVC.

MVC is actually defined in two life cycles, the application life cycle, and the request life cycle.

The application life cycle, in which the application process starts the running server until the time it stops. and it tagged the two events in the startup file of your application. i.e the application start and end events

This is separate from the request life cycle, which is the sequence of events or stages that executed every time an HTTP request is handled by the application

### What is Razor View Engine?

A view engine translates a server-side template into HTML markup and renders it in the web browser when triggered by a controller's action method.
Razor View Enginge is the default view engine for asp.net mvc and it uses razor syntax to render HTML.

### What you mean by Routing in MVC?

In MVC, routing is a process of mapping the browser request to the controller action and return response back.

### What is Layout in MVC?

The layout view allows you to define a common site template, which can be inherited in multiple views to provide a consistent look and feel for the application

### What ConfigureServices() method does in Startup.cs?

The ConfigureServices method is used for configuring services that are used by your application it is also where you should add configuration option classes that you would like to have available in your application.

### What Configure() method does in Startup.cs?

The Configure method is used to specify how the ASP.NET application will respond to individual HTTP requests.
Each "Use" extension method adds middleware to the request pipeline.

### What is wwwroot folder in ASP.NET Core?

In ASP.NET Core only those files that are in the web root - wwwroot folder can be served over an http request. All other files are blocked and cannot be served by default.

### What’s the usage of [InternalsVisibleTo] attribute? What are pros and cons of it?

the [InternalsVisibleTo] attribute allows you to specify other assemblies that can see all types and members marked “internal”.

## Object Relational Mapping, Entity Framework

### What is an ORM? What are benefits, when to use?

An ORM (Object Relational Mapper) is a piece/layer of software that helps map your code Objects to your database.
the main benefit of using an ORM is saving development time and costs.

### What is Entity Framework? What are the advantages, limitations?

EF's advantages are:
reduced development time and development cost.
It provides auto-generated code.
allows developers to visually design models and mapping of databases.

the main drawbacks of EF are:
Lazy loading
complicated syntax
Slow data access

### What is lazy loading?

Lazy loading means delaying the loading of related data, until you specifically request for it.
Lazy loading is the default for Entity Framework

### What is the difference between code first and DB first approach?

the main difference is that with code first you create the codebase and data models then let EF set up the database automatically.
With the DB first approach you design your database first and let EF create model codes (classes, properties, DbContext etc.) from the database in the project.

### What is a migration script?

A migration script is used to migrate between different versions of your database.

### What is a navigation property?

a navigation property is a property defined on the principal and/or dependent entity that references the related entity.

### Name 3 different attributes used in EF Core, what can they do for you?

[Key] Identifies one or more properties as a Key
[DatabaseGenerated] Specifies how the database generates values for a property.
[NotMapped] Applied to properties or classes that are to be excluded from database mapping.
