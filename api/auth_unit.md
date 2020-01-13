# auth_unit

**用户认证API**

### 接口列表

- root_login
- login
- logout
- stayalive
- get_login_info

### 接口功能

- root_login

    | 接口        | 请求方式 | 数据格式 |
    | ----------- | -------- | -------- |
    | /root_login | post     | json     |

    📘功能：针对单独的root超级管理员用户的认证，超级管理员拥有最高的权限可以控制其他的admin

    📌请求格式：

    ```json
    {
        "user": "root",
        "pass": "123456"
    }
    ```

    🌍响应格式

    ```json
    {
    	"status": 1,
        "user": "root",
        "token": ""
    }
    ```


- login

    | 接口   | 请求方式 | 数据格式 |
    | ------ | -------- | -------- |
    | /login | post     | json     |

    📘功能：针对管理员用户的认证

    📌请求格式：

    ```json
    {
        "user": "admin1",
        "pass": "123456"
    }
    ```

    🌍响应格式

    ```json
    {
    	"status": 1,
        "user": "admin",
        "token": ""
    }
    ```

- logout

    | 接口    | 请求方式 | 数据格式 |
    | ------- | -------- | -------- |
    | /logout | post     | json     |

    📘功能：用户的登出，返回信息清空保存的token信息

    📌请求格式：

    ```json
    {}
    ```

    🌍响应格式

    ```json
    {
    	"islogged": false,
    }
    ```

- stayalive

    | 接口      | 请求方式 | 数据格式 |
    | --------- | -------- | -------- |
    | /staylive | post     | json     |

    📘功能：定时向后端的硬件平台发送保持连接，用于保持与硬件的连线

    📌请求格式：

    ```json
    {
        "user": "root",
        "pass": "123456"
    }
    ```

    🌍响应格式

    ```json
    {
    	isalive":"yes"
    }
    ```

- get_login_info

    | 接口            | 请求方式 | 数据格式 |
    | --------------- | -------- | -------- |
    | /get_login_info | get      | json     |

    📘功能：询问后台当前登录的用户信息

    📌请求格式：

    ```json
    仅需在header里包含token
    ```

    🌍响应格式

    ```json
    {
    	"user":'root'
    }
    ```







