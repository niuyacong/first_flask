from flask import   Flask,render_template,request,url_for,redirect,flash,abort
from models import users
app =Flask(__name__)
# 给消息加密的key
app.secret_key="123" 

@app.route('/')
def hello_world():
    return "hello world"

# 将数据返回模板
@app.route('/hello/<name>')
def hello(name=None):
    app.logger.error('An error occurred')
    return render_template('hello.html', name=name)

# 接收参数
# 1、
@app.route('/users/<id>',methods=['POST'])
def hello_user(id):
    return "user"+id
# 2、
@app.route('/data')
def query_data():
    # 获取参数中的值
    # return request.args.get('id')
    # 获取表单中的参数
    return request.form["id"]


# url_for 反向路由
@app.route('/query_user')
def query_users():
    # 重定向
    # return redirect(url_for('test'))
    return (url_for('test'))

@app.route('/test')
def test():
    return "2"


# 向页面输出model
@app.route('/user_test')
def user_test():
    name=request.args.get('name')
    age=request.args.get('age')
    user=users.User(name,age)
    userlist=[]
    for i in range(11):
        user_model=users.User("name"+str(i),i)
        userlist.append(user_model)
    # 消息提示
    flash("hello world")
    return render_template('user_test.html',user=user,users=userlist)

@app.route('/one')
def OnePage():
    return render_template("onebase.html")

@app.route('/mylogin')
def mylogin():
    return render_template("mylogin.html")

@app.route('/login',methods=['POST'])
def login():
    form=request.form
    username=form.get('username')
    password=form.get('password')
    if not username:
        flash("please input username ")
        return render_template("mylogin.html")
    if not password:
        flash("please input password ")
        return render_template("mylogin.html")
    if  username=="nyc" and password=="111111":
        flash("login success")
        return render_template("mylogin.html")
    else:
        flash("username or password is wrong")
        return render_template("mylogin.html")
# 自定义异常处理
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route('/test/<userid>')
def tests(userid):
    if int(userid)==1:
        return render_template("mylogin.html")
    else:
        abort(404)


if __name__=="__main__":
    app.run()