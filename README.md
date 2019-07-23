# employees_luizalabs
Challenge sended by luizalabs


#employees_luizalabs
Challenge sended by luizalabs

### Descrição Funcional

    Esse serviço tem como finalidade efetuar o cadastro dos funcionarios que estão contratados pela luizalabs.

### Arquitetura
    .
    ├── employee_luizalabs      #Django Project            
    ├──employee           # Django App
        ├──api            # Serializer e ViewSets
        ├──migrations     # Inicia / Altera o banco
        ├──models         # Modelos do serviço
        └──tests          # Testes de todo o App Employee
    └──requirements    # Todas as bibliotecas utilizadas.

### Executar o Script

    - 1º Passo
        Abra o cmd, indique o caminho que está a pasta do script.
    
    - 2º Passo
        Dentro do cmd, digite os seguites comandos.
        ```bash
            pip install virtualenvwrapper-win
            mkvirtualenv employee_luizalabs
            workon employee_luizalabs
            pip install -r requirements.txt
            python manage.py runserver
        ```
        O script será incializado.

### Tests

    - 1º Passo
        Abra o cmd, indique o caminho que está a pasta do script.

    - 2º Passo
        Dentro do cmd, digite as seguintes mensagens.
        ```bash
            pip install virtualenvwrapper-win
            mkvirtualenv employee_luizalabs
            workon employee_luizalabs
            pip install -r requirements.txt
            python manage.py test employee.tests
        ```