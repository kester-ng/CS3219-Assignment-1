from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "http://www.rover.com/blog/wp-content/uploads/2019/06/cat-4223305_1920-300x200.jpg"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")