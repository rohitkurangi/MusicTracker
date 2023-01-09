# MusicTracker
##Python Virtual Environment

pip install virtualenv

virtualenv --version

virtualenv my_name



pip install django

django-admin startproject MusicPlayer


cd MusicPlayer

### migrations setup
python mananage startapp  catalogue

python manage startapp crud_ajax

python mananage makemigrations catalogue

python mananage migrate catalogue

mkdir templates
mkdir static


python manage.py runserver 0:8000

