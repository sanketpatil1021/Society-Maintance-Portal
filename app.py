from flask import *
import sqlite3


app=Flask(__name__)

app.secret_key="anhshgvghv"

@app.route("/")
def login():
     return render_template('index.html')




# @app.route("/login")
# def login1():
#     return render_template("index.html")py

@app.route("/adminragistration")
def adminragistration():
    return render_template("adminragistration.html")

@app.route("/adminregistration_save",methods=["POST","GET"])
def adminragistration_save():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["emailid"]
        phone = request.form["phone_no"]
        password = request.form["password"]

        con = sqlite3.connect("admin.db")
        cur = con.cursor()
        cur.execute("insert into admin (name,email_id,contact_no,password)values(?,?,?,?)", (name, email, phone, password))
        con.commit()
        return redirect(url_for("login"))
    else:
        return "Fail"

@app.route("/adminlogin")
def adminlogin():
    return render_template("index.html")


@app.route("/report")
def report():
    con = sqlite3.connect("admin.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM flat")
    flats = cur.fetchall()
    con.close()
    return render_template("report.html", flats=flats)



@app.route("/search")
def search():
    query = request.args.get("query")
    con = sqlite3.connect("admin.db")
    cur = con.cursor()
    # Query the database with the search term
    cur.execute("""SELECT * FROM flat WHERE flat_no LIKE ? OR owner_name LIKE ? OR contact_no LIKE ? OR alternate_contact_no LIKE ? """, ('%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%'))
    results = cur.fetchall()
    con.close()
    return render_template("search.html", results=results, query=query)



@app.route("/check",methods=["POST","GET"])
def check():
    if request.method=="POST":
        email=request.form["emailid"]
        password=request.form["password"]

        con = sqlite3.connect("admin.db")
        cur = con.cursor()
        cur.execute("select * from admin where email_id=? and password=?",(email,password))
        data=cur.fetchall()

        if len(data) == 1:
           session["username"] = email# session start
           return redirect(url_for("dashboard"))


        else:
            return redirect(url_for("login"))





@app.route("/dashboard")
def dashboard():
    if session.get('username') is not None:
        return render_template("dashboard.html")
    else:
        return redirect(url_for("login"))





@app.route("/ragistration")
def  ragistration():
    if session.get('username') is not None:
        return render_template("ragistration.html")
    else:
        return redirect(url_for("login"))

@app.route("/ragistration_save",methods=["POST","GET"])
def ragistration_save():
    if request.method == "POST":
        flatno = request.form["flat_no"]
        oname = request.form["ownername"]
        contactno=request.form["phone_no"]
        altconno=request.form["alt_phone"]

        con=sqlite3.connect("admin.db")
        cur=con.cursor()
        cur.execute("insert into flat(flat_no,owner_name,contact_no,alternate_contact_no)values(?,?,?,?)",(flatno,oname,contactno,altconno))
        con.commit()
        return redirect(url_for("dashboard"))
    else:
        return "fail"


@app.route("/maintanance")
def maintanance():
    if session.get('username') is not None:
        return render_template("maintanance.html")
    else:
        return redirect(url_for("login"))

@app.route("/maintanance_save",methods=["POST","GET"])
def maintanance_save():
    if request.method == "POST":
        date = request.form["date"]
        amount=request.form["amount"]
        des=request.form["Description"]

        con=sqlite3.connect("admin.db")
        cur=con.cursor()
        cur.execute("insert into maintanance(date,amount,description)values(?,?,?)",(date,amount,des))
        con.commit()
        return redirect(url_for("dashboard"))
    else:
        return "fail"

@app.route("/expenses")
def  expenses():
    if session.get('username') is not None:
        return render_template("expenses.html")
    else:
        return redirect(url_for("login"))

@app.route("/expenses_save",methods=["POST","GET"])
def expenses_save():
    if request.method == "POST":
        fromdate = request.form["fromdate"]
        todate = request.form["todate"]
        amount=request.form["amount"]
        des=request.form["Description"]

        con=sqlite3.connect("admin.db")
        cur=con.cursor()
        cur.execute("insert into expenses(fromdate,todate,amount,description)values(?,?,?,?)",(fromdate,todate,amount,des))
        con.commit()
        return redirect(url_for("dashboard"))
    else:
        return "fail"

@app.route("/record")
def record():
    con = sqlite3.connect("admin.db")
    cur = con.cursor()
    cur.execute("select * from flat")
    data1 = cur.fetchall()

    cur.execute("select * from maintanance")
    data2 = cur.fetchall()
    cur.execute("select * from expenses")
    data3 = cur.fetchall()

    return render_template("records.html", data1=data1,data2=data2,data3=data3)



@app.route("/delete/<int:id>")
def delete(id):
    con = sqlite3.connect("admin.db")
    cur = con.cursor()
    cur.execute("delete from flat where id=?",[id])
    con.commit()
    return redirect(url_for("record"))

@app.route("/edit/<int:id>")
def edit(id):
    con = sqlite3.connect("admin.db")
    cur = con.cursor()
    cur.execute("select * from flat where id=?", [id])

    con.commit()
    data = cur.fetchone()
    return render_template("edit_flat.html", data=data)

@app.route("/edit_profile", methods=["POST"])
def edit_profile():
    id = request.form["id"]
    flat_no = request.form["flat_no"]
    name = request.form["ownername"]

    phone = request.form["phone_no"]
    alt_no = request.form["alt_phone"]

    con = sqlite3.connect("admin.db")
    cur = con.cursor()
    cur.execute("UPDATE flat SET  flat_no=?,owner_name=?, contact_no=?, alternate_contact_no=? WHERE id=?", (name, flat_no, phone, alt_no, id))
    con.commit()
    con.close()
    return redirect(url_for("record"))

@app.route("/logout")
def logout():
    session.pop('username',None) #session end
    return redirect(url_for("login"))

if __name__==("__main__"):
    app.run(debug=True)