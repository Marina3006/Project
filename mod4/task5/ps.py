
from flask import Flask, request
from typing import List
import shlex
import subprocess

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    command = "ps"
    args: List[str] = request.args.getlist('arg')
    clean = [shlex.quote(i) for i in args]
    full_command = shlex.split(f"{command} {''.join(clean)}")
    result = subprocess.run(full_command, capture_output=True).stdout.decode()
    return "<pre>{result}</pre>".format(result=result)


if __name__ == "__main__":
    app.run(debug=True)