from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask_security import Security, SQLAlchemyUserDatastore
from model.oauth import User, Role
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

# 启动 Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# 创建flask admin
admin = Admin(app, name='后台管理',base_template='my_master.html', template_mode='bootstrap3')
admin.add_view(MyModelView(Role, db.session))
admin.add_view(MyModelView(User, db.session))
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
