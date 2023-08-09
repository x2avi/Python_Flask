# Python_Flask
Install packages
pip install -r requirements.txt

Run for concurrency
gunicorn --workers 3 --bind 0.0.0.0:5000 wsgi:app

Test API to generate Pascal triangle
curl --location --request POST 'http://localhost:5000/pascal?n=7'
