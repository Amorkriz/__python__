# 图格公司17^3格式的3D-LUT

lut_.txt是海思生成的表

python文件用来解析海思工具标定产生的结果，生成的excel表前三列为输入RGB，后三列为偏差值

m文件用于读取处理过后的excel（后三列为输出RGB)

sc是拍摄得到的图片，bz是标准图片，用作target来标定
