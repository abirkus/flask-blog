## Blog Posts with Flask

This a coding exercise setting up blog posts website using python, Flask and sqlite3.  
This repo is created for educaitonal purposes only and follows the instructions provided by [DigitalOcean.](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3) 


### Intro
Flask is a backend framework. It handles server-side operations like processing requests, managing databases, and serving content. While Flask can render HTML templates, it primarily focuses on backend logic. For frontend development, it’s commonly paired with HTML, CSS, and JavaScript, often utilizing frontend frameworks like Bootstrap.


### Prerequisites
1. Make sure python is installed on your local machine: `pip --version` pr `pip3 --version`
2. It is recommended to use a virtual environmant in your directory to isolate Python packages from the system 
```powershell
    python3 -m venv myenv  # Create a virtual environment
    source myenv/bin/activate  # Activate it
    pip install --upgrade pip  # Upgrade pip inside the virtual environment
```

3. Install Flask and validate: 
```powershell
    pip install flask
    python -c "import flask; print(flask.__version__)"
```

4. When finished, deactivate the virtual environment
```powershell
    deactivate
```




### Flask Syntax Notes
- @app.route is a decorator that turns a regular Python function into a Flask view function, which converts the function’s return value into an HTTP response to be displayed by an HTTP client, such as a web browser. You pass the value '/' to @app.route() to signify that this function will respond to web requests for the URL /, which is the main URL.
- Flask provides a render_template() helper function that allows use of the [Jinja template](https://jinja.palletsprojects.com/en/stable/) engine.
- To respond with a 404 page, you need to import the abort() function from the [Werkzeug library](https://werkzeug.palletsprojects.com/en/stable/), which was installed along with Flask
- The flash() function stores flashed messages in the client’s browser session, which requires setting a secret key. This secret key is used to [secure sessions](https://flask.palletsprojects.com/en/stable/api/#sessions), which allow Flask to remember information from one request to another, such as moving from the new post page to the index page. 
- use a SQLite database file to store your data because the sqlite3 module, which we will use to interact with the database, is readily available in the standard Python library.

### QuickStart
- Type `flask run` in the root directory to boot the app
- Navigate to `http://127.0.0.1:5000` in your browser to interact with the app