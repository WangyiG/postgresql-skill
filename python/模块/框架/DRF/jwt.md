## 前情
### cookie、session、token区别的浅薄理解
#### cookie

  1. 业务逻辑:登录后服务端生成cookie返回给浏览器,浏览器再次请求时携带cookie,服务端验证cookie
  2. 临时或永久保存在客户端
  3. 既可以记录用户信息也可以记录商品信息
  4. 服务器需要维护一张cookie表
  
#### session

  1. 业务逻辑:登录后服务端生成session,将sessionid给cookie返回给浏览器,浏览器再次请求时携带含sessionid的cookie,服务端根据验证sessionid
  2. 临时保存在服务端
  3. sessionid通过cookie给到浏览器
  4. 此时cookie只需要去记录用户信息(大大减少了cookie的体积),请求时将cookie传给服务端后,在服务端中关联用户的商品信息
  5. 服务器需要维护一张session表

#### token
计算代替存储
  1. 业务逻辑:登录后服务端根据算法生成一个token,通过cookie返回给浏览器,浏览器再次请求时携带含token的cookie,服务端验证token
  2. json web token的三段式组成:
     - header:头,指定签名算法等通用信息
     - payload:荷载,指定用户id,过期时间等非敏感关键数据;
     - Signature:签名,server根据header的签名算法与服务端的密钥对head+payload加密生成签名
  3. 服务端不需要维护token表,只需要维护一个token函数,作用是检验请求携带的token是否合法以及返回用户id去得到用户id对应的商品信息
  
#### 优缺点

  1. cookie:cookie跨站是不能共享的,很难实现单点登录(在多个应用系统中,用户只需要登录一次就可以访问所有相互信任的应用系统,如微信登录)
  2. session:负载均衡需要在每台机器上复制session, session粘连一台机器,无法解决宕机问题,session共享需要搭建redis集群,总之就是资源开销高
  3. token:扩展性较高,但是token一旦生成必须等其过期失效,无法指定失效(发现问题也只能眼睁睁等过期),更适合一次性的命令认证,设置一个比较短的有效期
  4. session和token都是对用户身份的认证机制,一个保存在server通过在redis等中间件获取来校验,一个保存在client,通过签名校验的方式来校验

## jwt
- json web token
- base64编解码,二进制,字符串长度为4的倍数,不足部分补=
- 除了字符数据使用base64编码,有些图片也使用base64编码
```py
import base64
d = '{"name":"mt","age":28}'

# 编码
res = base64.b64encode(d.encode('utf-8'))
res                                        
# 返回2进制字符串:b'eyJuYW1lIjoibXQiLCJhZ2UiOjE4fQ=='

# 解码
import json
json.loads(base64.b64decode(res)),base64.b64decode(res)#.decode('utf-8')   
# 返回:({'name': 'mt', 'age': 18}, b'{"name":"mt","age":18}')
```
#### jwt签发与认证
1. 签发
  - 将通用信息存储成json格式字符串,采用base64编码得到头字符串
  - 将关键信息存储成json格式字符串,采用base64编码得到荷载字符串
  - 将头与荷载通过加密算法与密钥,采用base64编码得到签名字符串

  
2. 认证
  - 将token根据.拆分成3段字符串
  - 第一段为头,一般不做处理
  - 第二段为荷载,主要操作有:提取关键信息,通过关键信息关联到user表,验证过期时间是否合法等
  - 将头与荷载采用维护的加密算法与密钥得到一个base64字符串,与第三段签名字符串对比,判断token是否合法

#### 在Django中配置jwt
- 安装:pip install djangorestframework-jwt(或另一个djangorestframework-simplejwt)
- Django中快速签发
```py
# 配置子路由
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    ...,
    path('tokens/', obtain_jwt_token),
]

```
```sh
// 创建一个超级用户mt密码也为mt,基于auth_user表测试jwt
python manage.py createsuperuser

// 测试地址,post请求传入username与password 都为mt,验证是否返回了一个token
http://127.0.0.1:8000/filter_app/tokens/
```
```py
# 解析一下荷载看看过期时间
import base64
imprt arrow

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im10IiwiZXhwIjoxNjU4MTU4NjA1LCJlbWFpbCI6IiJ9.INBbk97HUrqB3gJEyk1Pm-VhjOKxPPncIOEGRVmroRg"

# 注意可能需要加=补齐荷载
base64.b64decode(b'eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im10IiwiZXhwIjoxNjU4MTU4NjA1LCJlbWFpbCI6IiJ9') # 其中exp即为过期时间

arrow.get(1658158605).to('Asia/Shanghai') # 或to('local')                                         # 实测默认过期时间为1天

```
#### jwt认证的快速使用
- 视图类中配置认证类与权限类(必须都配置)
```py
from .models import Book
from .serializer import BookSerializer
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BookView1(ViewSetMixin, ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # 指定排序类,分页只能使用一种方式,不再接收列表多模式指定
    # jwt内置认证类
    authentication_classes = [JSONWebTokenAuthentication, ]
    # jwt必须搭配该权限类
    permission_classes = [IsAuthenticated, ]

```
- 接口测试:注意**要在Headers中**传参,key是**Authorization**，value是**jwt+空格+登陆返回的token串**
```sh
// 接口地址,注意是在Headers中传参
http://127.0.0.1:8000/filter_app/books1/
```
#### 定制jwt的返回格式
- 新建utils.py,改写一个jwt返回函数
```py
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'code': 100,
        'msg': '登陆成功',
        'token': token,
        'username': user.username
    }
```
- 在setting中配置改写后的返回函数(修改默认JWT_RESPONSE_PAYLOAD_HANDLER配置)
```py
JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'filter_app.utils.jwt_response_payload_handler',
}
```
- token测试,定制之后已经可以post传参不必headers那么复杂的传参了
```sh
// body中传username:mt password:mt
http://127.0.0.1:8000/filter_app/tokens/
```
#### jwt签发认证源码粗识
```py
# 签发
# 入口:子urls中的obtain_jwt_token
# ObtainJSONWebToken.as_view() -->很明显ObtainJSONWebToken是一个视图(从obtain_jwt_token导入的from也可以看出来)
# ObtainJSONWebToken -->1.继承了一个post方法:需携带username与password访问 2.用到序列化类serializer_class = JSONWebTokenSerializer
# 1.post方法中:response_data = jwt_response_payload_handler(token, user, request)此为默认返回,所以我们改写wt_response_payload_handler
# 2.JSONWebTokenSerializer中validate全局钩子获取当前用户和签发token -->后面自定义user表token参照于此

# 认证
# 入口views下JSONWebTokenAuthentication
# 其父类中重写了authenticate方法
    def authenticate(self, request):
    
        # request可以取出前端传人的数据
        # 还记得之前在Headers中传参value格式是jwt+空格+token串,这里split取出token串
        jwt_value = self.get_jwt_value(request)
        
        # 如果没有传token,即jwt_value为None,直接返回了None跳出了认证
        # 这也是前面为什么认证必须配一个权限类的原因,如果没传token不允许校验,要求必须传token
        if jwt_value is None:
            return None
        
        
        try:
            payload = jwt_decode_handler(jwt_value)          # 验证签名,获取的token签名与根据token头+token荷载+密钥加密算法得到的token签名是否一致
        except jwt.ExpiredSignature:
            msg = _('Signature has expired.')                # token是否过期
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')             # token是否被篡改
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:                        # 其它不知名错误
            raise exceptions.AuthenticationFailed()

        user = self.authenticate_credentials(payload)        # 从荷载中获取用户信息

        return (user, jwt_value)

```






















