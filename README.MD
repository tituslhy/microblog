# Microblog

<div align="center">

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
<br>
![Generic badge](https://img.shields.io/badge/STATUS-INPROGRESS-<COLOR>.svg)
</div>

This is my first foray into fullstack web development. This website is a microblog made using python's flask and MongoDB, and deployed onto render.com. <br>

To run this project, first run the following command to instantiate the code environment.
```
git clone https://github.com/tituslhy/microblog
pip install -r requirements.txt
```
<br>
Then run the following codes to run them on your local machine
```
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```
Or if you have gunicorn installed, type
```
gunicorn "app:create_app()"
```

### Notes
Do note that you will need a MongoDB account and this will need to be kept in a .env file. To create a MongoDB account, visit [mongodb.com](https://www.mongodb.com/).
