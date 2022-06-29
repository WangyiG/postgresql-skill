## 安装
在全局环境下安装tsc命令
```sh
npm install -g typescript
```

## 编译
编写一个hello.ts文件
- 正常以.ts为后缀
- 但编写react时以tsx为后缀
```ts
console.log('hello,ts')
```
在ts文件所在目录下执行
```sh
tsc hello.ts
```
会编译出一个同名的js文件hello.js

## 类型声明
在ts中使用冒号：来指定变量类型,冒号前后有无空格不影响
ts的的精髓就在于类型声明后得到的ide类型提示推导
```ts
function sayhello(person:string){
    return 'hello,'+person
}

let user = 'Tom';

console.log(sayhello(user));
```
执行tsc命令编译
```sh
tsc hello.ts
```
编译得到一个同名js文件,执行node命令运行该js文件
```sh
node hello.js // 返回hello,Tom
```
ts会在编译时就进行类型检查,既然编译不过,自然不能运行,实际情况是诸如以下代码虽然编译报错,但还是生成了一个同名js文件
```ts
// 学习一下js中的raise Error 语法 : throw new Error()
function sayhello(person:string){
    if (typeof person === 'string'){
        return 'hello,' + person
    }else {
        // return  'person is not a string'
        throw new Error('person is not a string')
    }
}

let user0 = 'Tom';
let user1 = 1;

console.log(sayhello(user0));
console.log(sayhello(user1));
```
>如果需要在ts编译报错时终止js文件的生成,可以在tsconfig.json中配置onEmitOnError

## 配置WebStorm非命令行运行
1.安装ts—node
```sh
npm install -D ts-node
```
2.安装Run Configuration for TypeScript插件
3.右键使用run 

