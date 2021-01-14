# QueryPlus

[![](https://img.shields.io/badge/Made_with-Django-green?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![](https://img.shields.io/badge/IDE-Visual_Studio_Code-red?style=for-the-badge&logo=visual-studio-code)](https://code.visualstudio.com/  "Visual Studio Code")

QueryPlus is a Q&amp;A platform specially made for developers where they can post questions and answers.

## Getting Started

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/gocardless/sample-django-app.git
$ cd sample-django-app
```

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r https://raw.githubusercontent.com/juanifioren/django-project-template/master/requirements.txt

# You may want to change the name `projectname`.
$ django-admin startproject --template https://github.com/juanifioren/django-project-template/archive/master.zip projectname

$ cd projectname/
$ cp settings_custom.py.edit settings_custom.py
$ python manage.py migrate
$ python manage.py runserver
```

## Tech Stack 

* Frontend: HTML, CSS, JS, Bootstrap4
* Backend: Python3
* Framework: Django
* Database: sqlite

## Features

* QueryPlus is Q&A platform where users can post questions and answers.
* Users can also upvote or downvote a particular question or answer.
* Users can register and create/update their profile.
* There is CKEditor plugin integration, so if you write some code in your question/answer
it will be posted with proper syntax highlighting for that language.

---

## QueryPlus Screenshots

<div align="center">
<h4 align="center">Homepage</h4>
<img src="./snapshots/1.JPG" width=900px/>
<br>
<img src="./snapshots/2.JPG" width=900px/>
<br>
<h4 align="center">Sign In Page</h4>
<img src="./snapshots/3.JPG" width=900px/>
<br>
<h4 align="center">Questions Page</h4>
<img src="./snapshots/4.JPG" width=900px/>
<br>
<h4 align="center">Question Detail Page</h4>
<img src="./snapshots/5.JPG" width=900px/>
<br>
<h4 align="center">Answer Detail</h4>
<img src="./snapshots/6.JPG" width=900px/>
<br>
<h4 align="center">Ask Question</h4>
<img src="./snapshots/7.JPG" width=900px/>
<br>
</div>

---

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.
