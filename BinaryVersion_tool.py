import os

# Variables
# 2.1 OS Android
Branch = "V2.1Live"
Revision = 6689754
MajorVersion = 2
MinorVersion = 1
PatchVersion = 0
AssetBundleMajorVersion = 0
AssetBundleMinorVersion = 0
AssetBundlePatchVersion = 6689754
DesignDataBundleMajorVersion = 0
DesignDataBundleMinorVersion = 0
DesignDataBundlePatchVersion = 6689754
LuaBundleMajorVersion = 0
LuaBundleMinorVersion = 0
LuaBundlePatchVersion = 6689750
AudioBundleMajorVersion = 0
AudioBundleMinorVersion = 0
AudioBundlePatchVersion = 6689754
VideoBundleMajorVersion = 0
VideoBundleMinorVersion = 0
VideoBundlePatchVersion = 6689754
Time = "20240320-1126"
PakType = "PROD" # PROD BETA GM CECREAEATION
PakTypeDetail = ""
SubPakInlcudeAssetType = "StartAsset"
SubPakInlcudeDesignDataType = "StartDesignData"
DispatchSeed = "bba67d093e"
BuildId = "20240320-1126-V2.1Live-6689754-OSPRODAndroid2.1.0-OSLive-aab-icon"
AppIdentity = "0ccc11c5e66a11ee8ef7da26e0554e04"
GameCoreVersion = 6688752
IsEnableExcludeAsset = True
Sdk_PS_Client_Id = ""



def variable_to_hex(variable):
    if isinstance(variable, str):
        length_byte = len(variable).to_bytes(1, byteorder='big').hex()
        return "00" + length_byte + ''.join(format(ord(char), '02x') for char in variable)
    elif isinstance(variable, bool):
        return "01" if variable else "00"  # Encode boolean as 01 for True, 00 for False
    elif isinstance(variable, int):
        return variable.to_bytes(4, byteorder='big').hex()
    else:
        raise ValueError("Unsupported variable type")

# Convert variables to hexadecimal
variables = [
    Branch, Revision, MajorVersion, MinorVersion, PatchVersion,
    AssetBundleMajorVersion, AssetBundleMinorVersion, AssetBundlePatchVersion,
    DesignDataBundleMajorVersion, DesignDataBundleMinorVersion, DesignDataBundlePatchVersion,
    LuaBundleMajorVersion, LuaBundleMinorVersion, LuaBundlePatchVersion,
    AudioBundleMajorVersion, AudioBundleMinorVersion, AudioBundlePatchVersion,
    VideoBundleMajorVersion, VideoBundleMinorVersion, VideoBundlePatchVersion,
    Time, PakType, PakTypeDetail, SubPakInlcudeAssetType, SubPakInlcudeDesignDataType,
    DispatchSeed, BuildId, AppIdentity, GameCoreVersion, IsEnableExcludeAsset, Sdk_PS_Client_Id
]
# Convert variables to hexadecimal
variables_hex = [variable_to_hex(var) for var in variables]

# Write to fil 写入文件
output_dir = "output"  # 输出目录
output_path = os.path.join(output_dir, "BinaryVersion.bytes")

os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在
# Write to file
with open(output_path, 'wb') as f:
    for var_hex in variables_hex:
        f.write(bytes.fromhex(var_hex))

print("\nBinaryVersion.bytes_success")



'''
# 2.1 OS Android
Branch = "V2.1Live"
Revision = 6689754
MajorVersion = 2
MinorVersion = 1
PatchVersion = 0
AssetBundleMajorVersion = 0
AssetBundleMinorVersion = 0
AssetBundlePatchVersion = 6689754
DesignDataBundleMajorVersion = 0
DesignDataBundleMinorVersion = 0
DesignDataBundlePatchVersion = 6689754
LuaBundleMajorVersion = 0
LuaBundleMinorVersion = 0
LuaBundlePatchVersion = 6689750
AudioBundleMajorVersion = 0
AudioBundleMinorVersion = 0
AudioBundlePatchVersion = 6689754
VideoBundleMajorVersion = 0
VideoBundleMinorVersion = 0
VideoBundlePatchVersion = 6689754
Time = "20240320-1126"
PakType = "PROD"
PakTypeDetail = ""
SubPakInlcudeAssetType = "StartAsset"
SubPakInlcudeDesignDataType = "StartDesignData"
DispatchSeed = "bba67d093e"
BuildId = "20240320-1126-V2.1Live-6689754-OSPRODAndroid2.1.0-OSLive-aab-icon"
AppIdentity = "0ccc11c5e66a11ee8ef7da26e0554e04"
GameCoreVersion = 6688752
IsEnableExcludeAsset = True
Sdk_PS_Client_Id = ""
'''