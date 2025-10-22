from flask import Flask, request, render_template_string

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


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form.get("text", "")
        result = "-- " + text.upper() + " --"
    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
