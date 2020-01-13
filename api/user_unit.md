# user_unit

**用户 控制API**

### 接口列表

- get_user_list
- get_user
- add_user
- update_user
- delete_user

### 接口功能

- get_user_list

    | 接口           | 请求方式 | 数据格式 |
    | -------------- | -------- | -------- |
    | /get_user_list | get      | json     |

    📘功能：获取服务器上的全部用户列表

    📌请求格式：

    ```json
    携带token认证信息
    ```
    
    🌍响应格式
    ```json
        {
        userlist
        }
    ```

- get_user

    | 接口           | 请求方式 | 数据格式 |
    | -------------- | -------- | -------- |
    | /get_user+<id> | get      | json     |

    📘功能：获取某一个id的用户信息

    📌请求格式：

    ```json
    请求地址中指定<id>
    ```
    
    🌍响应格式
    ```json
        {
        user
        }
    ```

- add_user

    | 接口      | 请求方式 | 数据格式 |
    | --------- | -------- | -------- |
    | /add_user | post     | json     |

    📘功能：创建新用户

    📌请求格式：

    ```json
    {
        userdata
    }
    ```

    🌍响应格式

    ```json
    {
    	"user_added": "yes",
    }
    ```

- update_user

    | 接口              | 请求方式 | 数据格式 |
    | ----------------- | -------- | -------- |
    | /update_user+<id> | post     | json     |

    📘功能：更新用户数据

    📌请求格式：

    ```json
    {
        userdata
    }
    ```

    🌍响应格式

    ```json
        {
            user_up":"yes"
        }
    ```

- delete_user

    | 接口              | 请求方式 | 数据格式 |
    | ----------------- | -------- | -------- |
    | /delete_user+<id> | post     | json     |

    📘功能： 删除指定id用户

    📌请求格式：

    ```json
    仅需在header里包含token
    ```

    🌍响应格式

    ```json
    {
    	"user_del":'yes'
    }
    ```







