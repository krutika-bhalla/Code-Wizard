import web
from models import RegisterModel
from models import LoginModel
from models import Posts

web.config.debug = False

urls =(
    '/', 'home',
    '/register', 'register',
    '/login', 'login',
    '/logout', 'logout',
    '/postregistration', 'postregistration',
    '/checklogin', 'checklogin',
    '/postactivity', 'postactivity'
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer = {'user': None})

session_data = session._initializer

render = web.template.render("views/templates", base="MainLayout", globals={'session':session_data, 'current_user': session_data["user"]})


# Classes/Routes

class home:
    def GET(self):
        data = type('obj', (object,), {"username": "yuru", "password": "yuru"})
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)
        if isCorrect:
            session_data["user"] = isCorrect

        post_model = Posts.Posts()
        posts = post_model.get_all_posts()
        return render.home(posts)

class register:
    def GET(self):
        return render.register()

class login:
    def GET(self):
        return render.login()

class postregistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username

class checklogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect


            return isCorrect

        return "error"

class postactivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        post_model = Posts.Posts()
        post_model.insert_post(data)
        return "success"

class logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "success"

if __name__ =="__main__":
    app.run()