# Accuknox Project

# Installation

```shell script
pip install pipenv
```

* Create virtual environment.

```shell
python -m venv virtualenv
```

* Activate virtual environment.

```shell
Virtualenv/Scripts/activate.bat
```

* Install Packages:
  
```shell
pip install -r requirement.txt
```

* Perform database migrations:

```shell
python manage.py makemigrations
python manage.py migrate
```

* Run your project:

```shell
python manage.py runserver
```
## API Details

* Create user:

  ```url
  POST http://127.0.0.1:8000/api/register/
  {"Email":"user@gmail.com",
    "password": "123456",
    "UserName": "user"}

  ```

* Login user:

  ```url
  POST http://127.0.0.1:8000/api/login/
  {"Email":"user@gmail.com",
    "password": "123456"}
  ```
* Reponse
  
  ```
  {"accesstoken":"abc",
  "refreshtoken":"cbd"}
  ```

* Search User:

  ```url
  GET http://127.0.0.1:8000/api/searchuser/?search=user
  ```
* header:
  
  ```
  {"Authorization":"Bearer <accesstoken>"}
  ```

* Reponse
  
  ```
  {"Email":"user@gmail.com",
    "id": "123456",
    "UserName": "user"}
   ```
