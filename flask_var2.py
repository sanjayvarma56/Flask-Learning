from flask import Flask
app = Flask(__name__)
@app.route('/facebook_Home/<name>')
def facebook_Home(name):
    return 'Welcome %s! '%name 
if __name__ == "__main__":
    app.run()