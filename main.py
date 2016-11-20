from optparse import OptionParser
from flask import Flask, request, abort, redirect, url_for,render_template, make_response
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
import authomatic

#slogin_manager = LoginManager()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
     return render_template('index.html')

@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):

    response = make_response()
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)

    if result:
        if result.user:
            result.user.update()
        return render_template('login.html', result=result)

    return response












if __name__ == "__main__":

    parser = OptionParser()
    prod = False
    parser.add_option("-p", "--prod",
                  action="store_true", dest="prod", default=False,
                  help="don't print status messages to stdout")
    (options, args) = parser.parse_args()

    if options.prod == True:
        app.run(host='0.0.0.0',port=80)
    else:
        app.run(use_debugger=True, debug=True,
      use_reloader=True)
