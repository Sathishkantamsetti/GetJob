#This file has the passwords to be used in the getjob app.
###################################################################################################
## To use the database go to remotemysql.com and create a db or create one in your localhost     ##
## and import the data shared as sql file(in the repo) using phpmyadmin.                         ##
################################################################################################### 
'''To be able to use the mailing of the webapp, create a gmail account 
    and go to security settings and allow access to unsecured apps.
'''
dbhost='' #localhost or #mysqlserver             
dbuser='' #database username //root if not configured
dbpass='' #database password //null if not configured          
db = ''   #name of the database
com_email='youremail@gmail.com' #the code has smtp configured for gmail, so use gmail or make changes in sendemail.py
email_pass='youremailpassword' #the password of your email