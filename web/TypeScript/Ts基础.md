## 数据类型
1. 原始数据类型
  - boolean
  - number
  - string
  - null 数据类型为object,转换为数值时为0
  - undefined 数据类型为undefined,转换为数值时为NaN
  - Symbol，表示独一无二的值,通过Symbol()生成,Symbol('foo') === Symbol('foo')是false
  - BigInt
2. 任意值any
  - 允许调用任何属性,任何方法
  - 返回的内容类型也为any
  - 变量声明时未指定类型,则默认为any任意值类型
3. 类型推论
  - 正常变量声明时未指定类型，默认为any任意类型
  - 但赋值为原始数据类型后，会推论该变量为对应原始数据类型
  - 此时再赋值为新类型则会报错
4. 联合类型
  - 使用 | 分隔每个类型
  - 只能访问联合类型共有的属性或方法
  - 比如string | number,可以访问共有属性toString()但不能访问length,因为number类型没有length属性

## 对象的类型——接口
- 使用接口（Interfaces）来定义对象的类型
- 接口（Interfaces）是一个很重要的概念，除了可用于对类的一部分行为进行抽象以外，也常用于对「对象的形状（Shape）」进行描述

1.简单的例子

  
