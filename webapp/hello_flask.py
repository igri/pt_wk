from flask import Flask

from vsearch import search4vowels
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
	return 'Hello world from Flask!'
	
@app.route('/search4')
def do_search() -> str:
	res = search4letters('life, the universe, and everything!','eiru,!')
	return str(res)

app.run()