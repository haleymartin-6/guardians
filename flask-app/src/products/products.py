from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


products = Blueprint('products', __name__)

@products.route('/products', methods=['GET'])
def get_products():
        # Get the database connection
        cursor = db.get_db().cursor()

        # Retrieve discounts associated with the referral code
        cursor.execute('select * FROM products')
        row_headers = [x[0] for x in cursor.description]
        json_data = []

        theData = cursor.fetchall()
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        the_response = make_response(jsonify(json_data))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response

@products.route('/products', methods=['POST'])
def post_product():
        # Get the database connection
        product_info = request.json

        name = product_info['name']
        cost = product_info['cost']
        tutorial = product_info['tutorial']
        productType = product_info['productType']
        brandID = product_info['brandID']

        query = 'INSERT INTO products (brandID, name, cost, tutorial, productType) VALUES (%s, %s, %s, %s, %s)'
        cursor = db.get_db().cursor()
        cursor.execute(query, (brandID, name, cost, tutorial, productType))
        db.get_db().commit()
        return 'new product added!'

@products.route('/products/<productID>', methods=['GET'])
def get_one_product_info(productID):
        # Get the database connection
        cursor = db.get_db().cursor()

        query = 'SELECT * FROM products WHERE productID = %s'
        values = (productID,)
        cursor.execute(query, values)

        row_headers = [x[0] for x in cursor.description]
        json_data = []

        theData = cursor.fetchall()
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        the_response = make_response(jsonify(json_data))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response


@products.route('/products/<productID>', methods=['PUT'])
def put_product(productID):
        # Get the database connection
        product_info = request.json

        name = product_info['name']
        cost = product_info['cost']
        tutorial = product_info['tutorial']
        productType = product_info['productType']
        brandID = product_info['brandID']

        cursor = db.get_db().cursor()

        query = 'UPDATE products SET brandID = %s, name = %s, cost = %s, tutorial = %s, productType = %s WHERE productID = %s'
        values = (brandID, name, cost, tutorial, productType, productID)
        cursor.execute(query, values)
        db.get_db().commit()
        return 'new product updated!'

@products.route('/products/<productID>', methods=['DELETE'])
def delete_product(productID):
       query = 'DELETE FROM products WHERE productID = %s'
       values = (productID,)

       cursor = db.get_db().cursor()
       cursor.execute(query, values)
       db.get_db().commit()
       return 'Product deleted successfully!'

@products.route('/tutorial-products/<productID>', methods=['PUT'])
def update_product_tutorial(productID):
        # Get the tutorial information from the request JSON data
        tutorial_info = request.json

        # Extract the tutorial text from the JSON data
        tutorial_text = tutorial_info.get('tutorial')

        # Update the product in the database with the new tutorial
        cursor = db.get_db().cursor()

        query = 'UPDATE products SET tutorial = %s WHERE productID = %s'
        values = (tutorial_text, productID)
        cursor.execute(query, values)

        db.get_db().commit()
        return 'Product tutorial updated successfully!'