from flask import Blueprint, render_template, session, redirect, url_for, flash

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login first!", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated_function

@dashboard_bp.route("/")
@login_required
def home():
    username = session.get("username")
    return render_template("dashboard/home.html", username=username)
