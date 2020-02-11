Project name: Test task. Creating news site with allauth, Celery, RabbitMQ

## Installation

##### Install python packages

```
pip install -r requirements.txt
```

Create groups for permitions

```
python manage.py create_groups
```

Run Django localhost

```
python manage.py runserver
```

##### Run Celery

```
celery -A news worker -l info
```

##### Run RabbitMQ
```
systemctl enable rabbitmq-server
```
```
systemctl start rabbitmq-server
```
## Run tests
```
python manage.py test board.tests
```

