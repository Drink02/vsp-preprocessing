# vsp-preprocessing
存放通用 VSP 地震数据预处理相关脚本，支撑后续速度结构成像与地震成因分析
- train.py：深度学习 VSP 初至波自动拾取脚本，搭配 model_13epoch.pth 预训练模型，输出高精度走时文件
- Trace_Viewer.py：基于 obspy 的 SEGY 格式 VSP 数据可视化工具，用于查看原始地震剖面质量、核对炮点与检波点分布
