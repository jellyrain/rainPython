## 1. rain_auto 自动化包（window， android）

依赖：`opencv-python` `pywin32` `Pillow` `pyautogui`

## 2. encrypt 加密包

依赖：`rsa` `pycryptodome`

## 3. bot QQ 机器人包

依赖：go-cqhttp（自行登录账号 非 python 库）`sqlite3` `requests` `flask`

## 4. content 内容包（大部分文件都可以单独使用）

随机、id 生成、文件监听、文件操作、词法分析、excel 操作

词法分析 依赖：`fuzzywuzzy`

excel 操作 依赖：`openpyxl` 词法分析的依赖

## 5. sql_faker 假数据包

依赖：`faker` 内容包的随机`prizes`文件（内置且也暴露方法）

## 6. sql_parse 数据库 连接、格式化、获取语句和血缘 包（当前支持 sql server）

依赖：`sqllineage` `pymssql(sql server 驱动)`

## 7. vacc 视频剪辑和转码包

## 8. timer 定时器包

依赖：`schedule`
