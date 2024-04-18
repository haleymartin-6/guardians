from flask import Blueprint, request, jsonify, make_response
import json
from src import db

discount = Blueprint('discount', __name__)

@discount.route('/discount', methods=['GET'])
def get_discount():
    # Get the database connection
    cursor = db.get_db().cursor()

    # Define the base SQL query with joins
    sql_query = '''
        SELECT d.discountID, d.amount, d.addedDate, d.likes, d.referralCode, 
                 d.expirationDate, b.name AS brand, pr.name AS product, r.name AS retailer,
                 d.brandID, d.retailerID
        FROM discounts d
        LEFT JOIN brand b ON d.brandID = b.brandID
        LEFT JOIN products pr ON d.brandID = pr.brandID
        LEFT JOIN retailer r ON d.retailerID = r.retailerID
'''


    # Execute the SQL query
    cursor.execute(sql_query)

    # Fetch data and format it as JSON
    row_headers = [x[0] for x in cursor.description]
    json_data = [dict(zip(row_headers, row)) for row in cursor.fetchall()]

    # Create the response
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
        expirationDate = discount_info['expirationDate']
        retailerID = discount_info['retailerID']
        brandID = discount_info['brandID']

        query = 'INSERT INTO discounts (amount, addedDate, likes, expirationDate, retailerID, brandID) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor = db.get_db().cursor()
        cursor.execute(query, (amount, addedDate, likes, expirationDate, retailerID, brandID))
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

@discount.route('/discount', methods=['PUT'])
def put_discount():
        # Get the database connection
        discount_info = request.json

        discountID = discount_info['discountID']
        amount = discount_info['amount']
        addedDate = discount_info['addedDate']
        likes = discount_info['likes']
        expirationDate = discount_info['expirationDate']
        

        query = '''UPDATE discounts 
                SET amount = %s, addedDate = %s, likes = %s, 
                        expirationDate = %s
                WHERE discountID = %s'''
        cursor = db.get_db().cursor()
        cursor.execute(query, (amount, addedDate, likes, expirationDate, discountID))
        db.get_db().commit()
        return 'Discount updated successfully!'

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

@discount.route('/organize-discount/<option>', methods=['GET'])
def get_organize_discount(option):
    # Get the database connection
    cursor = db.get_db().cursor()

    # Retrieve selected option from query parameter or request body
    selected_option = option # Assuming you're passing the selected option via query parameter

    # Define the base SQL query
    base_query = '''
        SELECT d.discountID, d.amount, d.addedDate, d.likes, d.referralCode, 
                 d.expirationDate, b.name AS brand, pr.name AS product, r.name AS retailer,
                 d.retailerID, d.brandID
        FROM discounts d
        LEFT JOIN brand b ON d.brandID = b.brandID
        LEFT JOIN products pr ON d.brandID = pr.brandID
        LEFT JOIN retailer r ON d.retailerID = r.retailerID
'''

    sql_query = ""
    # Modify the SQL query based on the selected option
    if selected_option == 'DATE':
        sql_query = base_query + ' ORDER BY addedDate DESC'
    elif selected_option == 'BRAND':
        sql_query = base_query + ' ORDER BY d.brandID'
    elif selected_option == 'RETAILER':
        sql_query = base_query + ' ORDER BY d.retailerID'

    # Execute the modified SQL query
    cursor.execute(sql_query)

    # Fetch data and format it as JSON
    row_headers = [x[0] for x in cursor.description]
    json_data = [dict(zip(row_headers, row)) for row in cursor.fetchall()]
    

    # Create the response
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@discount.route('/delete-brand-discounts/<brandID>', methods=['DELETE'])
def delete_brand_discounts(brandID):
    query = 'DELETE FROM discounts WHERE brandID = %s'
    values = (brandID,)

    cursor = db.get_db().cursor()
    cursor.execute(query, values)
    db.get_db().commit()
    
    return 'Discounts for brand {} deleted successfully!'.format(brandID)
