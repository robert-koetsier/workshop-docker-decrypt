from flask import Flask, request, render_template_string
from secretpy import Keyword
import os

KEY = os.environ.get("KEY")

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Text Processor</title>
  <style>
    body {
      font-family: system-ui, sans-serif;
      background: #f8f9fa;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .container {
      background: white;
      padding: 2rem;
      border-radius: 1rem;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      text-align: center;
      width: 300px;
    }
    input[type="text"] {
      width: 100%;
      padding: 0.5rem;
      border: 1px solid #ccc;
      border-radius: 0.5rem;
      margin-bottom: 1rem;
      font-size: 1rem;
    }
    input[type="submit"] {
      background-color: #007bff;
      color: white;
      border: none;
      padding: 0.5rem 1rem;
      border-radius: 0.5rem;
      cursor: pointer;
      font-size: 1rem;
    }
    input[type="submit"]:hover {
      background-color: #0056b3;
    }
    h2 {
      margin-bottom: 1rem;
    }
    p {
      background: #f1f3f5;
      padding: 0.5rem;
      border-radius: 0.5rem;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Enter text</h2>
    <form method="post">
      <input type="text" name="text" placeholder="Type something..." autofocus>
      <input type="submit" value="Process">
    </form>
    {% if result %}
      <h3>Result:</h3>
      <p>{{ result }}</p>
    {% endif %}
  </div>
</body>
</html>
"""
def write_message(message, out_file):
    with open(out_file, 'w') as out:
        out.write(message)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form.get("text", "")
        cipher = Keyword()
        try:
            result = cipher.decrypt(text, KEY)
            write_message(result, "/app/results/message.txt")
        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
