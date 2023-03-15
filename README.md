## Cоздать и активировать виртуальное окружение:
```python
python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade pip
```


### Установить зависимости из файла requirements.txt:
```python
pip3 install -r requirements.txt
pip3 install opencv-python
pip3 install python-dotenv

pip install Flask-SQLAlchemy
pip install mysqlclient
```

### Record library tu requirements.txt
```python
pip3 freeze > requirements.txt
```
### For check pip
```shell
pip list
```
### If port is busy
```shell
lsof -P -i :5000
kill -9 <PID>
```
### to run Docker separetely 
```shell
docker build -t docker_flask_app_app1 .
docker ps
docker run -d -p 8000:5000 docker_flask_app_app1

docker kill 9701eed5868d
```
### to install nano in terminal docker
```shell
apt update
apt install nano
```

```shell
# python3
Python 3.9.16 (main, Mar 14 2023, 03:45:02) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import app
>>> from app import db
>>> with app.app_context():
>>>    db.create_all()

```
### to run many containers in Docker-compose
```shell
docker-compose up -d

docker-compose ps

docker-compose ls

docker-compose down
```

