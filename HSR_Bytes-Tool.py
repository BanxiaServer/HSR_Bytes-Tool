TEXTS = [
    "by亡灵暴龙大帝",  # OverSeaLive Customizable 可以随意更改
    "只因你太美",  # com.HoYoverse.hkrpgoversea Customizable 可以随意更改
    "What can I say?",  # Star Rail Customizable 可以随意更改
    "Mamba out",  # OVERSEA_BUILD Customizable 可以随意更改

    # Modify the first half to the server address 修改前半部分内容为服务器地址
    "http://your_url.com:666" + "/query_dispatch"
]

def generate_file_with_length(texts):
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

    # Write to file 写入文件
    with open("ClientConfig.bytes", "wb") as f:
        f.write(file_content)

    print("文件生成成功。success")

if __name__ == "__main__":
    generate_file_with_length(TEXTS)
