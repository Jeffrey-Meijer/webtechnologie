#import x

from bungalowpark import app

@app.route('/')
def index():
    return 'test'
