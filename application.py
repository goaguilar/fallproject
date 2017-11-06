from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

   # User reached route via GET (as by clicking a link or via redirect)
    return render_template("index.html")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)
        # Ensure shares was submitted
        if not request.form.get("shares"):
            return apology("must provide shares amount", 403)
        # Ensure shares was submitted
        if not request.form.get("shares").isdigit():
            return apology("shares must be a number", 403)

        #Uppercase all char in symbol
        symbol = request.form.get("symbol").upper()
        #get quote of company with symbol
        quote = lookup(request.form.get("symbol"))
        #get amount of shares
        shares = request.form.get("shares")
        #get price of the stock
        priceperstock = quote["price"]
        #get total price of shares of stock
        price = priceperstock*shares

        #check to see if there is a quote or not
        if quote == None:
            return apology("Quote not found", 403)

        # Query database for cash balance
        balance = db.execute("SELECT cash FROM users WHERE id = :id",
                          id=session["user_id"])

        #updates the balance after the transaction
        new_balance = balance[0]['cash'] - price
        if new_balance < 0:
            return apology("Cannot Afford")

        #Updates balance in the database
        db.execute("Update users SET cash = ;new_balance WHERE id = :id",
                  new_balance=new_balance,
                  id=session["user_id"])
        #Updates database to add shares of stock to user
        rows = db.execute("SELECT * FROM portfolios WHERE id = :id AND stock = :symbol",
                          id=session["user_id"],
                          stock=symbol)
        #inserts the stock into the portfolio if it is not there
        if len(rows) == 0:
            db.execute("INSERT INTO portfolios (id, stock, shares) VALUES (:id, :symbol, :shares)",
                      id=session["user_id"],
                      stock=symbol,
                      shares=shares)
        else:
            db.execute("UPDATE portfolios SET shares = shares + :shares",
                      shares = shares)
        db.execute("INSERT INTO history (id, stock, shares, price) VALUES (:id, :symbol, :shares, :price)",
                  id=session["user_id"],
                  stock=symbol,
                  shares=shares,
                  price=price)
        return render_template("index.html")

   # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        return render_template("history.html")

   # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("history.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash('Successfully Logged In')
        return render_template("index.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        #Uppercase all char in symbol
        symbol = request.form.get("symbol").upper()
        #get quote of company with symbol
        quote = lookup(request.form.get("symbol"))

        #check to see if there is a quote or not
        if quote == None:
            return apology("Quote not found", 403)

        return render_template("quoted.html", name = quote["name"], symbol = symbol, price = quote["price"])
   # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure password confirmation was submitted
        elif not any(char.isdigit() for char in request.form.get("confirmation")):
            return apology("must contain at least one digit", 403)

        # Ensure password and password confirmation mation
        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("passwords must match", 403)

        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        if len(rows) == 1:
                return apology("user already exists", 403)
        rows = db.execute("INSERT INTO users(username, hash) VALUES (:username, :hash)",
                          username=request.form.get("username"),
                          hash=generate_password_hash(request.form.get("password")))

        # Redirect user to home pag
        flash('Successfully Registered')
        return redirect("/")

   # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)
        # Ensure shares was submitted
        if not request.form.get("shares"):
            return apology("must provide shares amount", 403)
        # Ensure shares was submitted
        if not request.form.get("shares").isdigit():
            return apology("shares must be a number", 403)

        #Uppercase all char in symbol
        symbol = request.form.get("symbol").upper()
        #get quote of company with symbol
        quote = lookup(request.form.get("symbol"))
        #get amount of shares
        shares = request.form.get("shares")
        #get price of the stock
        priceperstock = quote["price"]
        #get total price of shares of stock
        price = priceperstock*shares

        #check to see if there is a quote or not
        if quote == None:
            return apology("Quote not found", 403)

        # Query database for cash balance
        balance = db.execute("SELECT cash FROM users WHERE id = :id",
                          id=session["user_id"])

        #updates the balance after the transaction
        new_balance = balance[0]['cash'] + price

        #Updates balance in the database
        db.execute("Update users SET cash = ;new_balance WHERE id = :id",
                  new_balance=new_balance,
                  id=session["user_id"])
        #Updates database to subtract shares of stock to user
        rows = db.execute("SELECT * FROM portfolios WHERE id = :id AND stock = :symbol",
                          id=session["user_id"],
                          stock=symbol)
        db.execute("UPDATE portfolios SET shares = shares - :shares",
                  shares = shares)
        db.execute("INSERT INTO history (id, stock, shares, price) VALUES (:id, :symbol, :shares, :price)",
                  id=session["user_id"],
                  stock=symbol,
                  shares=shares,
                  price=price)
        return render_template("index.html")
   # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("sell.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
