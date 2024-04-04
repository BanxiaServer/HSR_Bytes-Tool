TEXTS = [
    "by亡灵暴龙大帝",
    "com.HoYoverse.hkrpgoversea",#可以随意更改
    "Star Rail",#可以随意更改
    "使用半夏公益服公开文件制作",
    "http://your_url.com:666" + "/query_dispatch"#修改前半部分内容为服务器地址
]

def generate_file_with_length(texts):
    # 准备用于存储整个文件内容的字节数组
    file_content = bytearray()

    # 添加文件开头的00间隔
    file_content.extend(bytearray.fromhex("00"))

    # 对于每个字符串
    for index, text in enumerate(texts):
        # 在每一组字符串前面添加一个十六进制的00间隔
        if index > 0:
            if index == 4:
                file_content.extend(bytearray.fromhex("0000000200"))
            else:
                file_content.extend(bytearray.fromhex("00"))

        # 计算UTF-8编码后的字节数量并转换为十六进制
        byte_count = len(text.encode("utf-8"))
        byte_count_hex = hex(byte_count)[2:].zfill(2)

        # 添加字节数量的十六进制表示作为前导字节
        file_content.append(int(byte_count_hex, 16))

        # 构造数据内容
        content = bytearray()
        content.extend(text.encode("utf-8"))

        # 将数据内容添加到文件内容中
        file_content.extend(content)

    # 写入文件
    with open("ClientConfig.bytes", "wb") as f:
        f.write(file_content)

    print("文件生成成功。")

if __name__ == "__main__":
    generate_file_with_length(TEXTS)
