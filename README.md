用于hsr安卓端连接到不同服务器的地址<br>
要使客户端链接到服务器需要修改两个文件<br>
`
ClientConfig.bytes
`
`
server_env_config.json
`
<br><br>
安装python是必须的
<br><br>
先打开HSR_Bytes-Tool.py 把http://your_url.com:666改为目标服务器地址 然后运行它 你就可以得到ClientConfig.bytes<br>
再打开本仓库的server_env_config.json 将文件内所有的http://your_url.com:666字符替换为目标服务器地址<br>
最后 把这两个文件放在apk/assets路径内 替换已有文件即可
