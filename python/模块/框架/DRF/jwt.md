## 前情
#### cookie、session、token区别的浅薄理解
##### cookie
  - 业务逻辑:登录后服务端生成cookie返回给浏览器,浏览器再次请求时携带cookie,服务端验证cookie
  - 临时或永久保存在客户端
  - 既可以记录用户信息也可以记录商品信息
  - 服务器需要维护一张cookie表
  
##### session
  - 业务逻辑:登录后服务端生成session,将sessionid给cookie返回给浏览器,浏览器再次请求时携带cookie,服务端根据cookie中的sessionid去找session
  - 临时保存在服务端
  - sessionid通过cookie给到浏览器
  - 此时cookie只需要去记录用户信息(大大减少了cookie的体积),请求时将cookie传给服务端后,在服务端中关联用户的商品信息
  - 服务器需要维护一张session表

##### token
  - 业务逻辑:登录后服务端根据算法生成一个token,通过cookie返回给浏览器,浏览器再次请求时携带含token的cookie,服务端验证token并直接取出用户id
  - token的三段式组成:header-指定签名算法等通用信息;payload-指定用户id,过期时间等非敏感数据;Signature-签名,server根据header的签名算法与服务端的密钥对head+payload生成签名
  - 服务端不需要维护token表,只需要维护一个token函数,作用是检验请求携带的token是否合法以及返回用户id去得到用户id对应的商品信息
  
###### 优缺点
  - cookie:cookie跨站是不能共享的,很难实现单点登录(在多个应用系统中,用户只需要登录一次就可以访问所有相互信任的应用系统,如微信登录)
  - session:负载均衡需要在每台机器上复制session, session粘连一台机器,无法解决宕机问题,session共享需要搭建redis集群,总之就是资源开销高
  - token:扩展性较高,但是token一旦生成必须等其过期失效,无法指定失效(发现问题也只能眼睁睁等过期),更适合一次性的命令认证,设置一个比较短的有效期
  - session和token都是对用户身份的认证机制,一个保存在server通过在redis等中间件获取来校验,一个保存在client,通过签名校验的方式来校验
