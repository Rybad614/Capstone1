# TuneSeek: find music by the lyrics
You can visit at, [tuneseek.com]().


## How It Works:

There may be a piece of a song stuck on repeat in your head right now, but you don't know the title of it? You want to find songs similar to a song you like? Just looking for songs new to you based off of words you heard, or emotions you feel?

The solution is here!

### Features:

- Search field: Find the most relateable song info based off lyrics typed.
- Select Genre and Year: Better percentage of getting what has been searched.
- Account registration: For history and suggestion purposes.
- DarkMode: Style for user preferences.


## Site Tour:

On the landing page, a user will be prompted to use the lyrics of the song they are searching for. These fields help find exactly what is wanted to be found, therefore they are required to fill out(if you do not know the genre or year range, select `"Uncertain"`).

The user will then be directed to the result page where the question, `"Is this what you're looking for?"` will be asked. Simply select the correct answer (found under the song info) and `confirm`. 
On `"Yes"`, the result will be added to your `"recently searched"` list, if user is signed in, otherwise you will be directed to the sign up page. 
On `"No"`, the next result will be presented. If the result is wrong 5 times, a message will appear to inform the user, the answer cannot be found.
Users also have the option to edit their search, but will be directed to the sign up page if not signed in.

Use the `"Contact me"` link found in the top left of the page if you need help, find a bug/problem, or just want to get in touch with the site creator.


## Created using:
[Genius API](https://docs.genius.com/#songs-h2)

[LyricGenius](https://github.com/johnwmillr/LyricsGenius)

- HTML / CSS
- JavaScript
- Python
- Flask 
- PostgreSQL