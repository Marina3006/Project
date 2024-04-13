from flask import Flask
import sys
import subprocess

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    stdout = sys.stdout
    sys.stdout = subprocess.check_output('uptime', shell=True).decode('utf-8').strip().split(' ')
    output = [i for i in sys.stdout]
    sys.stdout = stdout
    # print(f'\033[36m{output[0]}')
    return f"Current uptime is {output[0]}"


if __name__ == '__main__':
    app.run(debug=True)