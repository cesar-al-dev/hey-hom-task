
# Task: Develop a Property Listing API using Django and Django REST Framework

Note: For your convinience, I included the db.sqlite3 file in the repository, as well as enviroment variables, but they shouldn't be included in a production enviroment.

## Deployment

To run this program locally, you need to run this commands.

```bash
  python3 -m venv venv
  source venv/Scripts/activate
  pip install -r requirements.txt 
  cd hey_hom/
  python3 manage.py runserver
```


## API Reference

The base url of this project is http://127.0.0.1:8000 or localhost:8000

#### Get token

```http
  POST /auth/
```
#### Form-Data

| Key       | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `admin` | **Required**. Your username |
| `password` | `admin` | **Required**. Your password |


#### Get all items

```http
  GET /properties/
```

#### Get single item

```http
  GET /properties/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Add new item

```http
  POST /properties/
```
Example 

```
{
    "title": "Naranja",
    "description": "casa naranja",
    "price": 200.00,
    "location": "CDMX",
    "property_type": "apartment",
    "bedrooms": 1,
    "bathrooms": 1,
    "square_feet": 100,
    "available": true
}
```

#### Update existing item

```http
  PUT /properties/<id>
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to update |
Example 

```
{
    "title": "Azul",
    "description": "Casa Azul",
    "price": 200.00,
    "location": "CDMX",
    "property_type": "apartment",
    "bedrooms": 1,
    "bathrooms": 1,
    "square_feet": 100,
    "available": true
}
```

#### Delete existing item

```http
  DELETE /properties/<id>
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to delete |

Expected response

```
[
    "Item deleted successfully"
]
```