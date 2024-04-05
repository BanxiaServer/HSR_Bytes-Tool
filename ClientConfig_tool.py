import re
import os
# 定义变量
ChannelName = "by亡灵暴龙大帝" # OverSeaLive Customizable 可以随意更改
BundleIdentifier = "只因你太美"  # com.HoYoverse.hkrpgoversea Customizable 可以随意更改
ProductName = "What can I say?"  # Star Rail Customizable 可以随意更改
ScriptDefines = "Mamba out"  # OVERSEA_BUILD Customizable 可以随意更改

GlobalDispatchUrlList = "http://your_url.com:666"

TEXTS = [
    ChannelName,
    BundleIdentifier,
    ProductName,
    ScriptDefines,
    GlobalDispatchUrlList + "/query_dispatch"
]

def generate_ClientConfig_bytes(texts):
    # Prepare a byte array to store the entire file content 准备用于存储整个文件内容的字节数组
    file_content = bytearray()

    # Add 00 separators at the beginning of the file 添加文件开头的00间隔
    file_content.extend(bytearray.fromhex("00"))

    # For each string 对于每个字符串
    for index, text in enumerate(texts):
        if index > 0:
            if index == 4:
                # 对于第四个字符串，添加特定的字节表示两个IP地址
                file_content.extend(bytearray.fromhex("0000000100"))
            else:
                # 对于其他字符串，添加普通的00间隔
                file_content.extend(bytearray.fromhex("00"))

        # Calculate the number of bytes after UTF-8 encoding and convert it to hexadecimal
        # 计算UTF-8编码后的字节数量并转换为十六进制
        byte_count = len(text.encode("utf-8"))
        byte_count_hex = hex(byte_count)[2:].zfill(2)

        # Add the hexadecimal representation of byte count as leading byte
        # 添加字节数量的十六进制表示作为前导字节
        file_content.append(int(byte_count_hex, 16))

        # Construct data content 构造数据内容
        content = bytearray()
        content.extend(text.encode("utf-8"))

        # Append data content to file content 将数据内容添加到文件内容中
        file_content.extend(content)

    # Add 16 hexadecimal '00's at the end of the file 在文件末尾添加16个十六进制的'00'
    file_content.extend(bytearray.fromhex("00" * 16))

    # Write to fil 写入文件
    output_dir = "output"  # 输出目录
    output_path = os.path.join(output_dir, "ClientConfig.bytes")  # 输出文件路径

    os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在
    with open(output_path, "wb") as f:
        f.write(file_content)

    print("\nClientConfig.bytes_success")


def modify_json():
    url_regex = re.compile(r'(https?://)([\w.-]+)(:[0-9]+)?')

    try:
        with open('input/server_env_config.json', 'r') as file:  # 输入文件路径
            file_content = file.read()
    except FileNotFoundError:
        print("File 'input/server_env_config.json' not found.")
        return

    updated_content_str = url_regex.sub(GlobalDispatchUrlList, file_content)

    output_dir = "output"  # 输出目录
    output_path = os.path.join(output_dir, "server_env_config.json")  # 输出文件路径

    os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在
    try:
        with open(output_path, 'w') as file:
            file.write(updated_content_str)
            print("server_env_config.json_success")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    generate_ClientConfig_bytes(TEXTS)
    modify_json()