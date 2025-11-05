from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import pagination
import pandas as pd

app = Flask(__name__)

# reading the csv from raw url into dataframe
url = 'https://raw.githubusercontent.com/gchandra10/filestorage/refs/heads/main/friends_data.csv'
# friends_data = 'friends_data.csv'
df = pd.read_csv(url, index_col=0)
page_At = '&_page='
page_Total = '&_per_page='
per_page = 10
page = 1

# home page 
@app.route('/', methods=["GET"])
def home_page():
    return jsonify("Page here")

# pagination
@app.route('/characters', methods=["GET"])

def paginate_data(df, page, page_size=10):
    data_found = []
    
    current_page = request.args.get('characters')

    # for page in range(page_size):
    #     page_url = url + page_At + str(page) + page_Total +     
    #     pages = df.paginate(per_page, page_size).items      
    #     return jsonify(page)

# searching by first/last name
@app.route('/characters/search', methods=["GET"])
def search_items():
    query_string = request.query_string
    return f'Query String: {query_string}'

# update character by id
@app.route('/characters', methods=["PUT"])
def update_character(): 
    return jsonify()

if __name__ == '__main__':
    app.run(debug=True)