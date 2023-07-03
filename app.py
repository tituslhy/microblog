import datetime
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from pymongo import MongoClient

def create_app():
    load_dotenv()
    app = Flask(__name__)
    MONGODB_URI = os.environ["MONGODB_URI"]
    client = MongoClient(MONGODB_URI)
    app.db = client.microblog #save db inside "app"

    @app.route("/", methods = ["GET", "POST"])
    def home():
        
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one({"content": entry_content,
                                    "date": formatted_date})
        
        entries_with_date = [
            (entry['content'],
            entry['date'],
            datetime.datetime.strptime(entry['date'], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
            ]
        return render_template('home.html', entries = entries_with_date)
    return app
