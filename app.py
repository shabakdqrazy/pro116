# importing modules from flask library
from flask import Flask , render_template


app = Flask(__name__)

# Decorator function for the /father page
@app.route('/father')
def father_page():
    return "This is the Father page"

# Decorator function for the /mother page
@app.route('/mother')
def mother_page():
    return "This is the Mother page"

# Decorator function for the /friend page
@app.route('/friend')
def friend_page():
    return "This is the Friend page"

if __name__ == '__main__':
    app.run(debug=True)
