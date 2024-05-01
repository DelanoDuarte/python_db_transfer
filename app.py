from flask import Flask, render_template
from flask import request, make_response
import jinja_partials

from forms import MigrationForm

import os
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

jinja_partials.register_extensions(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/migration/metrics", methods=['GET'])
def migration_metrics():
    return render_template("migrations/metrics.html", 
                            migrated_tables_count = random.randint(1, 50), 
                            records_inserted_count = random.randint(1, 50)
                        )

@app.route("/migrate", methods=['POST'])
def migrate():
    form = MigrationForm(request.form)
    print(form.sourceHost.data)

    response = make_response(render_template('migrations/sumary.html', data = form.data))
    response.headers.add('HX-Trigger', 'migrationStarted')
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 