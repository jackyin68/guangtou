#001
price_of_house = "1000000"
is_good_credit = False
if is_good_credit:
    number1 = str(int(price_of_house) * 0.1)
    print(('the down payment is ') + (number1))
else:
    number2 = str(int(price_of_house) * 0.2)
    print(('the down payment is ') + (number2))
print('end of 001')
#001标准答案
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
#print(f'you will pay ${down_payment}') 格式化字符串 formatted string会把引号内除{}外的变量变为文本，方便引用
print(f"down payment: {down_payment}")
print('end of 001标准答案')
#002
# print("please type your name here: ")
name = "Tom"
name_lens = len(name)
if name_lens < 3 :
    print("name must be at least 3 characters")
elif name_lens > 50 :
    print("name can be a maximum of 50 characters")
else:
    print("name looks good!")
print('end of 002')
#002标准答案:没有name_lens这个变量，直接if len（name）<3

#003
# weight = input('Weight: ')
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == 'L':
#     weight1 = weight * 0.45
#     print('your weight is' + weight1 + 'kg')
# elif unit.upper() == 'K':
#     weight2 = weight * 0.3
#     print('your weight is' + weight2 + 'Lbs')
# else :
#     print('type wrong unit')

#003标准答案：错误点在weight是一个string object不能和浮点值;如果用了格式化字符串就可以用同一个变量
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit.upper() == 'K':
    converted = weight / 0.45
    print(f"You are {converted} pounds")
else:
    print('type the wrong unit')
print('end of 003')
#004while语句
# secret_number = 9
# guess_count = int(input('guess a number: '))
# guess_limit = 3
# while guess_count < guess_limit:
#     if guess_count == secret_number:
#         print('Congratulations！')
#     else:
#         print("Loser!")
# print('Game Over')
#004第二次尝试
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
    elif guess_count >= guess_limit:
        print("Loser!")
#004标准答案
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print("Sorry you failed!")
print('end of 004')
#005while循环 增加布尔值表示车的状态，根据该变量的状态判断车子是否被多次启动
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":#在下面加入another if语句来判断是否启动
        if started:
            print("Car is already started....")
        else:
            started = True
            print("Car started.")
    elif command == "stop":
        if not started:
            print("Car is already stopped...")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        print("Game over")
        break
    else:
        print("Sorry,I don't understand that!")
#006for循环
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"the total price is: {total}")
#007 loop嵌套 内循环inter loop循环完三次之后才会跳到外循环
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")
#008测试1
# dot = "xxxxxxx"
# numbers = [5, 2, 5, 2, 2]
# for number in numbers:
#     x = number + 1
#     for x in dot:
#         print(x)
#测试2 print(f"'x' * {number}") python可以用string乘以一个数字
#008答案1
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print('x' * number)
#008答案2
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'#output = output + 'x' 调用了_add_
    print(output)
#009list
number = [3, 6, 7, 4, 2, 10, 9]
max = number[0]
for number in numbers:
    if number > max:
        max = number
print(max)
#010list
numbers = [2, 2, 3, 5, 3, 7, 8, 9, 23, 33]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
#011字典
customer = {
    "1": "one",
    "2": "two"
}
ph = input("Phone ")
output = ""
for cu in customer:
    output += customer.get(cu, "!") + " "
print(output)
#012字符的输入与拆分，形成新的列
message = input(">")
words = message.split(" ")
print(words)
#013字符拆分输入，加入字典，字典内冒号，不能忘了逗号分隔--019
message = input(">")
words = message.split(" ")
emoji = {
    ":)": "😄",
    ":(": "😂"
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)
#014function需要空两行下面会显示start然后调用函数里的命令最后打印finish


def greet_user():
    print('Hi there!')
    print('Welcome aboard')


print("Start")
greet_user()
print('Finish')
#015rename


def greet_user(name):
    print(name)
    print('Welcome aboard')


print("Start")
greet_user("John")
print("finish")
#016refactor rename


def greet_user(first_name, last_name):#这个是形参是hole或者占位符定义了接受的信息
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("John", "Smith")#argument是实际信息
print("finish")
#017函数利用return


def square(number):
    return number * number


result = square(3)
print(result)
#018return


def square(number):
    return number * number


print(square(3))
#019将013emoji部分转化成函数形式,改写的时候注意，function部分不应该包含input和output的内容


def emoji_converter(message):
    words = message.split(" ")
    emoji = {
        ":)": "😄",
        ":(": "😂"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))
#020try except避免输入值错误导致程序崩溃
try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age
    print(risk)
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid value')
#use comments to say why and how, not what
#021类class
class Point:
    def __init__(self, x, y):#初始化，构建类的属性in the body of the method
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)
#022类
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()
#023类的继承
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass

class Cat(Mammal):
    def be_cut(self):
        print("cut")


cat = Cat()
cat.be_cut()
#024模块封装可调用
def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45
#将以上代码写入一个py文件converters保存在同一个项目下
import converters
print(converters.kg_to_lbs(50))
#另外还可以导入modular中特定的function，这样就不需要加模块名进行前缀
from converters import kg_to_lbs
kg_to_lbs(100)
#025封装类
numbers = [1, 3, 5, 73, 43]


def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


print(find_max(numbers))
#utils上面的放在py文件中
from utils import find_max
numbers = [1, 3, 5, 73, 43]
max = find_max(numbers)#max其实是一个函数也可以直接实现findmax的功能,可以call it(max(numbers))，在这里max重新被赋值为一个整数
print(max)
#py3 内置模块演示
import random
for i in range(3):
    print(random.random(10,20))#（）会返回0到1的三个随机值
#内置模块random演示2
import random
menbers = ['John', 'Marry', 'Bob', 'Mosh']
leader = random.choice(menbers)
print(leader)
#026练习
import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
#027绝对路径
from pathlib import Path

Path()#括号里为空就会传递当前默认目录
path = Path("ecommerce")
#path下也有一些有趣的方法
print(path.exists())
print(path.mkdir())#创建了ecommerce的文件夹，会返回None，因为不会返回任何值
print(path.rmdir())#删除了
path = Path()
print(path.glob('*.*'))#点后面的可以变成文件名.py之类
for file in path.glob('*'):
    print(file)
#028读取excel
import pandas as pd
df = pd.read_csv('vgsales.csv')
print(df)
print(df.shape)
print(df.describe())
df.describe()




















