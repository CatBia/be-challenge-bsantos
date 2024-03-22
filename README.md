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


### The Layered Architecture
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
We're gonna use FastAPI framework. Uses modern python features such as
### Libraries
#### Pytest - The main test libraty for python
#### Pytest-AsyncIO - Support to test asynchronous entities
#### MongoDb
## The Error Handling
Each
## Secrets
It's not secure to host secrets on environments. So, at `application/settings/configuration.py`, there's a function called "get_env".
Currently gets an evironment variable. But we can choose any other services, like:
- Hashicorp Secrets Vault
- MS Azure Keyvault
- Google Cloud KMS
Just redefine `get_env` at inbound persistence layer to get the environments.
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
## How to build a production environment

# References:
- [O'Reilly's Software Architecture Fundamentals, Second Edition](https://www.oreilly.com/library/view/software-architecture-fundamentals/9781491998991/video316994.html)
- [Nautilu's top 6 Secret Management Platforms](https://medium.com/@Nautilus_Technologies/top-6-secret-management-platforms-15f72a131130)
- [KraceKumar's Five Reasons To Use Py.Test](https://kracekumar.com/post/five-reason-to-use-pytest/)
- [Docker's documentation](https://docs.docker.com/)
- [O'Reilly's Database fundamentals for Java Programmers](https://www.oreilly.com/library/view/database-fundamentals-for/9781491973448/video287867.html)
- [O'Reily's Using AsyncIO in Python](https://www.oreilly.com/library/view/using-asyncio-in/9781492075325/)
