用于hsr安卓端连接到不同服务器的地址<br><br>
要使客户端链接到服务器需要修改两个文件:
- ClientConfig.bytes
- server_env_config.json


先打开HSR_Bytes-Tool.py 把http://your_url.com:666改为目标服务器地址 然后运行它 你就可以得到ClientConfig.bytes

再打开本仓库的server_env_config.json 将文件内所有的http://your_url.com:666字符替换为目标服务器地址

最后 把这两个文件放在apk/assets路径内 替换已有文件即可<br>

---

Here is the translation in English using ChatGPT:

This is used for connecting the HSR Android client to different server addresses.<br>

To make the client connect to a server, you need to modify two files:
- ClientConfig.bytes
- server_env_config.json


First, open HSR_Bytes-Tool.py. Replace "http://your_url.com:666" with the target server address. Then run it to get ClientConfig.bytes.

Next, open the server_env_config.json file in this repository. Replace all instances of "http://your_url.com:666" with the target server address.

Finally, place these two files in the apk/assets directory, replacing the existing files.
