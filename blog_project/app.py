from flask import Flask, render_template,request
import datetime
from pymongo import MongoClient


app=Flask(__name__)
client=MongoClient("mongodb+srv://krishnasankar:psks2002@cluster0.5uoahpg.mongodb.net/")
app.db=client.microblog

@app.route('/',methods=['POST','GET'])
def home():
    
    if request.method=='POST':
        entry_content=request.form.get('content')
        formatteddate=datetime.datetime.today().strftime("%Y-%m-%d")
        app.db.entries.insert_one({"content":entry_content,"date":formatteddate})
    
    entries_with_date=[
        (
            entry["content"],
            entry["date"],
            datetime.datetime.strptime(entry["date"],"%Y-%m-%d").strftime("%b %d")
        )
        for entry in app.db.entries.find({})
    ]
    return render_template('home.html',entries=entries_with_date)

if __name__=='__main__':
    app.run(debug=True)



