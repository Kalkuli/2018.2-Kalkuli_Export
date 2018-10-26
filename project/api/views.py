import csv
from flask import Flask, jsonify, Blueprint, request, send_file


export_blueprint = Blueprint('export', __name__)

@export_blueprint.route('/export', methods=['POST'])
def exports():
    post_data = request.get_json()

    error_response = {
        'status': 'fail',
        'message': 'wrong json'
    }

    if not post_data:
        return jsonify(error_response), 400

    employ_data = open('./project/assets/arquivo.csv', 'w')
    csvwriter = csv.writer(employ_data)

    receipts = post_data.get('receipts')
    total_cost = post_data.get('total_cost')

    count = 0
    for emp in receipts:
        if count == 0:
            header = emp.keys()
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(emp.values())
    # csvwriter.writerows(total_cost)
    employ_data.close()

    return send_file('./assets/arquivo.csv')