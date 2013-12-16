Hello!
======

This is a very simple package which should get you started on [Heroku](http://heroku.com) to serve static files using Python [Tornado](http://tornadoweb.org). Knowledge of Python or Tornado is not required.

It can be used for serving a static blog or your personal portfolio page etc. You can check the demo [here](http://tornado-static.herokuapp.com/)

How to deploy on Heroku:
========================
- Make sure you already have an account on [Heroku](https://id.heroku.com/signup/www-header) and you have [set up](https://devcenter.heroku.com/articles/quickstart) your local machine.
- Run `heroku login` command in terminal, enter your email and password. If you get 'Authentication successful.' then your machine is setup.
- [Download the zip](https://github.com/avinassh/heroku-tornado-starter/archive/1.zip) or clone this repo by running following : `git clone https://github.com/avinassh/heroku-tornado-starter.git`
- cd into the heroku-tornado-starter
- Run this to create an app on Heroku:
`heroku create --stack cedar`
- Now push the repo to heroku by running:
`git push heroku master`
- Done ! Run `heroku open` to open your site in browser.
- Bro tip : rename the app by following : `heroku apps:rename new-name`


Feeling lazy? Run the [starter.sh](https://github.com/avinassh/heroku-tornado-starter/raw/master/starter.sh) script, it will do all the steps for you!

So, what next?
==============
Make changes to index.html as required. This is the default file which will be served whenever someone visits your site. Do not rename or remove this file. You can add more HTML files and keep them in same directory or in subdirectory. You can add/modify stylesheets under assets/css and javascripts under assets/js directory. All the paths are relative and specified with respect to root directory i.e. '/' 

To keep things clean, move all your images to assets/images and other assets to respective directories. You can link them in your HTML with path relative to root. 
e.g. `<link rel="stylesheet" href="/assets/css/style.css">`

Once all required changes are made, commit them and then run `git push heroku master`. Done! :sunglasses: