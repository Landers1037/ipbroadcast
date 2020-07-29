import Mock from 'mockjs'
//登录相关
const login = {
    "status": 1,
    "user": "root",
    "token": "123456"
};

//当前用户信息
const user_info = {
    "id": 0,
    "name": "root",
    "type": "root",
    "m": "",
    "pw": "123456",
    "ml": "utm",
    "tl": "3"
};

const user_list = [
    {
        "id": 0,
        "name": "root",
        "type": "root",
        "pw": "123456",
        "ml": "utm",
        "tl": "3"
    },
    {
        "id": 1,
        "name": "user1",
        "type": "root",
        "pw": "123456",
        "ml": "u",
        "tl": "1"
    },
    {
        "id": 2,
        "name": "user2",
        "type": "root",
        "pw": "123456",
        "ml": "um",
        "tl": "1"
    },
];
//登录IP广播验证
const ip = {
    "status": true
};
//终端测试
const media = {
    'rows|10':[{
        "id|+1": 100,
        "type|13-20": 13,
        "name": "101",
        "status|0-1": 0,
        "volume|0-100": 70,
        "power|0-1": 0,
        "ip": "192.168.1.102"
    }]
};

//任务列表
const tasklist = [{
   "id": 1,
   "name": "测试任务",
   "en": 1,
   "exe": 0,
    "mode": 0,
    "type": 1,
    "terminals": [101,102]

}];
Mock.setup({
    timeout: '300-1000'
});

Mock.mock('/api/root_login','post',login);
Mock.mock('/api/login','post',login);
Mock.mock('/api/keepalive','post',ip);
Mock.mock('/api/get_user_info','post',user_info);
Mock.mock('/api/get_user_list','post',user_list);
Mock.mock('/api/get_user','post',user_info);
Mock.mock('/api/get_terminal_list','post',Mock.mock(media).rows);
Mock.mock('/api/get_task_list','post',tasklist)

export default Mock