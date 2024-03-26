# be-challenge-bsantos
## About the Repository
## Architecture & Design
Here, we use a Layered design called Hezagonal Desing.
The advantage of this choice is purely business strtegy:
- We can change the tech stack for some other:
  - Java
  - Javascript
  - Go

- We can change easily the presentation layer in/out bound
- We can detach easily business rules to other external service (microsservice) and access it to a presentation inbound/outbound
  - Although, was already proved that some* microsservices are not so good as a well-done* monolith *(SOME!!!!)


### The Domain-Layered Architecture
![image](https://github.com/CatBia/be-challenge-bsantos/assets/13903840/4f7dd502-c4d9-48c4-87d0-c316b7287d80)

_Color-blind freindly representation of the main layers, main domains and main functions of this project_
#### The Business Rules Layer - The company's core
 Here, we host all the services and entities definition that will serve to apply the business rules to the Outbound and Inbound
#### The Persistence Layer - Database Management
Here, we access the database (it has business rules too, although it's important to separate to 2 layers)
#### The Presentation Layer - Data Translator to network
Here, we include all the In/out bound adapters, that will import data and export a transformed data via business rules.
##### Outbound and Inbound Usage
Outbound - Is where the system's API lives. Data is always out, transformed by some business rules. Here we're gonna use REST and JSON format.
Inbound - Is where the system imports Data from some resource. Here, we're gonna use REST and JSON format.
### REST API - Why so important?
State a contract between two entities is always good, because the communication will be always according wit some pattern. REST is an well known architecture, with defined guidelines to communiate in complex networks.
### Framework
#### FastAPI - Fast and Asynchronous
We're gonna use FastAPI framework. Uses modern python features such as async.
##### Pydantic library and the data object
Pydantic library has some interesting features, like `BaseModel`.
BaseModel is a importnt structure to create data objects and I might say more complete (and heavier) than python's `dataclasses.dataclass`:
- Transform highly nested `dicts` to data objects with the double-star notation
- Serialize vairous type of objects to JSON with a a single class method
  - AND/OR have the seraliztion easily customizable
For data modeling, `BaseModel` showed it's importance at the API and Data services.
### Libraries
#### Pytest - The main test libraty for python
Pytest is our choice of testing framework. Being flexible and extensible, is a key tool to test async functions (with `pytest-async`), parametrize tests to avoid test redundancy, has an advanced test discovery without heavy setup, less verbose that the native `unitest` framework.
You can write the tests only using functions, although in this project we *separate the unit test by standard classes*.

#### Pytest-AsyncIO - Support to test asynchronous entities
We use this extension to have the super ability of async test the async functions
#### MongoDb's pymongo
`pymongo` is offered by MongoDB official support as main library to handle the connection between the python application and the MongoDatabase. The databas can be local or remote. It's easy to set up the connection with the proper URL and PORT.
We configired this connection at the standard _persistence adapter layer_ (layered architecture, again!), to simplyfy a future adapter changes.
## The Error Handling
Each business decision that is not startdand throw an Error. The error is thrown in each leayer and handled at the most "outer" layer to control the final results.
Example:
Something happened to the `presentation.inbound` layer and now `foorball-data`'s API answers our calls with a `429 Reached Rate Limit`. This layer throws a `TeamReachedRateLimit` error that's caught by an higher layer - `business_rules.services` - that will handle it waiting 1 minute and retry the request.
This error hadleing is important to make important business decisions clear each layer.

## Secrets
It's not secure to host secrets on environments. So, at `application/settings/configuration.py`, there's a function called "get_env".
Currently gets an evironment variable. But we can choose any other services, like:
- Hashicorp Secrets Vault
- MS Azure Keyvault
- Google Cloud KMS
Just redefine `get_env` at inbound persistence layer to get the environments.
As Development environment, we have a `dev.env` file, that will be loaded at the `docker-compose` start. Add your custom values there to have your desirable outcome.

Warning: _Some services require a infrastructure configuration, and this can increate implementation time_
## Logging
Right now, we didn't defined the log output. Here, we use Stream as main output, although you can get them via Docker's command:
```
docker logs <CONTAINER_ID>
```
Add `--tail` to get the latest

You can get the container ID in:
```
docker ps
```
Logs are defined at `application/settings`.

We can add:
- Datadog (global)
- Azure Log Insights (azure-hosted applications)
- New Relic (global)
- CloudWatch Log Insight (AWS-hosted applications)
Warning: _Some services require a infrastructure configuration, and this can increate implementation time_

## How to build a development environment
### Install Docker at your machine
Access [Docker's installation page](https://docs.docker.com/engine/install/) and follow the instructions to install Docker in your machine
_Tip: Pay special attention to the "Docker User" step. This configuration is important if you're not your own machine administrator/root and file created inside the machine_
### Install GNU's Make tool
Make is a well-known, older than 70% of the SWE community on this blue rock, amazing tool (i'm biased, i knnow!)._Is a build automation tool that builds executable programs and libraries from source code by reading files called makefiles which specify how to derive the target program._[Wikipedia Make's page](https://en.wikipedia.org/wiki/Make_(software)). 
#### `Make` for Windows
Access [GNUWin32 Make's page](https://gnuwin32.sourceforge.net/packages/make.htm) and follow the instructions
OR
Access [Chocolatey - The Windows Package Manager](https://chocolatey.org/) and follow the instructions to install this tool and [this instrutions](https://community.chocolatey.org/packages/make) to install `Make`. (Developer's First Choice!🥇)
### Execute the build instuctions
At the project's folder. exeecure the following instruction:
```
make build
```
### To open the developer's environment have a bash playground:
At the project's folder. exeecure the following instruction:
```
make devmode
```
### To execute the unit tests:
At the project's folder. execute the following instruction:
```
make test
```
### To execute the API server:
At the project's folder. exeecure the following instruction:
```
make up
```
The API will be served at the following address:
```
0.0.0.0:8003
```
Please read the API Doc section to see all available endpoints
### Additional tools:
#### Mongo Express Tool:
You can see all the data created at the development environment  (be_challenge_bsantos database)and test environments (be_challenge_test database).
Access, with your browser:
```
0.0.0.0:8081
```
With the access pair keys:
- User: `admin`
- Password: `pwd`
(don't call SecOPS!)

# API documentation:
Acces the following endpoint to have the API documentation:
```
http://0.0.0.0:8003/docs
```
We have an OpenAPI auto generated documentation, as FastAPI feature. Although, these are some words regarding the API:

# `/import-league`:
## Request
GET `/import-league`
no params
If success, will take a few minutes to return. We're not downg async import here (we could adding an async job with `async.gather`...)
## Response
### Status Code
200
```
{
    "status": "success",
    "message": "League imported successfully"
}
```

# References:
- [O'Reilly's Software Architecture Fundamentals, Second Edition](https://www.oreilly.com/library/view/software-architecture-fundamentals/9781491998991/video316994.html)
- [Nautilu's top 6 Secret Management Platforms](https://medium.com/@Nautilus_Technologies/top-6-secret-management-platforms-15f72a131130)
- [KraceKumar's Five Reasons To Use Py.Test](https://kracekumar.com/post/five-reason-to-use-pytest/)
- [Docker's documentation](https://docs.docker.com/)
- [O'Reilly's Database fundamentals for Java Programmers](https://www.oreilly.com/library/view/database-fundamentals-for/9781491973448/video287867.html)
- [O'Reily's Using AsyncIO in Python](https://www.oreilly.com/library/view/using-asyncio-in/9781492075325/)
