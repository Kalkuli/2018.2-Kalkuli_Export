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

    csvwriter.writerow(['CNPJ','ID da Empresa','Data de Emissão','Local','Imposto','Valor', 'Valor total'])

    count = 0

    for emp in receipts:
        if not count:
            csvwriter.writerow([emp['cnpj'],
                            emp['company_id'],
                            emp['emission_date'],
                            emp['emission_place'],
                            emp['tax_value'],
                            emp['total_price'],
                            total_cost])
            count += 1
        else:
            csvwriter.writerow([emp['cnpj'],
                emp['company_id'],
                emp['emission_date'],
                emp['emission_place'],
                emp['id'],
                emp['tax_value'],
                emp['total_price']])

    employ_data.close()

    return send_file('./assets/arquivo.csv', mimetype='text/csv',
                     attachment_filename='arquivo.csv',
                     as_attachment=True), 200