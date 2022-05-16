from flask import Flask
import cheat

app = Flask(__name__)
app.config["debug"] = True
@app.route('/')


def add_page():
    return '''
        <html>
            <body>
                <h1>cheatz 4 wordle</h1>
                <p>What would you like to search for?</p>
                <p>- Search for word starting with -</p>
                <form method="post" action="."> 
                    <p><input name="htmlquery" /></p>
                    <p><input type="submit" value="htmlsearch" /></p>
                </form>
                <p>- Search for word ending with -</p>
                <p>- Search for word containing -</p>
                <p>- Search for letters in a position -</p>
            </body>
        </html>
'''