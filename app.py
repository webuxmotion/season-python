from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    result = ""
    result += "<h2>Виберіть номер місяця:</h2>"
    for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        result += f"<a href='/{month}'>{month}</a></br></br>"
    return result

@app.route("/<int:month>")
def month(month):
    if month in [12, 1, 2]:
        season = "Зима"
    elif month in [3, 4, 5]:
        season = "Весна"
    elif month in [6, 7, 8]:
        season = "Літо"
    elif month in [9, 10, 11]:
        season = "Осінь"
    else:
        season = "Невідомий місяць"

    return f"<a href='/'>Додому</a> | Пора року: {season}"

if __name__ == "__main__":
    app.run()