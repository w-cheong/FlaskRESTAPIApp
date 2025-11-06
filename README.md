FlaskRestAPIApp

This program reads data from a csv using pandas built as a Flask REST API application.

Routes 

* [X] GET `/characters` -- list all characters with pagination
* [X] GET `/characters/search` -- search for a character by first or last name
* [X] PUT `/characters/<id>` -- update a character by id and persist to CSV
* [X] DELETE `/characters/<id>` -- remove a character by id and persist to CSV


Examples:
* `GET /characters?page=1&per_page=10`
* `GET /characters/search?first_name=Phoebe`
* `GET /characters/search?last_name=Geller`
* `PUT /characters/1`
* `DELETE /characters?1`
