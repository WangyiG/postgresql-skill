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

1. 简单的例子,定义接口Person(接口一般约定首字母大写),定义变量tom类型是Person约束了tom的形状必须和接口Person一致
```ts
interface Person {
    name: string;
    age: number;
}

let tom: Person = {
    name: 'Tom',
    age: 25
};
```

2. 使用 ？定义可选属性,可选属性可以不选，但不能增加属性
```ts
interface Person {
    name: string;
    age?: number;
}

let tom: Person = {
    name: 'Tom'
};
```

3. 使用 [propName: string]: any; 来定义任意属性,可增不可减,另外需要注意任意属性指定的数据类型需要是确定属性与可选属性的超集
```ts
interface Person {
    name: string;
    age?: number;
    // 一定要是超集
    [propName: string]: string | number;
}

let tom: Person = {
    name: 'Tom',
    age: 25,
    gender: 'male'
};
```
4. 使用 readonly 定义只读属性,只读属性同样需要初始化,初始化之后不可再赋值
```ts
interface Person {
    readonly id: number;
    name: string;
    age?: number;
    [propName: string]: any;
}

let tom: Person = {
    // 这里id初始化不能少
    id: 89757,
    name: 'Tom',
    gender: 'male'
};

// 不可赋值tom.id = 9527;
```
## 数组类型
>数组的一些方法的参数会根据数组在定义时约定的类型受到限制
1. 使用原始类型+[]和数组泛型Array+<>,来约束数组内的元素类型
```ts
let fibonacci: number[] = [1, 1, 2, 3, 5];

let list: any[] = ['xcatliu', 25, { website: 'http://xcatliu.com' }];

let arr:Array<any> = [1,'a',[1,2],{'name':'张三',age:18}];
```

2. 类数组,比如arguments
- 每一个函数都会有一个Arguments对象实例arguments，它引用着函数的实参
- 可以用数组下标的方式" [ ] "引用arguments的元素
- arguments.length为函数实参个数
- arguments.callee引用函数自身
- 常用的类数组都有自己的接口定义，如 IArguments, NodeList, HTMLCollection等
其中 IArguments 是 TypeScript 中定义好了的类型，它实际上是一个接口数组：
```ts
interface IArguments {
    [index: number]: any;
    length: number;
    callee: Function;
}
```
约束当索引的类型是number时，值的类型any任意值，也约束了它还有 length 和 callee 两个属性
```ts
function saygood(text: string): string {
        let args: IArguments = arguments
        console.log(args.length, args[0])
        return 'good,' + text
}

console.log(saygood('job'))
```














