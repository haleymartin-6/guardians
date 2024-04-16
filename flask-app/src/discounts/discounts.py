from flask import Blueprint, request, jsonify, make_response
import json
from src import db

discount = Blueprint('discount', __name__)

@discount.route('/discount', methods=['GET'])
def get_discount():
        # Get the database connection
        cursor = db.get_db().cursor()

        # Retrieve discounts associated with the referral code
        cursor.execute('select amount, addedDate, likes, referralCode, expirationDate, retailerID, brandID from discounts')
        row_headers = [x[0] for x in cursor.description]
        json_data = []

        theData = cursor.fetchall()
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        the_response = make_response(jsonify(json_data))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response

@discount.route('/discount', methods=['POST'])
def post_discount():
        # Get the database connection
        discount_info = request.json

        amount = discount_info['amount']
        addedDate = discount_info['addedDate']
        likes = discount_info['likes']
        referralCode = discount_info['referralCode']
        expirationDate = discount_info['expirationDate']
        retailerID = discount_info['retailerID']
        brandID = discount_info['brandID']

        query = 'INSERT INTO discounts (amount, addedDate, likes, referralCode, expirationDate, retailerID, brandID) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        cursor = db.get_db().cursor()
        cursor.execute(query, (amount, addedDate, likes, referralCode, expirationDate, retailerID, brandID))
        db.get_db().commit()
        return 'new discount added!'

@discount.route('/recent-discount', methods=['GET'])
def get_recent_discounts():
        cursor = db.get_db().cursor()

        # Retrieve recent discounts sorted by addedDate in descending order
        query = 'SELECT * FROM discounts ORDER BY addedDate DESC'
        cursor.execute(query)
        
        row_headers = [x[0] for x in cursor.description]
        json_data = []

        theData = cursor.fetchall()
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        the_response = make_response(jsonify(json_data))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response

@discount.route('/brand-discount/<brandID>', methods=['GET'])
def get_brand_discounts(brandID):
        cursor = db.get_db().cursor()

        # Retrieve recent discounts sorted by addedDate in descending order
        query = 'SELECT * FROM discounts WHERE brandID = %s'
        values = (brandID,)
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

@discount.route('/retailer-discount/<retailerID>', methods=['GET'])
def get_retailer_discounts(retailerID):
        cursor = db.get_db().cursor()

        # Retrieve recent discounts sorted by addedDate in descending order
        query = 'SELECT * FROM discounts WHERE retailerID = %s'
        values = (retailerID,)
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

@discount.route('/discount/<discountID>', methods=['PUT'])
def put_discount(discountID):
        # Get the database connection

        query = 'UPDATE discounts SET likes = true where discountID=%s'
        values = (discountID,)
        cursor = db.get_db().cursor()
        cursor.execute(query, values)
        db.get_db().commit()
        return 'new discount like updated!'

@discount.route('/discount/<discountID>', methods=['DELETE'])
def delete_discount(discountID):
       query = 'DELETE FROM discounts WHERE discountID = %s'
       values = (discountID,)

       cursor = db.get_db().cursor()
       cursor.execute(query, values)
       db.get_db().commit()
       return 'Discount deleted successfully!'

@discount.route('/discount/<discountID>', methods=['GET'])
def get_one_discount_info(discountID):
        # Get the database connection
        cursor = db.get_db().cursor()

        # Retrieve discounts associated with the referral code
        query = 'SELECT * FROM discounts WHERE discountID = %s'
        values = (discountID,)
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
