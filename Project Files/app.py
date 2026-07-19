from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Tableau Public Configuration
TABLEAU_BASE_URL = "https://public.tableau.com/views/Food_Delivery_Analysis_17840324425720"
TABLEAU_PROFILE = "yashwanthkumar.mallela"

@app.route("/")
def index():
    """Landing page with overview and navigation."""
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    """Dashboard embed page."""
    return render_template(
        "dashboard.html",
        tableau_url=f"{TABLEAU_BASE_URL}/Dashboard1",
        tableau_profile=TABLEAU_PROFILE,
    )

@app.route("/story")
def story():
    """Story embed page."""
    return render_template(
        "story.html",
        tableau_url=f"{TABLEAU_BASE_URL}/Story1",
        tableau_profile=TABLEAU_PROFILE,
    )

@app.route("/about")
def about():
    """About page."""
    return render_template("about.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") != "production"
    app.run(debug=debug, host="0.0.0.0", port=port)
