import requests

base_url = "http://localhost/androidAppIpa/productsCRUD/"

def fetch_all_products():
    url = base_url + "getAll.php"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching all products: {e}")
        return None

def fetch_product_by_id(product_id):
    url = base_url + f"getByID.php?id={product_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching product with ID {product_id}: {e}")
        return None

def create_product(product_data):
    url = base_url + "create.php"
    try:
        response = requests.post(url, data=product_data)
        response.raise_for_status()
        
        # Check content type
        content_type = response.headers.get('content-type')
        if 'application/json' in content_type:
            return response.json()
        else:
            return {'message': response.text}  # Handle non-JSON response
        
    except requests.exceptions.RequestException as e:
        print(f"Error creating product: {e}")
        return None


def update_product(product_id, product_data):
    url = base_url + f"edit.php?id={product_id}"
    try:
        response = requests.post(url, data=product_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error updating product with ID {product_id}: {e}")
        return None

def delete_product(product_id):
    url = base_url + "delete.php"
    try:
        response = requests.post(url, data={"id": product_id})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error deleting product with ID {product_id}: {e}")
        return None
