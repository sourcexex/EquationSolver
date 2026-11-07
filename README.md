# EquationSolver

<div align="center">

<img src="src/resources/logo.ico" width="30%" alt="Uartis logo">

[![Release](https://img.shields.io/github/v/release/sourcexex/uartis)](https://github.com/sourcexex/equationsolver/releases/latest)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3776AB)](https://www.python.org/)


</div>

## 关于
你是否会因为解不出方程而恼怒，这个程序可以解决你的问题  

本程序使用 `sympy` 和 `PySide6` 开发  

如果发现bug或有修改建议可以在[作者的B站](https://space.bilibili.com/3461569679722999?spm_id_from=333.337.0.0)或在上方 issues 页面反馈

## 下载与安装
### GitHub 下载
请点击右侧 `Releases` 打开下载页面，并选择最新版本  

本软件提供两种方式，安装包和压缩包(绿色版)  

Windows 请使用 `.exe` 结尾的安装包
### 网盘下载
如果GitHub下载不了请使用网盘下载  
> [!NOTE]
> 
> 网盘安装包不保证为最新版

安装包(exe): [点我下载](https://wwbiu.lanzouv.com/iiDWN3hlsaoj)， 密码: 1234  

压缩包(zip): [点我下载](https://wwbiu.lanzouv.com/iCPtd3hls9aj)， 密码: 1234
## 使用
方程组中间用 `,` 分割，如：x+y=10,x-y=2  

乘方使用 `^` 或 `**`  

点击工具栏的求解按钮或 文件>求解 进行求解

点击工具栏的清除按钮或 文件>清除 可以清除所有

其他函数见 关于>帮助 

## 开发
本程序使用 Python 3.13 作为 Python 版本，UV 作为管理工具

使用以下命令安装依赖

```bash
uv sync
```