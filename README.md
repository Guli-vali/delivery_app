# Delivery app


# Architecture overview

![alt text](https://i.imgur.com/UEesKCx.jpeg)


----

# Stack

* Docker
* Fastapi
* Postgres/Postgis

# Installation

Create `.env` based on `.env.example`

```
Install using `docker-compose`...

    docker-compose up

```

# Documentation(OpenAPI/Swagger)
Documentation available at link http://localhost:8000/docs

# Requests exmples

1) Принимает и сохраняет зоны в виде набора координат, -> возвращает id зоны
```
curl --location --request POST 'http://localhost:8000/api/delivery-zone' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=LzNZm77bnuZN0L3Gt1W0D7vxpadi8yu0iz6NYZ5dfcZZ6M3hg6zkMKUvn68EDMnX' \
--data-raw '{
    "area": [
        {"long": "39.713486869846335", "lat": "47.255296682939225"},
        {"long": "39.72309990695571", "lat": "47.21613410663748"},
        {"long": "39.77871819308852", "lat": "47.2226632126592"},
        {"long": "39.80996056369399", "lat": "47.224295363537884"},
        {"long": "39.838799675022116", "lat": "47.23665144678"},
        {"long": "39.85493584445571", "lat": "47.246207950162464"},
        {"long": "39.85012932590102", "lat": "47.283718032866844"},
        {"long": "39.713486869846335", "lat": "47.255296682939225"}
    ]
}'
```

2) Принимает данные Курьеров с привязкой к зоне доставки, -> возвращает данные курьера
```
curl --location --request POST 'http://localhost:8000/api/courier/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=LzNZm77bnuZN0L3Gt1W0D7vxpadi8yu0iz6NYZ5dfcZZ6M3hg6zkMKUvn68EDMnX' \
--data-raw '{
    "first_name": "Jonh",
    "last_name": "Doe",
    "zone_id": 26
}'
```

3) Принимает координаты места доставки и возвращает данные Курьера и идентификатор зоны доставки
```
curl --location --request POST 'http://localhost:8000/api/delivery/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=LzNZm77bnuZN0L3Gt1W0D7vxpadi8yu0iz6NYZ5dfcZZ6M3hg6zkMKUvn68EDMnX' \
--data-raw '{
    "long": "39.77631493381118", "lat": "47.23525278949814"
}'
```
# Linters

No exceptions for flake8

![alt text](https://i.imgur.com/umcIv6c.png)

9.38 out of 10 for pylint

![alt text](https://i.imgur.com/QsB4SEy.png)

