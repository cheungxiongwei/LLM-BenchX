import logging
import os
import re
import time
from openai import OpenAI
from tabulate import tabulate
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_LOG"] = "debug"

test_prompt = "Hello"

tokens_per_char = 1 / 4  # 估算每个 token 约 4 个字符

# 配置不同的LLM提供商API信息
llm_providers = {
    "Tencent@deepseek-chat": {
        "url": "https://api.lkeap.cloud.tencent.com/v1",
        "api_key": os.getenv("Tencent_API_KEY"),
        "model": "deepseek-v3",
    },
    "Tencent@deepseek-reasoner": {
        "url": "https://api.lkeap.cloud.tencent.com/v1",
        "api_key": os.getenv("Tencent_API_KEY"),
        "model": "deepseek-r1",
    },
    "DeepSeek@deepseek-chat": {
        "url": "https://api.deepseek.com/v1",
        "api_key": os.getenv("DeepSeek_API_KEY"),
        "model": "deepseek-chat",
    },
    "DeepSeek@deepseek-reasoner": {
        "url": "https://api.deepseek.com/v1",
        "api_key": os.getenv("DeepSeek_API_KEY"),
        "model": "deepseek-reasoner",
    },
    "Fireworks@deepseek-chat": {
        "url": "https://api.fireworks.ai/inference/v1",
        "api_key": os.getenv("Fireworks_API_KEY"),
        "model": "accounts/fireworks/models/deepseek-v3",
    },
    "Fireworks@deepseek-reasoner": {
        "url": "https://api.fireworks.ai/inference/v1",
        "api_key": os.getenv("Fireworks_API_KEY"),
        "model": "accounts/fireworks/models/deepseek-r1",
    },
    "Together@deepseek-chat": {
        "url": "https://api.together.xyz/v1",
        "api_key": os.getenv("Together_API_KEY"),
        "model": "deepseek-ai/DeepSeek-V3",
    },
    "Alibaba@deepseek-chat": {
        "url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "api_key": os.getenv("Alibaba_API_KEY"),
        "model": "deepseek-v3",
    },
    "Alibaba@deepseek-reasoner": {
        "url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "api_key": os.getenv("Alibaba_API_KEY"),
        "model": "deepseek-r1",
    },
    "Deepinfra@deepseek-chat": {
        "url": "https://api.deepinfra.com/v1/openai",
        "api_key": os.getenv("Deepinfra_API_KEY"),
        "model": "deepseek-ai/DeepSeek-V3",
    },
    "Deepinfra@deepseek-reasoner": {
        "url": "https://api.deepinfra.com/v1/openai",
        "api_key": os.getenv("Deepinfra_API_KEY"),
        "model": "deepseek-ai/DeepSeek-R1",
    },
    "Siliconflow@deepseek-chat": {
        "url": "https://api.siliconflow.cn/v1",
        "api_key": os.getenv("Siliconflow_API_KEY"),
        "model": "deepseek-ai/DeepSeek-V3",
    },
    "Siliconflow@deepseek-reasoner": {
        "url": "https://api.siliconflow.cn/v1",
        "api_key": os.getenv("Siliconflow_API_KEY"),
        "model": "deepseek-ai/DeepSeek-R1",
    },
    "Siliconflow@pro/deepseek-chat": {
        "url": "https://api.siliconflow.cn/v1",
        "api_key": os.getenv("Siliconflow_API_KEY"),
        "model": "Pro/deepseek-ai/DeepSeek-V3",
    },
    "Siliconflow@pro/deepseek-reasoner": {
        "url": "https://api.siliconflow.cn/v1",
        "api_key": os.getenv("Siliconflow_API_KEY"),
        "model": "Pro/deepseek-ai/DeepSeek-R1",
    },
    "Novita@deepseek-chat": {
        "url": "https://api.novita.ai/v3/openai",
        "api_key": os.getenv("Novita_API_KEY"),
        "model": "deepseek/deepseek_v3",
    },
    "Novita@deepseek-reasoner": {
        "url": "https://api.novita.ai/v3/openai",
        "api_key": os.getenv("Novita_API_KEY"),
        "model": "deepseek/deepseek-r1",
    },
    # 添加更多提供商
}

def benchmark_provider(name, config):
    logging.info(f"request {name}: {config["model"]} endpoint.")
    start_time = time.time()
    try:
        client = OpenAI(api_key=config["api_key"], base_url=config["url"])
        response = client.chat.completions.create(
            model=config["model"],
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": test_prompt},
            ],
            stream=False,
        )
        latency = time.time() - start_time
        reply = (
            response.choices[0].message.content if response.choices else "<No response>"
        )
        token_count = int(len(reply) * tokens_per_char)
        tokens_per_sec = token_count / latency if latency > 0 else 0
        return (
            name,
            "Success",
            f"{latency:.2f} sec",
            f"{tokens_per_sec:.2f} tok/s",
            reply[:50] + "...",
        )
    except Exception:
        return name, "Failed", "-", "-", "-"

def main(selected_providers=None):
    if selected_providers:
        filtered_providers = {
            name: config
            for name, config in llm_providers.items()
            if any(re.match(sp, name) for sp in selected_providers)
        }
    else:
        filtered_providers = llm_providers

    results = [
        benchmark_provider(name, config) for name, config in filtered_providers.items()
    ]
    print(
        tabulate(
            results,
            headers=["Provider", "Status", "Response Time", "Token/s", "Reply Preview"],
            tablefmt="grid",
        )
    )


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    selected = [r"^Tencent",r"^DeepSeek",r"^Alibaba",r"^Fireworks",r"^Fireworks",r"^Together",r"^Deepinfra",r"^Siliconflow",r"^Novita"]
    main(selected)
