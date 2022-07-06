# Selectors选择器
选择器Selectors用于创建定位器Locators的字符串

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
3.选择与条件之一匹配的元素
- 以逗号分隔的CSS选择器列表,只有满足其一即可匹配
- 这并不意味着会选择多个元素,因为定位器只会定位在DOM顺序中第一个满足的元素上
```py
# log in或sign in一般只会用一个，而我不知道用的是那个 
page.locator('button:has-text("Log in"), button:has-text("Sign in")').click()
```

4.XPath并集
- 使用管道运算符 | 来指定多个选择器
```py
# Waits for either confirmation dialog or load spinner.
page.locator("//span[contains(@class, 'spinner__loading')]|//div[@id='confirmation']").wait_for()
```

## 高级DOM元素选择
- 默认情况下css与text会进行深层匹配递归检索,不局限于当前层,当然在当前层匹配到则取当前层
- 可以使用伪类 :light限制只做当前层检索
- 不使用伪类的情况下,也可以使用 > 来限制层级,与css中子代与后代选择器相似,playwright中默认支持后代选择, > 限制子代选择 
```html
<!--html示例-->
<article>
  <div>In the light dom</div>
  <div slot='myslot'>In the light dom, but goes into the shadow slot</div>
  #shadow-root
    <div class='in-the-shadow'>
      <span class='content'>
        In the shadow dom
        #shadow-root
          <li id='target'>Deep in the shadow</li>
      </span>
    </div>
    <slot name='myslot'></slot>
</article>
```
```py
# 都只定位<div>In the light dom</div>
page.locator("article div")
page.locator(":light(article div)")

# 都定位到<article>下的所有div
page.locator("article > div")
page.locator(":light(article > div)")

# 递归检索,匹配到article内li标签且li标签id属性为target
page.locator("article li#target")
```
## css配合布局进行选择
- selector:right-of(inner_selector),与内部选择器匹配的元素的左侧垂直位置（是的,不局限于左侧水平位置)再去与外部选择器匹配
- :left-of,
- :above,
- :below,
- :near,


