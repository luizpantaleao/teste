![imersao](https://user-images.githubusercontent.com/102190998/190873920-672f9dfe-86fb-4af3-ae4b-2da50c735dcd.jpeg)
<h1 align="center">DESAFIO BACK-END - PROJETO AGENDA :notebook:</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green"/>
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
  <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/luizpantaleao/teste?color=GREEN&style=flat-square">
</p>


<h2>Descrição do projeto:pencil2:</h2>
<p align="justify">Esse projeto foi desenvolvido como proposta de resolução ao desafio enviado na workshop de back-end. Ele consiste em uma agenda,
na qual podem ser inseridos, editados e deletados contatos.</p>
<p align="justify">Para inserir um contato é preciso, primeiramente, cadastrar o usuário. Em seguida basta efetuar o login. Uma vez logado o usuário poderá acrescentar novos contatos e modificar ou deletar os já existentes. 
Para sair bastaefetuar o logout, que redicionrá para a pagina inicial.</p>


# Instalação
Para criar o ambiente virtual, no qual ficarão as bibliotecas necessárias para rodar o projeto:
```
python -m venv venv
.\venv\Scripts\activate 
``` 

Para instalar os requisitos do projeto:
```
pip install -r requirements.txt
```

# Login 
Para logar deve criar o superuser:
```
python manage.py createsuperuser
```

# Execução 
```
python manage.py runserver
```

<h2>Estrutura</h2>
<ul>
  <li>:open_file_folder: agenda : é a pasta com as configurações padrões do projeto</li>
	<li>:open_file_folder: contatos: é o app responsável por criar contatos que podem ser acessados por qualquer usuário</li>
	<li>:open_file_folder: accounts: é o app responsável por criar usuários e promover sua interação com o projeto</li>
	<li>:open_file_folder: media: é a pasta na qual são inseridas/armazenadas fotos</li>  
	<li>:open_file_folder: static: pasta que contém arquivos css e javascript</li>
	<li>:open_file_folder: templates: pasta que guarda os arquivos html base e parciais</li>
</ul>