from flask import flask 
app = flask(__name__)

@app.route('/')
def myapp():
    return 'my name is guri'

if __name__=='__main__':
    app.run( )