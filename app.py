from flask import Flask, request, render_template, redirect, session, url_for
from models import connect_db, db, User, History
from forms import SignInForm, SignUpForm, EditForm, ContactForm, SearchForm, DeleteForm
from secret import GENIUS, SECRET_KEY
import requests

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///tuneseek"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY


connect_db(app)

def print_results(hit):
    print(hit['highlights'][0]['value'])
    print("__________________________")
    print(hit['result']['full_title'])
    print(hit['result']['release_date_for_display'])
    print("__________________________")


@app.route("/")
def homepage():
    """If logged in, redirect to profile page.
    
    Otherwise, homepage search bar.
    """

    form = SearchForm()
    if 'username' not in session:
        return render_template("homepage/index.html", form=form)
    
    user = session['username']
    user_profile(user)    
    return redirect(f"/user/{user}")


@app.route("/result", methods=['GET', 'POST'])
def search_result():
    """Info page for searched track."""


    form = SearchForm()
    lyrics = form.lyrics.data
    genre = form.genre.data
    year = form.year.data

    req = GENIUS.search_lyrics(lyrics)
    for hit in req['sections'][0]['hits']:
        print_results(hit)

    res = req['sections'][0]['hits'][0]
    display_art = res['result']['song_art_image_url']
    display_lyrics = res['highlights'][0]['value']
    display_song = res['result']['full_title']
    display_year = res['result']['release_date_components']['year']
    
    res2 = req['sections'][0]['hits'][1]['result']['full_title']
        
    results = {
        "art": display_art,
        "snippet": display_lyrics,
        "title": display_song,
        "published in": display_year
    }

    if 'username' not in session:
        return render_template("homepage/result.html",
                           form=form,
                           results=results)    
    
    user = session.get('username')
    recent = History.retrieve(display_song,
                              res2,
                              user)
    db.session.add(recent)
    db.session.commit()

    return render_template("homepage/result.html",
                           form=form,
                           results=results)


@app.route("/register", methods=['GET', 'POST'])
def user_register():
    """Sign up form to save data for a user.
    
    Will be rendered prior to second search.
    """

    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        passowrd = form.password.data
        email = form.email.data
        new_user = User.register(username,
                                 passowrd,
                                 email)
       
        db.session.add(new_user)
        db.session.commit()
        return redirect(f"/user/{new_user.username}")

    return render_template("register.html", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login_user():
    form = SignInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username, password)
        if user:
            session['username'] = username
            return redirect(f"/user/{user.username}")
        else:
            form.username.errors = ['Invalid username/password.']

    return render_template("login.html", form=form)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    """Contact form for the user to get in touch 
    with me (site editor) via email.

    """

    form = ContactForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        feedback = form.feedback.data
        content = form.content.data
        
        return redirect("/")

    return render_template("contact.html", form=form)


@app.route("/user/<username>")
def user_profile(username):
    """Profile page for user that contains
    all user info.
    
    """

    form = SearchForm()
    
    user = User.query.get(username)
    recent = History.query.all()
    return render_template("profile.html",
                           user=user,
                           form=form,
                           recent=recent)


@app.route("/user/<username>/edit", methods=["GET", "POST"])
def edit_profile(username):
    """Edit a users profile."""

    user = User.query.get(username)
    form = EditForm(obj=user)

    if form.validate_on_submit():
        user.bio = form.bio.data
        user.image = form.image.data
        db.session.commit()
        return redirect(f"/user/{user.username}")

    else:
        return render_template("edit.html", form=form, user=user)



@app.route("/logout")
def logout_user():
    session.pop("username")
    return redirect("/login")