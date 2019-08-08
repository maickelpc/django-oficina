#django-oficina

#Pré requisitos
Python3.6 ou superior: Disponível em https://www.python.org/

#Desejavéis
Pycharm: Disponível em: https://www.jetbrains.com/pycharm/download/

#Ambiente
O Django pode ser global, mas é recomendável um ambiente virtual.<br><br>

Se utilizar o Pycharm, o mesmo já cria um ambiente virtual e ativa para desenvolvimento, caso não possua a ferramenta utilize os comandos abaixo:<br>
Dentro da pasta onde deseja executar o seu projeto:
<ul>
  <li>virtualenv venv --python=python3</li>
  <li>source venv/bin/activate</li>
</ul>
Fazendo isso, vai perceber que no seu console, aparece entre parenteses o ambiente virtual:<br>


#Comandos utilizados
Com o ambiente virtual ativado, instalamos os requisitos deste projeto com os comandos:
<ul>
  <li>pip install django</li>
  <li>pip install django-suit</li>
</ul>

#Pycharm
Ao abrir o projeto no pycharm, ele já ativa o ambiente, e você pode verificar no Terminal, se está o nome do ambiente entre parenteses.


#O Projeto
Baixe o projeto, e abra o mesmo com o pycharm, em seguida, crie um ambiente virtual utilizando o comando virtualenv, ou, no pycharm acessando Menu File->Settings->Project:<<nomedoprojeto>> -> Project Interpreter. nesta tela, no canto superior direito, em opções (icone de engrenagem) clique em ADD, ele vai sugerir o endereco, e certifique-se de estar selecionado uma versão igual ou superior a 3.6 do python em "Base interpreter".<br>
Com isso, já pode acessar o terminal e ativar o ambiente, isntalar os requisitos e prosseguir.


#Executando o projeto
Com a (venv) ativada e os requisitos (django e django-suit) instalados, criamos o banco de dados e um novo super usuario, e inicia o servidor:<br>
python manage.py migrate<br>
python manage.py createsuperuser<br>
python manage.py runserver<br><br>



#Comandos Extras
Para usar base de dados postgres:
<ul>
  <li>instale a biblioteca: pip install psycopg2-binary</li>
  <li>Configure a conexão em settings: <p>'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nomedabase',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': '127.0.0.1',
        'PORT': '5432',  # 8000 is default
</p> </li>
</ul>

#Comandos uteis:
django-admin startproject <nome_do_projeto> //Para criar um novo projeto
python manage.py startapp <nome_do_app> // Para criar um novo app
python manage.py createsuperuser // para criar um novo super usuario
python manage.py makemigrations // para criar migracoes para atualizar o banco conforme modelo
python manage.py migrate // para atualizar o banco, conforme as migrations disponiveis
python manage.py runserver // para rodar o projeto

#Cursos e acessos
<ul>
  <li>Documentação do Django: https://www.djangoproject.com/</li>
  <li>Documentação do Django MODELS (usado em models.py): https://docs.djangoproject.com/en/2.2/topics/db/models/</li>
  <li>Documentação do Django ADMIN (usado em admin.py): https://docs.djangoproject.com/en/2.2/ref/contrib/admin/</li>
  <li>Curso de Python básico Gratuito: https://solyd.com.br/treinamentos/python-basico</li>
  <li>Overview para criação de API com django-rest-framework: https://www.youtube.com/watch?v=gFsIGJR5R8I</li>
  <li>Documentação do django-rest-framework https://www.django-rest-framework.org/</li>
</ul>
