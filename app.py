from flask import Flask, render_template, request
import service.logger as logger

import requests

app = Flask(__name__)
log = logger.Logger()


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    """ Home page """
    log.debug(f"Method: {request.method}")
    if request.method == 'POST':
        joke = get_chuck_norris_joke()
        log.debug(f"Joke: {joke}")
        log.debug("Rendering index.html")
        return render_template(template_name_or_list='index.html', title='Home', joke=joke)
    log.debug("Rendering index.html")
    return render_template(template_name_or_list='index.html', title='Home')


@app.route('/helloWorld')
def hello_world() -> str:
    """ Secret helloWorld page """
    log.debug("Found hidden treasure hello world")
    return '<p>Hello, World!</p>'


@app.errorhandler(404)
def not_found(error) -> tuple[str, int]:
    """ Error handling for 404 errors """
    log.error(error)
    return (render_template(template_name_or_list='404.html'), 404)


def get_chuck_norris_joke() -> str:
    """ Get a random Chuck Norris joke with the help of the API https://api.chucknorris.io/ """
    log.debug("Getting Chuck Norris joke")
    response = requests.get(url = "https://api.chucknorris.io/jokes/random", stream=True)
    return response.json()["value"]


if __name__ == '__main__':
    log.info("Starting application")
    app.run()
