from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from app.models.medicine import Medicine
from functools import wraps

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

def login_required(f):
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
    user_id = session["user_id"]
    username = session["username"]
    medicines = Medicine.get_all_by_user(user_id)
    return render_template("dashboard/home.html", username=username, medicines=medicines)


@dashboard_bp.route("/medicine/add", methods=["POST"])
@login_required
def add_medicine():
    user_id = session["user_id"]
    name = request.form["name"]
    dosage = request.form["dosage"]
    times = request.form["times"]
    description = request.form["description"]

    Medicine.create(user_id, name, dosage, times, description)

    flash("Medicine added successfully!", "success")
    return redirect(url_for("dashboard.home"))


@dashboard_bp.route("/medicine/edit/<int:med_id>", methods=["POST"])
@login_required
def edit_medicine(med_id):
    name = request.form["name"]
    dosage = request.form["dosage"]
    times = request.form["times"]
    description = request.form["description"]

    Medicine.update(med_id, name, dosage, times, description)
    flash("Medicine updated successfully!", "success")
    return redirect(url_for("dashboard.home"))

@dashboard_bp.route("/medicine/delete/<int:med_id>", methods=["POST"])
@login_required
def delete_medicine(med_id):
    Medicine.delete(med_id)
    flash("Medicine deleted successfully!", "success")
    return redirect(url_for("dashboard.home"))
