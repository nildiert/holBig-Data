# Tinderton



This service uses the Holberton School's checker-scoped API to create matches based on the others students checkers.


# What does Tinderton do?

  - User introduces valid Holberton School's email, password and api_key. Using this data, our system is able to get data about projects and their tasks' completion, and based on that our system brings a match for the user based in performance on projects. Specifically, our system picks a random project, checks if all the tasks has been completed and if that's the case, it makes available the option of get a random match.   


> Tinderton was created just for the LOLs
> choosing fun upon usefulness,
> but fun projects can contribute to science too.


### Tech

Tinderton makes use of the following components

* [Flask] - Microframework for delivering content
* [Python] - For all the work behind our API
* [HTML] - For setting the main structure of the served content
* [Bootstrap] For organize content in a easy and clean way
* [CSS] - All about styling
* [Javascript] - It handles input from the web page.


### Installation
Tinderton requires the following Python modules:
```certifi==2019.9.11
chardet==3.0.4
Click==7.0
Flask==1.1.1
Flask-Cors==3.0.8
gunicorn==19.4.5
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
pkg-resources==0.0.0
requests==2.22.0
six==1.12.0
urllib3==1.25.6
Werkzeug==0.16.0
```
You need to ```git clone``` this repository and enter into the ```holBig-Data``` directory. After that, you need to set up the API and the web servers:

For the API server you need to run ```python3 -m api.v1.app``` inside the main directory of this project.
For the web server you need to run first the following commands on the shell on two different terminals:
```
export FLASK_APP=main.py
flask run
```

After this, you will be able to connect to the server from your web browser. (If you're using Vagrant or some virtual machine, maybe you need to set it up for forwarded ports)

### Prototype online (Minimum Viable Product) 

You can see it in http://fesusrocuts.tech:5000/

### Authors
[Ryan Hudson](https://github.com/ryanhudson)
[Nildiert Jimenez Jaramillo](https://github.com/nildiert)
[Jessica Sandoval](https://github.com/alexadeveloper)
[Jeniffer Vanegas](https://github.com/jeniffervp)
[Lucia Rodriguez Toloza](https://github.com/luroto)
[Andres Martin Peña](https://github.com/andres-martin)
[Fesus Rocuts](https://github.com/fesusrocuts)
[Nicolas Martínez Machado](https://github.com/noeuclides)       
