import CatchUtil
import argparse
import Logging

# 设置6个参数
# 抓取次数： times, 整型，非必须传入参数，包含默认值6
# 抓取间隔： interval, 整型，非必须传入参数，单位分钟，包含默认值10
# 需要cpu数据的包名列表：cpuProcessNameList, 数组型，非必须传入参数，包含默认值["com.boe.team.e3visualprotect", "camerahalserver", "cameraserver"]
# 需要mem数据的包名列表，memProcessNameList，数组型，非必须传入参数，包含默认值["com.boe.team.e3visualprotect"]

# 构建一个命令行参数解析对象
parser = argparse.ArgumentParser(description='命令行参数')

parser.add_argument('--times', '-t', type=int, help='抓取次数，单位：次，整型，非必须传入参数，包含默认值：6', default=6)
parser.add_argument('--interval', '-i', type=int, help='抓取间隔，单位：分钟，整型，非必须传入参数，包含默认值：10', default=10)
parser.add_argument('--cpuProcessNameList', '-c', type=str, nargs='+', help='需要cpu数据的包名列表，字符串型，包名之间需要空格，非必须传入参数，包含默认值： "com.boe.team.e3visualprotect" "camerahalserver" "cameraserver"', default=["com.boe.team.e3visualprotect","camerahalserver","cameraserver"])
parser.add_argument('--memProcessNameList', '-m', type=str, nargs='+', help='需要mem数据的包名列表，字符串型，包名之间需要空格，非必须传入参数，包含默认值："com.boe.team.e3visualprotect"', default=["com.boe.team.e3visualprotect"])

# 解析参数,获取所有的命令行参数（Namespace），然后转为字典
args = vars(parser.parse_args())

# 获取所有参数
print("所有命令行参数为:")
for key in args:
    Logging.logger.info(f"命令行参数名:{key}，参数值:{args[key]}")

CatchUtil.get_cpu_mem(args['times'], args['interval'], args['cpuProcessNameList'], args['memProcessNameList'])
