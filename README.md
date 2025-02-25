# LLM-BenchX

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
+---------------------+----------+-----------------+------------+-------------------------------------------------------+
| Provider            | Status   | Response Time   | Token/s    | Reply Preview                                         |
+=====================+==========+=================+============+=======================================================+
| OpenAI             | Success  | 2.34 sec        | 23.12 tok/s| Hello! How can I assist you today? ...                |
+---------------------+----------+-----------------+------------+-------------------------------------------------------+
| Tencent@deepseek-r1 | Success  | 6.84 sec        | 10.58 tok/s| Hello! How can I assist you today? 😊...               |
+---------------------+----------+-----------------+------------+-------------------------------------------------------+
```

## 贡献
欢迎 issue 和 PR！如果你有新的 LLM 提供商支持需求或优化建议，请提交到 GitHub。

## 许可证
MIT License
