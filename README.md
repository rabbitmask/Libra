# Libra 网站安全监测系统

![Version](https://img.shields.io/badge/version-2.53-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

Libra [天秤座] 是一个功能全面的网站安全监测与分析平台，专注于网站篡改、黑链、后门、违规内容、死链等安全威胁的自动化检测。

## 💌 项目更新说明

感谢关注，Libra项目意外收获了近300个Star，这份信任让我深感荣幸。同时也为长期积压的Issues未能及时回复而深表歉意。

**项目历程回顾**

Libra最初诞生于一次应急需求，仅用两天时间快速开发完成的概念验证脚本。由于开发时间紧迫且缺乏充分的架构设计，代码结构和思路确实存在许多不足之处。

随着项目在实际业务中的应用，我们基于大量实战经验对检测引擎进行了深度优化，包括：
- 针对黑帽SEO常用编码技术的专项识别
- 集成主流加解密算法的检测能力

经慎重考虑，现决定将商业版本中的部分核心改进回馈给开源版本。新版本在检测精度、性能表现和代码质量方面都有显著提升，相较于早期的纯正则匹配方案有了质的飞跃。

希望全新的Libra能够为有需求的师傅们提供些许帮助。



## 🌟 核心功能

### 安全检测模块
| 模块 | 重要等级 | 功能描述 |
|------|----------|----------|
| 🔗 黑链检测 | ⭐⭐⭐⭐⭐ | 检测隐藏的恶意外链和SEO黑链 |
| 🚪 后门检测 | ⭐⭐⭐⭐ | 识别Webshell和后门文件 |
| ⚠️ 违规检测 | ⭐⭐⭐⭐ | 检测违法违规内容 |
| 💔 死链检测 | ⭐⭐ | 识别失效链接 |

### 扫描类型
- **HomePage_Scan**: 首页检测 - 快速检测网站首页安全状况
- **SecondPage_Scan**: 二级页面检测 - 深入检测子页面
- **AllSite_Scan**: 全站扫描 - 全面扫描整个网站
- **CustomPage_Scan**: 自定义页面检测 - 指定页面检测

## 🏗️ 项目结构

```
Libra_API/
├── Libra.py                 # 主程序入口
├── Framework/               # 核心框架
│   └── Libra_Console.py    # 命令行控制台
├── Moudle/                  # 业务模块
│   ├── task_console.py     # 任务控制器
│   ├── task_crawler.py     # 爬虫模块
│   ├── task_response.py    # 数据响应处理
│   └── task_rulefind.py    # 规则检测引擎
├── Config/                  # 配置文件
│   ├── config_banner.py    # 程序横幅配置
│   ├── config_crawler.py   # 爬虫配置
│   ├── config_db.py        # 数据库配置
│   ├── config_logging.py   # 日志配置
│   ├── config_proxies.py   # 代理配置
│   └── config_requests.py  # 请求配置
├── ORM/                     # 数据库ORM
│   └── db_rules.py         # 规则数据库操作
├── Tools/                   # 工具库
│   └── tools.py            # 通用工具函数
├── Libra.db                # SQLite数据库
└── requirements.txt        # 依赖包列表
```

## 🚀 快速开始

### 环境要求
- Python 3.6+
- SQLite (内置)

### 安装依赖
```bash
pip install -r requirements.txt
```

### 基本用法

#### 1. 显示帮助信息
```bash
python Libra.py
```

#### 2. 快速检测网站首页
```bash
python Libra.py -u http://example.com
```

#### 3. 指定检测类型
```bash
# 首页检测
python Libra.py -u http://example.com -t HomePage_Scan

# 二级页面检测
python Libra.py -u http://example.com -t SecondPage_Scan

# 全站扫描
python Libra.py -u http://example.com -t AllSite_Scan

# 自定义页面检测
python Libra.py -u http://example.com -t CustomPage_Scan
```

## 📊 检测报告

系统将生成详细的安全检测报告，包括：
- 🔍 **检测概览**: 目标URL、检测类型、检测状态
- 🌐 **页面信息**: 响应状态、内容哈希、页面标题
- 🔗 **链接分析**: 内链、外链统计与分析
- ⚠️ **安全威胁**: 发现的黑链、后门、违规内容等

## ⚙️ 配置说明

### 数据库配置
编辑 `Config/config_db.py` 配置数据库连接：
```python
# SQLite配置（默认）
DB_TYPE = 'sqlite'
DB_PATH = 'Libra.db'
```

### 爬虫配置
在 `Config/config_crawler.py` 中可配置：
- 爬取深度限制
- 并发数量
- 超时设置
- User-Agent配置

### 黑名单配置
文件类型黑名单配置（不进行检测的文件类型）：
```python
file_type_black = [
    '.css', '.jpg', '.png', '.bmp', '.gif', '.ico', '.svg', '.jpeg',
    '.zip', '.rar', '.7z', '.doc', '.xls', '.xlsx', '.pdf',
    '.mp3', '.mp4', '.wmv', '.ttf'
]
```

## 🔧 高级功能

### 代理设置
在 `Config/config_proxies.py` 中配置代理服务器：
```python
PROXIES = {
    'http': 'http://proxy.server:port',
    'https': 'https://proxy.server:port'
}
```

### 自定义规则
通过数据库添加自定义检测规则：
- 黑链检测规则
- 后门检测规则
- 违规内容规则

### 白名单机制
支持白名单机制，避免误报：
- URL白名单
- 内容白名单
- 规则白名单

## 📝 更新日志
### V3.0 (2025-09-22)
- ✅ 项目重构


### V2.53 (2023-12-07)
- ✅ 默认百度爬虫访问，失败时尝试正常访问
- ✅ 提升判定准确率

### V2.52 (2023-12-06)
- ✅ 黑链检测基于script切片实现
- ✅ 提高判定准确率

### V2.51 (2023-12-01)
- ✅ 内外链索引正则优化，现在将发现更多的内外链
- ✅ 优化本地输出，现在将基于markdown语法完成打印
- ✅ 傻瓜式兼容前段输入，不再爆炸

### V2.41 (2023-11-28)
- ✅ 优化违规模块，在违规内容校验前增加ncr解码（全局解码会影响黑链模块原始数据判断）
- ✅ 优化黑链、违规模块输出，增加标签（当前标签拼接字符串）

### V2.40 (2023-11-27)
- ✅ 优化黑链模块规则（精度广度平衡值3级切换）
- ✅ 优化黑链模块输出（现输出内容为中文，不再为不可读编码）

## 🤝 贡献

欢迎提交Issue和Pull Request来改进项目。

## 📄 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 👨‍💻 作者

**RabbitMask** - 网站安全研究者

---

> ⚠️ **免责声明**: 本工具仅用于授权的安全测试和防护目的，请勿用于非法用途。使用者需自行承担使用风险。