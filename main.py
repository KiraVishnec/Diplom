from lib2to3.pgen2 import driver
from unicodedata import numeric
from kivymd.app import MDApp
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import ButtonBehavior
from kivymd.utils.fitimage import FitImage
import sqlite3
from selenium import webdriver
import webbrowser
from contextlib import closing
from kivymd.uix.list import OneLineAvatarIconListItem, IRightBody
Window.size = 360, 640



class RoundIcon(ButtonBehavior,FitImage):
    pass


class WindowManager(ScreenManager):
    pass

class Login(Screen):
    pass
         
class Regi(Screen):
    pass

class News(Screen):
    pass

class Menu(Screen):
    pass

class Searchprof(Screen):
    pass

class Searchprofsucsess(Screen):
    pass

class Chats(Screen):
    pass

class Profile(Screen):
    pass

class SearchUserResult(OneLineAvatarIconListItem):
    pass

class Main(MDApp):

    def build(self): 
        
        FUmkcia = Builder.load_file('layout.kv')
        return FUmkcia


    def enter(self, user, passw):
        username = (user)
        password = (passw)
        con = sqlite3.connect("db/Socsetnew.db")
        cur = con.cursor()
        statement = f"SELECT login from User WHERE login='{username}' AND password='{password}';"
        cur.execute(statement)
        if not cur.fetchone():
            app = MDApp.get_running_app()
            app.root.get_screen('login').ids.user.error = True
            app.root.get_screen('login').ids.password.error = True
            print("Неверный логин")
        else:
            statement = f"SELECT status from User WHERE status NOT LIKE 'N' AND login='{username}' AND password='{password}';"
            cur.execute(statement)
            if not cur.fetchone():
                app = MDApp.get_running_app()
                app.root.current = "regi"
                a1= f"SELECT login from User WHERE login='{username}' AND password='{password}';"
                cur.execute(a1)
                records = cur.fetchone()
                app.root.get_screen('regi').ids.login.text = str(records[0])
                a2= f"SELECT password from User WHERE login='{username}' AND password='{password}';"
                cur.execute(a2)
                records = cur.fetchone()
                app.root.get_screen('regi').ids.passw1.text = str(records[0])
                a3= f"SELECT id from User WHERE login='{username}' AND password='{password}';"
                cur.execute(a3)
                records = cur.fetchone()
                app.root.get_screen('regi').ids.ident.text = str(records[0])
                print (records[0])


            else:
                if not cur.fetchone():
                    app = MDApp.get_running_app()
                    app.root.current = "profile"
                    a1= f"SELECT first_name from User WHERE login='{username}' AND password='{password}';"
                    cur.execute(a1)
                    records = cur.fetchone()
                    print (records[0])
                    app.root.get_screen('profile').ids.Fname.text = str(records[0])
                    a2= f"SELECT second_name from User WHERE login='{username}' AND password='{password}';"
                    cur.execute(a2)
                    records = cur.fetchone()
                    print (records[0])
                    app.root.get_screen('profile').ids.Sname.text = str(records[0])
                    a3= f"SELECT groupuser from User WHERE login='{username}' AND password='{password}';"
                    cur.execute(a3)
                    records = cur.fetchone()
                    print (records[0])
                    app.root.get_screen('profile').ids.Group.text = str(records[0])
                    con.commit()
                    cur.close()
                    con.close()

    def reg(self, login, passw1, passw2, name, nametwo, group, ident):
        loginnew = (login)
        passwordnew = (passw1)
        passwordnewretry = (passw2)
        familiya = (name)
        imya = (nametwo)
        gruppa = (group)
        id_user = (ident)
        app = MDApp.get_running_app()
        con = sqlite3.connect("db/Socsetnew.db")
        cur = con.cursor()
        print (id_user[0])
        if(str(passwordnew) == str(passwordnewretry)):
            
            query2 = f"UPDATE User SET login='{loginnew}',password='{passwordnew}',first_name='{familiya}',second_name='{imya}',groupuser='{gruppa}',status='S' WHERE id='{id_user}';"

            cur.execute(query2)
            cur.fetchone()

            app = MDApp.get_running_app()
            app.root.current = "profile"
            a1= f"SELECT first_name from User WHERE id='{id_user}';"
            cur.execute(a1)
            records = cur.fetchone()
            #print (records[0])
            app.root.get_screen('profile').ids.Fname.text = str(records[0])
            a2= f"SELECT second_name from User WHERE id='{id_user}';"
            cur.execute(a2)
            records = cur.fetchone()
            #print (records[0])
            app.root.get_screen('profile').ids.Sname.text = str(records[0])
            a3= f"SELECT groupuser from User WHERE id='{id_user}';"
            cur.execute(a3)
            records = cur.fetchone()
            #print (records[0])
            app.root.get_screen('profile').ids.Group.text = str(records[0])
            con.commit()
            cur.close()
            con.close()   
        else:
            print("Пароли не совпадают")



    def izmprof(self, Fname, Sname, Group):
        username = (Fname)
        secondusername = (Sname)
        gruppa = (Group)
        con = sqlite3.connect("db/Socsetnew.db")
        cur = con.cursor()
        statement = f"SELECT id from User WHERE first_name='{username}' AND second_name='{secondusername}' AND groupuser='{gruppa}';"
        cur.execute(statement)
        records = cur.fetchone()
        app = MDApp.get_running_app()
        app.root.current = "regi"
        app.root.get_screen('regi').ids.ident.text = str(records[0])
        print (records[0])




    def poisk(self, query):
        if query == "":
            pass
        else:
            app = MDApp.get_running_app()
            con = sqlite3.connect("db/Socsetnew.db")
            cur = con.cursor()
            statement = f"SELECT  first_name from User WHERE lower(first_name) LIKE'%{query}%'LIMIT 200;"
            cur.execute(statement)
            records1 = cur.fetchall()
            statement = f"SELECT  second_name from User WHERE lower(first_name) LIKE'%{query}%'LIMIT 200;"
            cur.execute(statement)
            records2 = cur.fetchall()
            statement = f"SELECT  id from User WHERE lower(first_name) LIKE'%{query}%'LIMIT 200;"
            cur.execute(statement)
            records3 = cur.fetchall()
            search_list_user = app.root.get_screen('searchprof').ids.searchuser
            search_list_user.clear_widgets()
            a = -1
            a = int(a)
            b = len(records1)
            b = int(b)
            b = b - 1
            while a < b:
                a = a + 1
                search_list_user.add_widget(
                    SearchUserResult(text= str(((records1[a]))[0]) + " " + str(((records2[a]))[0]))
            )
       

            print (records1)
            print (records2)
            print (records3)
            print (query)

    def pisat(self):
        pass
    
    
    
    def site(self):
        browse = webdriver.Chrome()
        browse.get("https://himkol.ru/")
    

    
    def hidenpass(self, query):
        if query.password == True:
            query.password = False
        elif query.password == False:
            query.password = True



    def import_pict_binary(pict_path):
        f = open(pict_path, 'rb')
        pict_binary = f.read()
        return pict_binary



if __name__ == '__main__':
    Main().run()