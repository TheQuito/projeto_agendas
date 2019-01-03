# projeto_agendas_django

## PROCEDIMENTOS PARA INSTALAÇÃO E CONFIGURAÇÃO DO PROJETO

### INSTALAR O PYTHON 3.7 E CONFIGURAR A VARIÁVEL DE AMBINETE


### INSTALAR O VIRTUALENV VIA PIP
`pip install virtualenv` 

### CRIAR UM AMBINETE VIRTUAL
`virtualenv nome_do_ambiente`

### ATIVAR O AMBINETE VIRTUAL(pelo cmd, navegar para dentro do ambiente virtual criado e executar o comando a seguir)
`Scripts\activate`

### CLONAR O PROJETO DENTRO DO AMBINETE VIRTUAL CRIADO (USAR O GIT BASH)
`git clone https://github.com/TheQuito/projeto_agendas.git`

### INSTALAR AS BIBLIOTECAS REQUERIDAS PARA O PROJETO
(de dentro da pasta clonada executar) `pip install -r requirements.txt`


O sistema faz acesso a um banco oracle. A configuração padrão de acesso ao banco assume que existe um banco de
{'NAME': 'XE', 'USER': 'system', 'PASSWORD': '123456', 'HOST': 'localhost'} portanto certifique-se de haver um banco
com essas especificações ou acesse o arquivo de configução - projeto_agendas/agendas_rest_api/utils/connectionOracle.py - e ajuste as configurações para acessar o banco que você deseja. Após verificar essas informações execute as etapas a baixo para por o projeto em execução.


Se tudo tiver ocorrido sem erros, agora estamos prontos para inicir nosso servidor e começar a usar a aplicação.
O comando a seguir vai iniciar o servidor no seu ip público na porta 9191

### INICIANDO O SERVIDOR
`python manage.py runserver 0.0.0.0:9191`

Agora basta acessar ´http://localhost:9191/agendas_rest_api/`
