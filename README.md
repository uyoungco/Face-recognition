# Face-recognition
人脸识别认证 imooc java课程搭配使用

安装face_recognition比较麻烦建议使用docker 下面已经准备好了 cv工程师准备好了吗

### 1.1行构建

```shell
$ docker build -t [镜像名称] .

$ docker run -d -p 3000:3000 --name [容器名称] [镜像名称]
```

### 1.2拉取镜像

```shell
$ docker pull registry.cn-shanghai.aliyuncs.com/uyoung/face_recognition:latest

$ cker run -d -p 3000:3000 --name [容器名称] registry.cn-shanghai.aliyuncs.com/uyoung/face_recognition:latest
```

### 2.食用方法

1. 创建模型接口

   ["POST", "GET"]

   http://localhost:3000/create_face_model
   
   直接访问是调试页面 可以通过此页面上传图片进行测试

2. 识别与认证接口
   ["POST", "GET"]

   http://localhost:3000/checkin

   直接访问是调试页面

