from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

def fetch_API_RandomUser():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch data")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            username, country = fetch_API_RandomUser()
            return render_template_string('''
                <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Random User</title>
                  </head>
                  <body>
                    <h1>Random User</h1>
                    <form method="post">
                      <button type="submit">Get Random User</button>
                    </form>
                    <p>Username: {{ username }}</p>
                    <p>Country: {{ country }}</p>
                  </body>
                </html>
            ''', username=username, country=country)
        except Exception as e:
            return str(e)
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <title>Random User</title>
          </head>
          <body>
            <h1>Random User</h1>
            <form method="post">
              <button type="submit">Get Random User</button>
            </form>
          </body>
        </html>
    ''')

if __name__ == "__main__":
    app.run(debug=True)
