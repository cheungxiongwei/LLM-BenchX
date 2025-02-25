# LLM-BenchX

## Project Overview

LLM-BenchX is a lightweight and easy-to-use benchmarking tool for Large Language Models (LLMs). It supports multiple LLM providers, including OpenAI, DeepSeek, and more. The tool measures key performance metrics such as response time and token throughput (tokens per second).

## Features
- **Support for multiple LLM providers**: Test OpenAI, Ollama, DeepSeek, and other API-compatible models.
- **Automatic token processing rate calculation**: Measure how many tokens are generated per second.
- **User-friendly table output**: Uses `tabulate` for clear and structured results.
- **Environment variable support**: Manages API keys securely with `python-dotenv`.
- **Custom filtering**: Use regex patterns to benchmark specific providers.

## Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/LLM-BenchX.git
cd LLM-BenchX
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Add API keys to the `.env` file:
```
OPENAI_API_KEY=your_openai_api_key
PROVIDER2_API_KEY=your_provider2_api_key
```

### 4. Run the benchmark
```bash
python benchmark.py
```

## Sample Output
```
+---------------------+----------+-----------------+------------+-------------------------------------------------------+
| Provider            | Status   | Response Time   | Token/s    | Reply Preview                                         |
+=====================+==========+=================+============+=======================================================+
| OpenAI             | Success  | 2.34 sec        | 23.12 tok/s| Hello! How can I assist you today? ...                |
+---------------------+----------+-----------------+------------+-------------------------------------------------------+
| Tencent@deepseek-r1 | Success  | 6.84 sec        | 10.58 tok/s| Hello! How can I assist you today? 😊...               |
+---------------------+----------+-----------------+------------+-------------------------------------------------------+
```

## Contributing
Issues and PRs are welcome! If you have suggestions for new LLM provider support or improvements, feel free to submit them on GitHub.

## License
MIT License
