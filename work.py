from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def ini():
    if request.method == "GET":
        return render_template('homework.html')
    return redirect(request.form.get("URL"))

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='20000',debug=True)
