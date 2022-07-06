# Selectors选择器
- 选择器Selectors是用于创建定位器Locators的字符串
- 定位器Locators用于定位元素,确定元素是who之后才能执行相应操作
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
