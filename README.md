# Part 1 

## Criando django project

    $ mkdir djangotutorial

    $ django-admin startproject mysite djangotutorial

> não nomear nada como "django" ou "test"


## Criando um APP

    python manage.py startapp polls


### Project x APP 

An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.


# Part 2


## Database setup

Set TIME_ZONE in mysite/settings.py 

Crie um DB para os INSTALLED_APPS (você pode selecionar quais apps vai usar, no caso do tutorial instalei todos), comando:

    $ python manage.py migrate


## Criando e ativando models

Crie o schema do DB em polls/models.py (polls é o app)

Adiciona a classe PollsConfig aos INSTALLED_APPS, ex: "polls.apps.PollsConfig" e aplique as mudanças com **makemigrations**:

    $ python manage.py makemigrations polls

para ver a instrução SQL e verificar problemas no projeto:

    $ python manage.py sqlmigrate polls 0001

    $ poetry run python manage.py check 

Now, run migrate again to create those model tables in your database:

    $ python manage.py migrate


## Playing with the API

    $ python manage.py shell

> Ex: https://docs.djangoproject.com/en/5.2/intro/tutorial02/#playing-with-the-api


## Introducing the Django Admin

### Creating an admin user

    $ python manage.py createsuperuser

    $ python manage.py runserver


# part 3 - cápitulo prático: básico sobre views (urls.py e view.py)


# part 4


## criando formulário de votos (details.html, results.html e view.py)

    - forloop.counter
    - |pluralize

    - F()
    - HttpResponseRedirect
    - get_object_or_404
    - reverse


## Use generic views: Less code is better

> veja os comentarios dos arquivos urls.py e views.py


# part 5 - tests

## create test inside tests.py in your app. In this case polls/tests.py

    $ python manage.py test polls

## The django test client

    $ python manage.py shell

    >>> from django.test.utils import setup_test_environment
    >>> setup_test_environment()
    >>> from django.test import Client
    >>> client = Client()
    >>> from django.urls import reverse
    >>> response = client.get(reverse("polls:index"))
    >>> response.status_code
    >>> response.content
    >>> response.context

> Para testar a renderização do HTML pode usar LiveServerTestCase com Selenium
> Fácil integração com coverage

# part 6 - static files

# part 7 - customizing admin

create "templates" dir dentro da pasta do projeto "djangotutorial"

Where are the Django source files? 

    $ python -c "import django; print(django.__path__)"

pegue o arquivo do  Django e adicione no template. e edite do seu jeito :D

# part 8 - debug

    $ python -m pip install django-debug-toolbar

Não é uma ferramenta nativa do django. Para integrá-la ao framework siga o passo a passo da doc: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html


# Dicas extras

## Criando diagrama com models

Download graphviz: https://graphviz.org/download/

    $ python -m pip install django-extensions
    $ python -m pip install pyparsing pydot
    $ python manage.py graph_models -a --exclude-models User,Group,Permission,LogEntry,ContentType,Session -o my_project_erd.png

Excluíndo modelos do Django:

    $ python manage.py graph_models -a --exclude-models User,Group,Permission,LogEntry,ContentType,Session,AbstractBaseSession,AbstractUser -o my_project_erd.png

![img_erd_django_tutorial](djangotutorial/my_project_erd.png)