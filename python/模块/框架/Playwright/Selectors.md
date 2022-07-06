# Selectors选择器
选择器Selectors是用于创建定位器Locators的字符串

定位器Locators用于定位元素,确定元素是who之后才能执行相应操作
## Text
- 默认不区分大小写
- 支持[JavaScript-like regex](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)表达式

```py
// 常规写法
page.locator("text=Log in").click()
page.locator("text='Log in'").click()

// 隐式转换,内引号不能省略
page.locator("'Log in'").click()

// 支持js正则
page.locator("text=/Log\s*in/i").click()
```
## css
playwright给dom自定义了伪类如：:visible,:text等

1.选择可见元素

假设有一个如下页面：
```html
<div>
<button style='display: none'>Invisible</button>
<button  class='c1' id='id1'>Visible</button>
<div/>
```
使用伪类,:visible
```py
# 正常选择只会找DOM顺序中的第一个button
page.locator("button").click()

# 限制选择第二个button
page.locator("button:visible").click()
page.locator("button >> visible=true").click()
```
2.选择包含其它元素的元素
- has用于检索标签属性
- has_text用于检索html标签所包裹的内容
- 支持链式定位,在定位器的基础上再次定位locator.locator(selector,\**kwargs)
```py
# 搜寻标签属性id为id1,内部text为Visible的元素
page.locator("#id1 :text('Visible')").click()

# 搜寻标签为button,内部text含Visible的元素
page.locator("button", has_text="Visible").click()

# 搜寻内部有button标签且class属性为c1的div元素,注意内部定位器从外部定位器开始匹配,而非从文档根目录开始匹配
page.locator("div", has=page.locator("button.c1"))
# :has伪类简写
page.locator("div :has("button.c1")).text_content()
```






