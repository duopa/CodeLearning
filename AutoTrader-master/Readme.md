# VNPY_FXDAYU

## 简介

    基于官方版VNPY修改的适用于Python 3.6 开发环境的开源量化交易程序开发框架，当前用于数字货币的策略研究和实盘交易。
    已经可以使用的数字货币交易所有 OKEX， 火币HUOBI，币安BINANCE，其他交易所功能陆续开通中。
    项目增加了多策略和多品种持仓、订单的存储和查询，优化回测引擎，帮助用户更好地制定策略。
## 项目安装（WINDOWS）：

    1、此版本VNPY基于python3.6开发，建议安装ANACONDA3_5.2.0以上版本
    2、安装MONGODB 4.0
    3、在下载项目的文件夹内找到install.bat，双击即可进入自动安装VNPY_FXDAYU

## 项目使用方法：

实盘：

在下载的文件中，打开example文件夹，按照设置的说明填写配置文件，双击打开 “VNPY - 交易界面.bat” 这个文件，即可进行实盘。
同时，我们为数字货币准备了专用的交易界面Crypto_Trader，同样在example文件夹内，双击打开 “VNPY - 数字货币.bat”这个文件，即可进行实盘。

回测：

1、在MongoDB存入历史数据，范例可在下载的文件内找到loadData文件夹，配置好数据库连接，即可导入提供的数据样本，时间跨度2018年1月1日到1月31日，
    
2、在example文件夹内，有两个和回测有关的配置文件，runBacktesting 是回测，runOptimization 是对回测进行优化。
同样的，提供了运行的快捷方式，双击 “VNPY-回测” 可以进行回测，双击 “VNPY-并行优化” 可以得到优化结果
