
# coding: utf-8

# In[2]:


from flask import Flask, flash, redirect, render_template, request, session, abort, Markup
import os
import ctypes  # An included library with Python install.   
import tableauserverclient as TSC
import pandas as pd
import datetime as dt
from datetime import datetime, timedelta
import random
import string
import numpy as np

log=pd.read_csv('Log.csv')
app = Flask(__name__, template_folder='flask_template')
error=''
message="e"


@app.route('/<username>',methods=['GET'])
def home(username):
    global logged_by,log_time
    log_time=dt.datetime.now()
    logged_by=username
    return render_template('password_reset.html',message=message)

@app.route('/user',methods=['POST'])
def reset():
    #ctypes.windll.user32.MessageBoxW(0,"Please confirm to reset password", "Action", 1)
    tableau_auth = TSC.TableauAuth('Kamalesh', 'Welcome123', 'Dealers')
    server = TSC.Server('http://partnerbi.ashleycc.com')
    date=datetime.now()
    input_name=request.form['username']
    with server.auth.sign_in(tableau_auth):

        all_users = list(TSC.Pager(server.users))
        appended = pd.DataFrame(all_users,columns=['tableau_alias'])
        appended['tableau_alias'] = appended['tableau_alias'].apply(str)
        appended['user_id'] = appended['tableau_alias'].apply(lambda x:x.split('name=')[1].split(' ')[0])
        appended['ID'] = appended['tableau_alias'].apply(lambda x:x.split('User ')[1].split(' name=')[0]) 


        if len(appended[appended['user_id']==input_name])>0:
            user=appended[appended['user_id']==input_name]['user_id'].values[0]
            ID=appended[appended['user_id']==input_name]['ID'].values[0]
            
            #newuser = TSC.UserItem(user, 'Interactor')
            #password setting
            key=(str('%02d'%date.hour)[1])+(str('%02d'%date.minute)[1])+(str('%02d'%date.second)[1])
            d=int(str('%02d'%date.hour)[1])+int(str('%02d'%date.minute)[1])+int(str('%02d'%date.second)[1])
            if len(str(d))>1:
                t=int(str(d)[1])+int(str(d)[0])
            else:
                t=d

            list1=['*','!','#','(',')','_','[',']','@']
            password=user[1]+user[0]+list1[t-1]+key
            
            
            for i in all_users:
                if i.name==user and i.id==ID:
                    newuser=i
            
            
            #result=ctypes.windll.user32.MessageBoxW(0,"Please confirm to reset password", "Action",4|0x00001000)
            '''message = "hiTHERE DFSFDS"
            flash(message)
            return render_template('password_reset.html')
            '''
            result=6
            print(result)
            if result == 6:#YES ID is 6 , No ID is 7
                newuser = server.users.update(newuser, password)
                message = 'New password :              '+password
                #print(message)
                username=logged_by
                reset_time=dt.datetime.now()
                log.loc[len(log)] = [user,reset_time,username]
                log.to_csv('Log.csv',index=False)
                return home(username)+message
            
            else:
                message='Password not changed'
                username=logged_by
                #print(message)
                return home(username)+message
            
        elif len(input_name)>0:
            message = 'Enter valid UserName'
            user=logged_by
            return home(user)+message
        else:
            #ctypes.windll.user32.MessageBoxW(0, "User not valid", "Alert",0x00001000)
            message = 'UserName field cannot be empty'
            username=logged_by
            return home(username)+message   


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=False,host='0.0.0.0')




