#!/bin/bash

docker-compose run wasm wasm-pack build --target web
cp ./wasm-test/myproject/pkg/myproject* ./mysite/myapp/static/js/
docker-compose run web python manage.py collectstatic --noinput