## Langchain Custom C++ Executor

This package provides an integrated tool for generating and executing C/C++ code snippets externally in Langchain. Allows Langchain users to specify the desired C++ standard version and set optional CPU time limits for code execution. Provides an interface with subprocess to run the generated C/C++ code.

### Installation

```bash
pip3 install cpp-langchain
```

### Features

- **C/C++ Code Generation and Execution:** Generate and execute C/C++ code snippets to provide answers.
- **Version Selection:** Specify the desired C++ standard version (e.g., c++11, c++14, c++17, c++20).
- **CPU Time Limits:** Set optional CPU time limits for code execution to prevent long-running processes.

### Disclaimer

This tool can execute arbitrary code on the host machine. Use with caution and only if you fully understand the security risks associated with subprocess execution.

- **Default Safety:** The `allow_dangerous_code` option is set to `False` by default to prevent unauthorized code execution.
- **Risk Acceptance:** If you choose to set `allow_dangerous_code` to `True`, you acknowledge and accept the potential risks of executing malicious code.

### Usage

Below is a simple script to use CppSubprocessTool with Langchain. 

For more advanced usages please check [example notebook.](https://github.com/0xdti/cpp-langchain/blob/main/example.ipynb)

```python

import os

os.environ["OPENAI_API_KEY"] = ""

from cpp_langchain import CppSubprocessTool
tools = [CppSubprocessTool(allow_dangerous_code=True)]

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful coding assistant. Make sure to use the CppSubprocessTool tool for code execution.",
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

# Construct the Tools agent
agent = create_tool_calling_agent(llm, tools, prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Execute agent
agent_executor.invoke({"input": "What is the 10th fibonacci number?"})
```

