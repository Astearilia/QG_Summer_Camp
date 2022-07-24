# Flask

## Python装饰器

- python里的函数可以付给变量，例如

```python
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"
 
    def welcome():
        return "now you are in the welcome() function"
 
    if name == "yasoob":
        return greet
    else:
        return welcome
 
a = hi()
print(a)
#outputs: <function greet at 0x7f2143c01500>
 
#上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
#现在试试这个
 
print(a())
#outputs: now you are in the greet() function
```

​	由于if-else中没有使用括号，函数没有执行

```python
def hi(name="yasoob"):
    return "hi " + name
 
print(hi())
# output: 'hi yasoob'
 
# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个
 
print(greet())
# output: 'hi yasoob'
 
# 如果我们删掉旧的hi函数，看看会发生什么！
del hi
print(hi())
#outputs: NameError
 
print(greet())
#outputs: 'hi yasoob
```

 这可以说明python里的函数操作与C有所不同

- 可以说python的函数装饰器能辅助函数进行封装，并通过这个封装来使函数作为参数传递

## Hello world!

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
```

## app.route

- @app.route('/') 指明了函数当地址是根路径时就调用下面函数

- 其中进入URL，网址之后就会进入根目录，读取到修饰符后会进入到函数中，打印出Hello world! 

- 返回的字符串可以修改为其他类型，例如

  ```html
  '<h1>Hello World!</h1>'
  ```

  使之成html指定的页面形式

## 路由

- flask通过将URL与app.rount()括号里的地址联系起来，完成了网址的读取

- 之后进入对应页面要在网址后面加上括号内的地址

- 可以在rount后面的括号里添加方式，如

  ```python
  methon=['GET','POST']
  ```

- 变量

  1. 可以通过在rount括号里使用尖括号来读取变量，例如

     ```python
     /user/<num>
     ```

     其中读取到的num是一个字符串，会通过命名参数传递到你的函数

- 变量表示

  1. int 整数
2. float 浮点数
  3. String 不带斜杆的字符串
4. path 带斜杆的字符串

```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_i

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

