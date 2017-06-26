1 创建一个窗口
===
我们创建一个窗口必须引入QApplication和QWidget
1. 每一个PyQt程序必须有一个application实例
2. QWidget中包含了基本的widgets

在QWidget类中，我们使用了resize、move、show方法
···python
sys.exit(app.exec_())
···
最后，我们进入应用程序的mainloop。事件处理从这一点开始。mainloop从窗口系统接收事件并将它们分派到应用程序小部件。如果我们调用该exit() 方法或主窗口小部件被破坏，那么mainloop就会结束。该sys.exit()方法确保一个干净的出口。环境将被通知应用程序如何结束。

该exec_()方法有一个下划线。这是因为这exec是一个Python关键字。因此，exec_() 被使用了。

2 带有图标的应用程序
===
```python
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('sun_logo.png'))
```
setGeometry结合了resize和move方法，QIcon()实例化了一个图标，参数是路径字符串

3 显示工具提示
===
在这个例子中，我们显示了两个PyQt5小部件的工具提示。
```python
QToolTip.setFont(QFont('SansSerif',10))
```
此静态方法设置用于呈现工具提示的字体。我们使用10pxSansSerif字体。
```python 
self.setToolTip（'这是一个<b> QWidget </ b>小部件）
```
要创建一个工具提示，我们称之为setTooltip()方法。我们可以使用富文本格式。
```python
btn = QPushButton('Button',self)
btn.setToolTip('这是一个<b> QPushButton </ b>小部件）
```
我们创建一个按钮小部件并为其设置工具提示。
```python 
btn.resize（btn.sizeHint（））
btn.move（50，50）
```
该按钮正在调整大小并在窗口上移动。该sizeHint() 方法给出了按钮的建议大小。

4 关闭窗口
===
```python 
qbtn.clicked.connect(QCoreApplication.instance().quit)
```
在这里将btn的点击信号与退出连接

5 Message Box
===
为了在程序退出的时候出现Message Box我们需要重写closeEvent()

6 窗口居中
===
QDesktopWidget类提供了用户桌面的信息
```python
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
```
# <center> 流程图
```flow
st=>start:开始
op1=>operation:得到程序窗口矩形
op2=>operation:获得桌面中心点
op2=>operation:将矩形的中心点移动到桌面中心点
op3=>operation:程序窗口的左上角对其矩形左上角
e=>end:结束

st->op1->op2->op3->e
```


```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```