用于HSR安卓端连接到不同服务器的地址<br><br>
要使客户端链接到服务器需要修改两个文件:
- ClientConfig.bytes
- server_env_config.json


先打开HSR_Bytes-Tool.py 把 GlobalDispatchUrlList 改为目标服务器地址 然后运行它 你就可以在output文件夹内得到ClientConfig.bytes和server_env_config.json
- server_env_config.json来自input文件夹内 你可以使用官方apk/assetc内的文件替换 但是一般没有这么做的必要

最后 把这两个文件放在apk/assets路径内 替换已有文件即可<br>

BinaryVersion_tool.py可以用于修改客户端左下角显示的版本号 修改它没有什么实际意义

---

Here is the translation in English using ChatGPT:

Used for HSR Android client to connect to different server addresses.

To make the client connect to the server, you need to modify two files:
- ClientConfig.bytes
- server_env_config.json

First, open HSR_Bytes-Tool.py and change GlobalDispatchUrlList to the address of the target server. Then run it, and you will get ClientConfig.bytes and server_env_config.json in the output folder.

- The server_env_config.json comes from the input folder. You can use files from the official apk/assets folder to replace it, but generally, there is no need to do so.

Finally, place these two files in the apk/assets path, replacing the existing files.
