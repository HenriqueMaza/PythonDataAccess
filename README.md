# Python Data Access #

Este projeto tem o objetivo de facilitar o acesso a dados para funções desenvolvidas em Python. Nesta versão ele suporta somente os seguintes bancos de dados: 

- MSSQL
- MongoDB

## Dependêcias ##

- `pymssql` 	: 	lastest
- `json` 		: 	lastest
- `asq` 		: 	lastest
- `pymongo` 	: 	lastest

## Configuração / Execução ##
Para instalar PythonDataAccess no seu projeto basta importar diratamente do git com o comando:

`$ pip install git+https://https://gitlab.com/Robbyson/PythonDataAccess.git`

As dependencias devem ser adicionadas executando o seguinte comando:

`$ ./install_dependences.sh`

## Utilizando o projeto ##

Para utilizar este projeto basta que sua classe de acesso a dados herde das classes base MongoDataAccessBase (para MongoDB) ou SqlDataAccessBase (para MSSQL) conforme exemplo:

- MongoDB

    ```
    from MongoDataAccessBase import *

    class NomeRepositorio(MongoDataAccessBase):
        def __init__(self, connectionString):
            MongoDataAccessBase.__init__(self, connectionString, "NomedaColeção");
        pass;
    ```
- MSSQL

    ```
    from SqlDataAccessBase import *

    class NomeRepositorio(SqlDataAccessBase):
        def __init__(self, connectionString):
            SqlDataAccessBase.__init__(self, ConfiguraçãoDeAcesso);
        pass;
    ```    
    IMPORTANTE: O que é esperado como configuração de acesso são os seguintes dados:
        - Server: Servidor onde o MSSQL está instalado.
        - user: Usuário de acesso ao MSSQL.
        - password: Senha de acesso ao MSSQL.
        - database: Base de dados principal de acesso ao MSSQL.

## Métodos disponíveis ##

Os metodos mais comuns já estão disponíveis para utilização, são eles:

# MongoDB

- getById(id): Busca por ID na coleção.
- insert(doc): Insere o objeto a coleção.
- count(query): Conta os registros baseados nos parâmetros passados.
- list(query): Retorna uma lista de registros baseados nos parâmetros passados.
- listLimited(query, start, end): lista os registros baseados nos parâmetros passados.
- update(doc): Altera o registro na coleção.
- dropAll(): Remove todos os registros da coleção.

# MSSQL

- executeQuery(query): executa instrução SQL no banco de dados.
