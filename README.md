# sample-APP

## Get Started

1. Copy env file.
```sh
$ cp .env/local/.fast_api.sample .env/local/.fast_api
$ cp .env/local/.mysql.sample .env/local/.mysql
$ cp .devcontainer/devcontainer.env.sample .devcontainer/devcontainer.env
```

2. Run local servers.
```sh
$ docker-compose up
```

## Get Docs
API documents
> http://localhost:8000/redoc

Test call
> http://localhost:8000/docs


## setting vscode
Reopen in container to reflect all settings.(flake8, pylance...)
