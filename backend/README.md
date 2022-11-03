# backend

## design concept
Minimize dependencies
Do not combine them into one, make them separate in detail.
Define separate functions for similar processes instead of combining them into one.
It's faster to fix multiple places than many dependencies.
For example, create a separate email sending function for each status, don't combine them into one
The pydantic and dataclass schemas should also be separated into smaller pieces. Avoid using them across multiple directories.

## reference rule
routers > services > datasources or routers > datasources

## about Directories
### routers
> Build the endpoints.
### services
> Build processing and logic.
### datasources
> Retrieving, saving, and mapping data

## reference type rule
```
All function responses are type-defined.
For dictionary types, always define the type in pydantic or dataclass.
router is defined in pydantic.
service is defined in pydantic.
datasource is defined by dataclass.
```

### alembic command
create migration file
```
$ alembic revision --autogenerate -m 'message'
```
execute migration
```
$ alembic upgrade head
```
```
$ alembic upgrade +1
```
rollback migration
```
$ alembic downgrade base
```
```
$ alembic downgrade -1
```
