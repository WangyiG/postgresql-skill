## 前言
在开始之前,先简单了解在vue中的几个概念：
1. attribute,常用于表示html标签中元素标签的属性如:<div style="color:red" title="this is a example">hello friend</div>中的style,title常见的还有click等
2. property,常用于元素对象属性,js中实例初始化的那些属性

## 插值
1. 语法：{{ args }}
2. 示例：<span>Message: {{ msg }}</span>
3. 实现：Mustache(双大括号)标签被实例中的msg属性的值所更新
4. 支持:JavaScript 表达式如：{{ number + 1 }},{{ ok ? 'YES' : 'NO' }},{{ message.split('').reverse().join('') }}
5. 限制：只支持单行表达式

## 指令
1. 概念：带有v-前缀的特殊attribute，如v-on,v-bind,v-if
2. 示例:v-on:click='clickMe',v-bind:title='some text',v-if='seen'
3. 实现:指令attribute的值预期是单个JavaScript表达式,指令的职责是,当表达式的值改变时,将其影响作用于DOM（文档对象模型）
4. 指令的参数:参数在指令名称之后以:连接,如示例中的click,title,不是所有的指令都有参数,如示例中的v-if
5. 动态参数:用方括号包裹,<a v-on:[eventName]="doSomething"> ... </a>,比如这里,动态参数可以是'click'也可以是'fcous'
6. 修饰符:<form v-on:submit.prevent="onSubmit">...</form>,指令对于触发的事件调用event.preventDefault()
