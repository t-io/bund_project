#GEODJANGO + MYSQL PROJECT #
##FOR THE MODULE GIS PROJECT 1


###GENERAL INSTALLATION

>Used with Vagrant:
>git clone https://github.com/pix0r/vagrant-lucid32-geodjango.git
>added also:
>>MySQL and python connector			
>>( sudo apt-get install mysql-server python-mysqldb )
>>pip install -r requirements.txt		( all the Project PyPI's)
>create DB:
>>mysql -u root -p 		# pass = 'root'
>>CREATE DATABASE django_db;
>>GRANT ALL ON django_db.* TO 'djangouser'@'localhost' IDENTIFIED BY 'mypassword';

###DESCRIPTION
> The goal for this project is to build an application wich can handle line and point types
> create, show and edit on an JS Map.

###CREATE INITIAL EXAMPLE DATA
>python manage.py dumpdata projekte.Road
>copy paste them to fixtures/initial_data.json

###PICTURES
<a href="http://www.flickr.com/photos/t_io/sets/72157634318569472" target="_blank">some screenshots</a>
