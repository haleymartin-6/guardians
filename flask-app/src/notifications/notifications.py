from flask import Blueprint, request, jsonify, make_response
import json
from src import db

notifications = Blueprint('notifications', __name__)

@notifications.route('/notifications', methods=['GET'])
def get_notifications():
        # Get the database connection
        cursor = db.get_db().cursor()

        # Retrieve discounts associated with the referral code
        cursor.execute('select * from notifications')
        row_headers = [x[0] for x in cursor.description]
        json_data = []

        theData = cursor.fetchall()
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        the_response = make_response(jsonify(json_data))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response

@notifications.route('/notifications', methods=['POST'])
def post_notification():
        # Get the database connection
        noti_info = request.json

        discountID = noti_info['discountID']
        text = noti_info['text']
        status = noti_info['status']
        dateTime = noti_info['dateTime']

        query = 'INSERT INTO notifications (discountID, text, status, dateTime) VALUES (%s, %s, %s, %s)'
        cursor = db.get_db().cursor()
        cursor.execute(query, (discountID, text, status, dateTime))
        db.get_db().commit()
        return 'new notification added!'

@notifications.route('/notifications/<notificationID>', methods=['PUT'])
def put_notification(notificationID):
        # Get the notification information from the request JSON data
        noti_info = request.json

        discountID = noti_info['discountID']
        text = noti_info['text']
        status = noti_info['status']
        dateTime = noti_info['dateTime']

        # Update the notification in the database
        cursor = db.get_db().cursor()

        query = 'UPDATE notifications SET discountID = %s, text = %s, status = %s, dateTime = %s WHERE notificationID = %s'
        values = (discountID, text, status, dateTime, notificationID)
        cursor.execute(query, values)
        db.get_db().commit()
        return 'new notification updated!'

# i didn't test this route bc it deletes everything out of noti table
@notifications.route('/notifications', methods=['DELETE'])
def delete_all_notifications():
        # Get the database connection
        conn = db.get_db()
        cursor = conn.cursor()

        # Delete all notifications
        query = 'DELETE FROM notifications'
        cursor.execute(query)

        # Commit the transaction
        conn.commit()

        return 'sucessfully deleted all notifications!'

@notifications.route('/notifications/<notificationID>', methods=['DELETE'])
def delete_notification(notificationID):
       # Get the database connection
        conn = db.get_db()
        cursor = conn.cursor()

        # Delete the notification with the specified ID
        query = 'DELETE FROM notifications WHERE notificationID = %s'
        values = (notificationID,)
        cursor.execute(query, values)

        # Commit the transaction
        conn.commit()

        return 'notification deleted!'


@notifications.route('/notifications/<notificationID>', methods=['GET'])
def get_one_notification(notificationID):
        # Get the database connection
        cursor = db.get_db().cursor()

        # Retrieve discounts associated with the referral code
        query = 'SELECT * FROM notifications WHERE notificationID = %s'
        values = (notificationID,)
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