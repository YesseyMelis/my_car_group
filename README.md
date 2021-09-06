# MyCarGroup
-----------------------------------

# Run project
-------------
```
docker-compose up --build
```

Docker settings
---------------

Configure docker if needed [settings](https://docs.docker.com/compose/install/)

Create superuser
-----------------
```
docker-compose run django bash
./manage.py createsuperuser
```

Get cars from [mycars.kz](https://mycar.kz/cars)
-------------------------------------------------
```
docker-compose run django bash
./manage.py get_cars
```

Make requests from swagger
---------------------------
