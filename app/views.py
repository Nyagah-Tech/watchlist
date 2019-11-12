from flask import render_template
from app import app

#views
@app.route('/')
def index ():
    title = 'home - Welcome to the best movie review website online'
    
    return render_template('index.html',title = title)
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    view root page function that returns the index page and it data
    '''
    message = 'hello world'
    return render_template('movie.html',id=movie_id)
    