# djangology

My way to separate logic layer from infrastructure in django project

![Linter](https://github.com/Miketsukami/djangology/actions/workflows/linting.yml/badge.svg)
![Tests](https://github.com/Miketsukami/djangology/actions/workflows/testing.yml/badge.svg)
![Coverage](http://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Miketsukami/0a80cbf8588e10d9a6b67eeae7bbcbd2/raw/djangology_python-3.10.json)

![It's also a compilation album by Django Reinhardt and Stephane Grappelli](https://imagine-club.com/sites/default/files/styles/product_zoom/public/photos/djangology_reinhardt_django_1_lp_not_now_eu.jpg?itok=lupAw0T5)

## How I see it

* `selectors` is a layer for select db-queries
* `morphers` is a layer for interacting with model instance without db communication
* `services` is a layer for high level business logic

## What's next?

I'll try to implement CQRS pattern for Django
