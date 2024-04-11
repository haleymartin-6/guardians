from flask import Blueprint, request, jsonify, make_response
import json
from src import db

discount = Blueprint('discount', __name__)

@discount.route('/discount/<referralCode>', methods=['GET'])
def get_discount(referralCode):
        # Get the database connection
        cursor = db.get_db().cursor()

        # Retrieve discounts associated with the referral code
        cursor.execute('SELECT * FROM discounts WHERE referralCode = %s', (referralCode,))
        row_headers = [x[0] for x in cursor.description]
        json_data = []

        theData = cursor.fetchall()
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        the_response = make_response(jsonify(json_data))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response
