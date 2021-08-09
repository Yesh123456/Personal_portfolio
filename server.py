from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_index():
    return render_template('./index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv','a') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])

@app.route("/submit_form",methods=['POST','GET'])
def submit_form():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
    except:
        return 'Data not stored'
    else:
        return 'Something went wrong'