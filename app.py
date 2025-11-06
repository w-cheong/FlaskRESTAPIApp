from flask import Flask, jsonify, request
import csv
# from flask_restful import Resource, Api, reqparse
# from flask_sqlalchemy import pagination
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

    # TODO: error handling, for invalid page numbers
    start_index = per_page * (page - 1)
    end_index = per_page * (page)
    results = df.iloc[start_index:end_index]
    print(results)

    # convert dataframe into list of dictionaries for jsonifying
    return jsonify(results.to_dict(orient='records'))

# searching by first/last name
@app.route('/characters/search', methods=["GET"])
def search_items():
    first_names = request.args.get('first_name') # query parameter setup
    last_names = request.args.get('last_name')

    #check if first or last name is being searched
    if first_names:
        search_results = df[df['first_name'] == first_names]
        return jsonify(search_results.to_dict(orient='records'))
    elif last_names:
        search_results = df[df['last_name'] == last_names]
        return jsonify(search_results.to_dict(orient='records'))
    else: #error handling if not searching for name properly
        return jsonify({"message": "names cannot be found."}), 404

# TODO: update character by id
@app.route('/characters/<int:id>', methods=["PUT"])
def update_character(id):
    character_data = request.get_json()
    if id: #check if id is found in the csv
        df.loc[id] = character_data #access rows for changing
        df.to_csv(FILE_PATH, quoting=csv.QUOTE_ALL)
        return jsonify(character_data)
    return jsonify({"message": "character cannot be found."}), 404

@app.route('/characters/<int:id>', methods=["DELETE"])
def delete_character(id):
    # TODO:
    return jsonify()

if __name__ == '__main__':
    app.run(debug=True)