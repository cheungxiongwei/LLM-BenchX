# LLM-BenchX

[![language](https://img.shields.io/badge/language-en__US-blue?style=flat)](https://github.com/cheungxiongwei/LLM-BenchX/blob/main/README_enUS.md)

## 项目简介

🔥LLM-BenchX 是一个轻量级、易于使用的 LLM（大语言模型）性能基准测试工具，支持多种 LLM 提供商，包括 OpenAI、DeepSeek 等。它能够快速测量不同 LLM 在响应时间、吞吐率（token/s）等关键性能指标上的表现。

## 功能特性
- **支持多家 LLM 提供商**：可测试 OpenAI、Ollama、DeepSeek 及其他 API 兼容的模型。
- **自动统计 Token 处理速率**：计算每秒生成的 token 数，评估吞吐性能。
- **友好的表格输出**：使用 `tabulate` 以清晰的格式展示结果。
- **环境变量支持**：利用 `python-dotenv` 进行 API 密钥管理。
- **可定制筛选**：支持通过正则表达式筛选特定提供商进行测试。

## 安装与使用

### 1. 克隆仓库
```bash
git clone https://github.com/cheungxiongwei/LLM-BenchX.git
cd LLM-BenchX
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置环境变量
在 `.env` 文件中添加 API 密钥：
```
OPENAI_API_KEY=your_openai_api_key
DeekSeed_API_KEY=your_deepseed_api_key
```

### 4. 运行基准测试
```bash
python benchmark.py
```

## 输出示例
```
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Provider                          | Status   | Response Time   | Token/s     | Reply Preview                                         |
+===================================+==========+=================+=============+=======================================================+
| Tencent@deepseek-chat             | Success  | 2.59 sec        | 3.48 tok/s  | Hello! How can I assist you today? 😊...              |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Tencent@deepseek-reasoner         | Success  | 7.56 sec        | 1.19 tok/s  | Hello! How can I assist you today? 😊...              |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| DeepSeek@deepseek-chat            | Success  | 8.06 sec        | 1.12 tok/s  | Hello! How can I assist you today? 😊...              |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| DeepSeek@deepseek-reasoner        | Success  | 16.67 sec       | 0.48 tok/s  | Hello! How can I assist you today?...                 |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Fireworks@deepseek-chat           | Success  | 5.40 sec        | 5.93 tok/s  | Hello! 😊 How can I assist you today? Whether you h...|
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Fireworks@deepseek-reasoner       | Success  | 3.11 sec        | 36.62 tok/s | <think>                                               |
|                                   |          |                 |             | Okay, the user greeted me with "Hello". I ...         |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Together@deepseek-chat            | Success  | 1.88 sec        | 4.79 tok/s  | Hello! How can I assist you today? 😊...              |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Alibaba@deepseek-chat             | Success  | 6.31 sec        | 4.60 tok/s  | Hello! How can I assist you today? Whether you hav... |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Alibaba@deepseek-reasoner         | Success  | 13.69 sec       | 0.58 tok/s  | Hello! How can I assist you today?...                 |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Deepinfra@deepseek-chat           | Success  | 3.81 sec        | 2.36 tok/s  | Hello! How can I assist you today? 😊...              |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Deepinfra@deepseek-reasoner       | Success  | 9.36 sec        | 8.76 tok/s  | <think>                                               |
|                                   |          |                 |             | Okay, the user greeted me with "Hello". I ...         |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Siliconflow@deepseek-chat         | Success  | 2.31 sec        | 3.46 tok/s  | Hello! How can I assist you today?...                 |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Siliconflow@deepseek-reasoner     | Success  | 3.78 sec        | 2.38 tok/s  | Hello! How can I assist you today? 😊...              |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Siliconflow@pro/deepseek-chat     | Success  | 5.98 sec        | 6.86 tok/s  | Hello! How can I assist you today? Whether you hav... |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Siliconflow@pro/deepseek-reasoner | Success  | 3.81 sec        | 2.10 tok/s  | Hello! How can I assist you today?...                 |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Novita@deepseek-chat              | Success  | 3.01 sec        | 2.99 tok/s  | Hello! How can I assist you today? 😊...              |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Novita@deepseek-reasoner          | Success  | 5.22 sec        | 9.58 tok/s  | <think>                                               |
|                                   |          |                 |             | Okay, the user greeted me with "Hello". I ...         |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Openrouter@deepseek-chat          | Success  | 1.73 sec        | 0.00 tok/s  | ...                                                   |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Openrouter@deepseek-reasoner      | Success  | 2.99 sec        | 2.67 tok/s  | Hello! How can I assist you today?...                 |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Targon@deepseek-chat              | Failed   | -               | -           | -                                                     |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
| Targon@deepseek-reasoner          | Failed   | -               | -           | -                                                     |
+-----------------------------------+----------+-----------------+-------------+-------------------------------------------------------+
```

## 贡献
欢迎 issue 和 PR！如果你有新的 LLM 提供商支持需求或优化建议，请提交到 GitHub。

## 许可证
MIT License
