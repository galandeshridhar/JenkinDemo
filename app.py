from flask import Flask, render_template,request

app = Flask(__name__)
@app.route("/", methods =["GET", "POST"])
def index():
    addition = 0
    if request.method == "POST":
        num1 = eval(request.form.get("number1"))
        num2 = eval(request.form.get("number2"))
        #print("Addition: "+ str(num1 + num2))
        #num1 = 1
        #num2 = 2
        addition = num1 + num2
    return render_template("index.html",Add=addition)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)