## 安装
- pip
```sh
pip install --upgrade pip
pip install playwright
playwright install
```
- conda
```sh
conda config --add channels conda-forge
conda config --add channels microsoft
conda install playwright
playwright install
```
## 录制脚本
- 并生成代码
```sh
playwright codegen + url
```

## 第一个脚本
- sync_playwright是一个支持上下文的函数,目前先理解为类似open
- 创建浏览器实例,headless默认为Ture无头模式,当指定为False时会模拟操作一遍,slow_mo控制模拟操作速度
- 创建页面实例
- 跳转至指定请求页面
- 可操作DOM(html文档对象模型)如title(可以验证一下这里打印的就是html中的title),可操作BOM(浏览器对象模型)如click,screenshot等事件
- 关闭浏览器实例,page实例类似浏览器实例中的线程,目测会随着浏览器实例关闭而关闭
```py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True,slow_mo=50)
    page = browser.new_page()
    page.goto("https://playwright.dev/python/docs/intro")
    print(page.title())
    browser.close()
```
## Inspector调试,GUI工具
1.先录制一个脚本inspec.py

```sh
// 请在录制过程中多操作几次,不要一会调试时一下就没了,将录制生成的代码复制到inspec.py
playwright codegen wikipedia.org
```

2.进入调试

- 理论上接项目文件完整路径,但我们通常都是在项目目录下操作,这里省略不写了
- win下powershell
```sh
$env:PWDEBUG=1
pytest -s  inspec.py
```
- mac下bash
```sh
PWDEBUG=1 pytest -s myproject.py
```
3.调试

- 单步执行
- 即将单击的点将在检查的页面上用大红点突出显示

4.除了以上调试方法之外还可以使用page.pause()

- 在page实例创建后的任意位置添加page.pause()
- 直接运行脚本,会将断点打在page.pause()的位置,即可执行单步调试

5.在调试模式打开时,可以在浏览器的开发者模式console项中使用playwright的api

```js
// playwright.$('text=English'),返回<strong>English<strong>
playwright.$(selector)            // 返回匹配的元素
playwright.$$(selector)           // 返回所有匹配的元素
playwright.inspect(selector)      // 检查元素,如果开发者工具Elements支持
playwright.locator(selector)      // 定位器,使用实际的playwright引擎查询元素
playwright.selector(element)      // 为给定元素生成选择器
```

## Trace Viewer跟踪
一个GUI工具

1. 记录跟踪
- 在context实例创建之后page实例创建之前声明要记录跟踪
- page实例操作完毕之后,关闭跟踪并导出跟踪文件
```py
context = browser.new_context()
// 参数分别为截图,呈现为胶片条,资源显示
context.tracing.start(screenshots=True, snapshots=True, sources=True)
page = context.new_page()
page.goto("https://playwright.dev")
context.tracing.stop(path = "trace.zip")
```
2.  查看跟踪
- 在[gui](https://trace.playwright.dev/)中选择跟踪文件打开
- 从终端打开
```sh
playwright show-trace trace.zip
```
3. 使用url远程查看跟踪,比如将trace.zip存放在github上(实测未成功,可能和我地址中文太多有关)
```sh
playwright show-trace  https://github.com/trace.zip
```



