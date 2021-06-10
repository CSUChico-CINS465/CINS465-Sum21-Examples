#/bin/bash

pylint --load-plugins pylint_django --disable=missing-docstring --disable=imported-auth-user --disable=django-not-configured ./mysite/mysite
pylint --load-plugins pylint_django --disable=missing-docstring --disable=imported-auth-user --disable=django-not-configured ./mysite/myapp
