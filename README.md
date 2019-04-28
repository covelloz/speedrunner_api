# SpeedRunner API
A RESTful API to store and query speedrun times.\
Written in Python 3.6 utilizing Flask microframework and SQLAlchemy with a MySQL database backend.

## Setting up Development Environment
In order to facilitate a cross-platform development environment, Vagrant and Virtualbox are used *. A **Vagrantfile** is provided. To provision a locally hosted virtualized machine and host the application:
```
$ vagrant up
```
The application should be hosted with all system and application requirements automatically configured. Visit http://localhost:8080/

\* In order to use virtualization, you may need enable virtualization in your system's BIOS depending on your hardware (Intel VT / AMD-V). Many vendors disable this setting by default.