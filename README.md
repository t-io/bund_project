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

###CURRENT STATE
>![alt text](https://github.com/t-io/bund_project/blob/master/current_state.png "LandingPage for the Project")


###PROJECT MEMBER
>grischa thomas