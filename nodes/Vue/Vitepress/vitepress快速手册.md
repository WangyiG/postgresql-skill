# Vitepress
## 简介
用于创建静态文档站点,你现在阅读的整个文档完全由vitepress完成

## 安装
1.创建项目目录并进入
```sh
mkdir vitepress-starter && cd vitepress-starter
```
2.初始化项目
如果没有yarn,先安装yarn
```sh
npm install -g yarn
```
执行初始化
```sh
yarn init
```
3.安装vitepress
将依赖vue一并安装
```sh
yarn add --dev vitepress vue
```
4.创建文档目录docs与入口文档index.md,以后我们的文档将全部存放在docs目录下
```sh
mkdir docs && echo '# Hello VitePress' > docs/index.md
```
5.在package.json中添加脚本
```json
{
  "scripts": {
    "docs:dev": "vitepress dev docs",
    "docs:build": "vitepress build docs",
    "docs:serve": "vitepress serve docs"
  },
}
```
6.启动文档站点
```sh
// docs:dev是我们刚刚添加的启动脚本,实际运行的是vitepress dev docs启动命令
yarn docs:dev
```
## 配置vitepress
1.新增.vitepress目录新建styles目录创建config.js文件

项目结构如下：
```sh
.
├─ docs
│  ├─ .vitepress
│  │  └─ config.js
│  └─ index.md
└─ package.json
```
2.由于接下来要使用一些静态图片图表等,我们在docs目录下新建一个public目录用于存放我们的一些静态资源
```sh
cd docs && mkdir public
```
3.配置标签头
>不知道什么是标签头?想一想html头中的title
在config.js中
```js
export default {
    title : 'MangTi',
    head : [["link",{rel:'icon',href:'/mt.jpg'}]],
}
```
4.配置主页内容
主页内容都配置在themeConfig选项中
```js
export default {
    title : 'MangTi',
    head : [["link",{rel:'icon',href:'/mt.jpg'}]],
    themeConfig: {
        // 网站标题与logo
        siteTitle: "MangTi's Blog",
        logo: '/mt.jpg',
        // 导航栏
        nav : [
            {text:'Python',link:'/Python/',activeMatch:'/Python/'},           
        ],
        // 侧边栏
        sidebar : {
            '/Python/' : [
                {
                    text : 'Python基础',
                    collapsible : true,
                    collapsed : false,
                    items : [
                        {text:'数据结构',link:'/Python/数据结构'},
                    ]
                }
            ],
        },
        // 社交链接
        socialLinks: [
            { icon: 'github', link: 'https://github.com/vuejs/vitepress' },
        ],
        // 底部文档主体信息
        footer: {
            message: 'Released under the MIT License.',
            copyright: 'Copyright © 2019-present Evan You'
        },
        // 更新信息
        lastUpdatedText: 'Updated Date'
    }
}
```

## 重新配置文档入口index.md
使用home布局
```md
---
layout : home

hero :
    name : MangTi's Blog
    // 描述
    text : Python & Postgre & Vue
    // 详情
    tagline : 不系统但正经的姿势,内有泡妞秘籍
    // 链接按钮
    actions :
    - theme : brand
      text : Get Started
      link : /Postgre/
    - theme : brand
      text : View Github
      link : https://vitepress.vuejs.org/

// 展示项      
features:
    - icon : 🖖
      title : Python
      details : 人生苦短,我用Python！Py+Pandas+Peewee+Django
    - icon : 🛠️
      title : Postgre
      details : Postgresql简单而高效的选择！Syntax+PL/pgsql+Triggers
    - icon : ⚡️
      title : Vue
      details : Vue全家桶YYDS！Vue3+Pinia+Antdesign+Echarts
    
---
```
