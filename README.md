# Macmenu   
API for macdonalds products written on DRF with Beautifulsoup and Selenium

### Installing using GitHub
Python3 must be already installed. Install PostgresSQL and create db.


```shell
git clone https://github.com/asdadaversa/macmenu.git
cd macmenu
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

### If you want to use empty base run migrations and run server

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```


## Use the following command to load prepared data from fixture:

`python manage.py loaddata product_parsing_data.json`

- After loading data from fixture you can use following superuser (or create another one by yourself):
  - email: `admin@example.com`
  - Password: `1111`

## API Endpoints
- **List Products**: `GET /api/products/`
- **Get Detail Product data**: `GET /api/products/bigmak(r)/`
- **Get Detail Product data with fields**: `GET /api/products/bigmak(r)/fats/`

## Features
- Parsing all menu links (products/parse_all_menu_links.py)
- Parsing and creating database instance with data (products/parse_product.py)
- Get all products
- Get detail products
- get data for each product field


