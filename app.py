from flask import Flask, request, jsonify

import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def echo():
    data = {'headers':dict(request.headers),
            'method':request.method,
            'url':request.url,
            'args':request.args,
            'query_string':request.query_string,
            'form':request.form,
    }
    print dir(request)
    print data
    return jsonify(**data)

if __name__ == '__main__':
    app.run(debug=True)
