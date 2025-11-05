from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import pagination
import pandas as pd

app = Flask(__name__)

FILE_PATH = 'friends_data.csv'
df = pd.read_csv(FILE_PATH, index_col=0)

# home page 
@app.route('/', methods=["GET"])
def home_page():
    return jsonify("Page here")

# pagination
@app.route('/characters', methods=["GET"])
def list_all_characters():
    print(request.args)

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per-page", 10, type=int)

    # todo error handling, for invalid page numbers

    start_index = per_page * (page - 1)
    end_index = per_page * (page)
    results = df.iloc[start_index:end_index]
    print(results)

    # convert dataframe into list of dictionaries for jsoinifying
    return jsonify(results.to_dict(orient='records'))

# TODO searching by first/last name
@app.route('/characters/search', methods=["GET"])
def search_items():
    query_string = request.query_string
    return f'Query String: {query_string}'

# TODO update character by id
@app.route('/characters/<int:id>', methods=["PUT"])
def update_character(id):
    # TODO
    return jsonify()

@app.route('/characters/<int:id>', methods=["DELETE"])
def delete_character(id):
    # TODO
    return jsonify()

if __name__ == '__main__':
    app.run(debug=True)