# FlaskBlog

####  This is a web app that allows writers to write articles and delete articles and for readers to comment on the articles.

#### By Francis Mwangi Maina. {c.h.u.i}

## Link to live site
You can view the site here ---> https://flask-blog254.herokuapp.com

## Description
This is a blog site created using the python flask framework whereby writers can be able to write articles.

## User Stories
- [x] User can see various blog articles from various categories on the homepage of the application.
- [x] Writer can sign into the application and create an article
- [x] User can add a comment on any article
- [x] Writer can edit or delete an article in the application 
- [x] User sees random quotes displayed on the homepage

## Setup/Installation Requirements
* Ensure that Python is installed on your machine if not please visit the python website and download the latest version python 3.6
* Fork the repository and either download the project or clone it to your machine
* Create a virtual environment using the following command
```
python3.6 -m venv --without-pip virtualenv
```
* then install the latest version of pip
```
curl https://bootstrap.pypa.io/get-pip.py | python
```
* Register the secret key as an environment variable in your terminal as follows
```
export SECRET_KEY=<your-secret-key>
```
* Regester your Email as follows in the environment
```
export MAIL_USERNAME=<Your-email>
```
* Regester your Email Password as follows in the environment
```
export MAIL_PASSWORD=<Your-email-password>
```
* run the application from your terminal using the following command
```
python3.6 manage.py server
```
* To edit the code if you will need any dependancys you will need to navigate to the virtual environment in order to install them from there to avoid version conflicts
```
source virtualenv/bin/activate
```

## Technologies Used
1. Python Version 3.6
2. Flask Framework
3. Html
4. Bootstrap
5. Css

## Support and contact details
if you run into any issues please contact mainaf471@gmail.com

### License

*MIT*
Copyright (c) 2022 Francis Mwangi Maina [c.h.u.i]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.