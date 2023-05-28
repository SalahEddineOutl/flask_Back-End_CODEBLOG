import json
from flask import Flask, render_template, make_response,request,jsonify
import spacy
import requests
import pandas as pd
from datetime import datetime, timedelta
import os
from flask_cors import CORS
import csv
import ast



app = Flask(__name__, static_url_path='/static')


CORS(app)
# @app.route('/data', methods=['GET', 'POST'])
# def get_filtered_data():
#     # Récupérer les tags depuis les paramètres de requête
#     tags = request.args.getlist('tags')

#     # Lire le fichier CSV et filtrer les lignes correspondantes aux tags spécifiés
#     filtered_rows = []
#     with open('data_test.csv', 'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             row_tags = ast.literal_eval(row['tags'])
#             if all(tag.lower() in [t.lower() for t in row_tags] for tag in tags):
#                 filtered_rows.append(row)

#     # Renvoyer les lignes filtrées sous forme de JSON
#     return json.dumps(filtered_rows)

data = []

def read_data_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

read_data_from_csv('data_test.csv')

@app.route('/data', methods=['GET', 'POST'])
def filter_data():
    selected_tags = request.json['tags']
    filtered_data = [row for row in data if any(tag in row['tags'] for tag in selected_tags)]
    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run()