git clone https://github.com/avinassh/heroku-tornado-starter.git
cd heroku-tornado-starter
heroku login
heroku create --stack cedar
git push heroku master