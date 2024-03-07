from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_command', methods=['POST'])
def execute_command():
    command = request.form['command']
    try:
        result = subprocess.Popen(['cmd.exe', '/c', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        output, errors = result.communicate()
        if errors:
            return render_template('index.html', output=errors.decode('cp866'))
        else:
            return render_template('index.html', output=output.decode('cp866'))
    except Exception as e:
        return render_template('index.html', output=str(e))

if __name__ == '__main__':
    app.run(debug=True)