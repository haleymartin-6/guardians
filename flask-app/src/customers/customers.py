from flask import Blueprint, request, jsonify, make_response
import json
from src import db


customers = Blueprint('customers', __name__)

# Get all customers from the DB
@customers.route('/customers', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT firstName, lastName, email1, email2, number, promotionScore FROM customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer detail for customer with particular userID
@customers.route('/customers/<int:customerID>', methods=['GET'])
def get_customer_detail(customerID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT firstName, lastName, email1, email2, number, promotionScore FROM customers WHERE userID = %s', (customerID,))
    row_headers = [x[0] for x in cursor.description]
    customer_data = cursor.fetchone()
    if customer_data:
        customer_detail = dict(zip(row_headers, customer_data))
        return jsonify(customer_detail), 200
    else:
        return jsonify({'error': 'Customer not found'}), 404
    
# Retrieve the promotion score 
@customers.route('/promotionScore', methods=['GET'])
def get_promotion_score():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT firstName, lastName, email1, email2, number, promotionScore FROM customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

#Instantiate a new promotion score
@customers.route('/promotionScore', methods=['POST'])
def post_promotion_score():
    promotion_score_info = request.json
    
    first_name = promotion_score_info['firstName']
    last_name = promotion_score_info['lastName']
    email1 = promotion_score_info['email1']
    email2 = promotion_score_info['email2']
    number = promotion_score_info['number']
    promotion_score = promotion_score_info['promotionScore']
    
    query = 'INSERT INTO customers (firstName, lastName, email1, email2, number, promotionScore) VALUES (%s, %s, %s, %s, %s, %s)'
    cursor = db.get_db().cursor()
    cursor.execute(query, (first_name, last_name, email1, email2, number, promotion_score))
    db.get_db().commit()
    
    return 'Promotion score updated!'