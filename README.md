# DRF ElasticSearch

## Example

### Download project

```shell
git clone https://github.com/bultakov/DRF-ElasticSearch.git
```

```shell
cd DRF-ElasticSearch
```

```shell
python manage.py shell
```

```python3
from product.documents import ProductDocument

products = ProductDocument.search().query('match', name='mahsulot')
for product in products:
    print(f"Name: {product.name}, Type: {product.product_type}")
```

- http://127.0.0.1:8000/search/product/mahsulot/