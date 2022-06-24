## json-server
1. 切换至项目目录，安装：npm install json-server --save -dev
2. 在项目根目录下创建mock目录
3. mock目录下新增db.json,模拟一些数据
4. 在项目的package.json中的scripts里新增一条命令："json-mock":"json-server mock/db.json"
5. 启动json-server生成接口,切换至项目目录,npm run json-mock,如4设置,该命令实际是去根据自己模拟的mock/db.json启动json-server

## 搭配faker
1. 切换至项目目录，安装：npm install @faker-js/faker --save-dev
2. 刚刚我们模拟了一个db.json,但是自己造不如faker造,继续在mock目录下新增一个db.js文件
3. 在db.js文件中，首先引入faker，const { faker } = require("@faker-js/faker")
4. 然后构建数据形如:module.exports = () => {return {list:[{name:faker.name.findName(),email:faker.internet.email()}],profile:{phone:faker.phone.imei()}}
5. 返回项目中package.json将json-mock命令修改为基于db.js启动json-server即："json-mock":"json-server mock/db.js"


## 注意
1. 构建的数据的数据类型，如list数据是列表形式，而profile不是
2. 所以axios在不同的接口获取数据可能一个写做data.data[0].name,一个写做data.data.phone
