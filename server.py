from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

def write_to_db(data):
    with open('database.csv', newline='', mode='a') as database:
        name = data["username"]
        email = data['email']
        subejct = data["subejct"]
        message = data["message"]
        csv_writter = csv.writer(database, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([name, email, subejct, message])

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=["GET", "POST"])
def email_sumb():
    if request.method == "POST":
        data = request.fo
        write_to_db(data)
        return redirect('./thanksYou.html')
    else:
        return "Something went wrong while send! OOHHHo"


app.run(debug=True)