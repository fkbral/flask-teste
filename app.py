from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

print(__name__)

@app.route('/')
def main():
  return render_template('index.html')

if __name__ == '__main__' :
  app.run()