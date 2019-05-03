# SpeedRunner API
A RESTful API to store and query speedrun times.\
Written in Python 3.6 utilizing Flask microframework and SQLAlchemy with a MySQL database backend.

## Setting up Development Environment
In order to facilitate a cross-platform development environment, Vagrant (v2.2.4) and Virtualbox (v6.0.6) are used *.\
Please download and install both.

**Vagrant:** https://www.vagrantup.com/downloads.html \
**VirtualBox:** https://www.virtualbox.org/wiki/Downloads


A *Vagrantfile* is provided.\
To provision a locally hosted virtualized machine and host the application, type the following terminal command in the application's root directory:
```
$ vagrant up
```
The application should be hosted with all system and application requirements automatically configured at http://localhost:8080/


\* In order to use virtualization, you may need enable virtualization in your system's BIOS depending on your hardware (Intel VT / AMD-V). Many vendors disable this setting by default. Moreover, if you have Hyper-V enabled for Windows you might need to disable it. You can read more here: https://www.vagrantup.com/docs/installation/

When you are ready to tear down the application
```
vagrant destroy
```
If you need to SSH into the virtual machine for any intermediatry provisioning
```
vagrant ssh
```
All applications files are located at synced folder: /vagrant

## Using the API
Replace %s with a *URL encoded string*.\
If you're not familiar with URL encodings, reference this [guide](https://www.w3schools.com/tags/ref_urlencode.asp)

**GET**
* List all games in database: http://locahost:8080/speedrunner/all-games
* List all games in a specific category: http://localhost:8080/speedrunner/all-games/category/%s \
*Examples*
    * http://localhost:8080/speedrunner/all-games/Any%25
    * http://localhost:8080/speedrunner/all-games/Any%25%20History%20Books
* List top 10 speedruns of a specific game: http://localhost:8080/speedrunner/top/speedruns/game/%s \
*Examples*
    * http://localhost:8080/speedrunner/top/speedruns/game/Dark%20Souls
* List all speedruns of a specific player: http://localhost:8080/speedrunner/all/speedruns/player/%s \
*Examples*
    * http://localhost:8080/speedrunner/top/speedruns/player/Madeline
    * http://localhost:8080/speedrunner/top/speedruns/player/Mr.%20X
* List top players in a specific category: http://localhost:8080/speedrunner/top/players/category/%s \
*Examples*
    * http://localhost:8080/speedrunner/top/players/category/Any%
    * http://localhost:8080/speedrunner/top/players/category/1xx%

**POST**\
Post requests are requested via JSON payloads.\
You can do this programatically or with the help of REST clients such as [Postman](https://www.getpostman.com/). The HTTP header must contain a Content-Type of **application/json**. All examples below are written in Python 3.6.

Add a game to the database
```python
import requests
import json

url = 'http://localhost:8080/speedrunner/add-game'
payload = {'game': 'Final Fantasy VII'}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.text)
```

Add a category to a game
```python
import requests
import json

url = 'http://localhost:8080/speedrunner/add-category'
payload = {'game': 'Final Fantasy VII', 'category': 'All Bosses'}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.text)
```

Add a speedrun to the database
```python
import requests
import json

url = 'http://localhost:8080/speedrunner/add-speedrun'
payload = {'game': 'Final Fantasy VII', 'player': 'silentz', 'duration': '7:07:07'}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.text)
```