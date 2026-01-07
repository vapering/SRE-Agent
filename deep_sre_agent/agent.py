from datetime import datetime
import os
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from deepagents import create_deep_agent
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek
from langgraph.checkpoint.memory import MemorySaver

env_path = os.path.join(os.path.dirname(__file__), ".env.dev")
if os.path.exists(env_path):
    load_dotenv(env_path)

from wiki_agent import (
    WIKI_AGENT_INSTRUCTIONS,
    wiki_read_structure,
    wiki_read_contents,
    wiki_ask_question,
)
# Create wiki sub-agent
wiki_sub_agent = {
    "name": "wiki-agent",
    "description": "项目的知识库Agent，当遇到和系统故障相关的问题和事件时，优先使用该Agent从系统架构层面进行分析，以便于指导下一步的问题排查分析计划。",
    "system_prompt": WIKI_AGENT_INSTRUCTIONS,
    "tools": [wiki_read_structure, wiki_read_contents, wiki_ask_question],
}


from log_agent import (
    LOG_AGENT_INSTRUCTIONS,
    log_query,
)
# Create wiki sub-agent
log_sub_agent = {
    "name": "log-agent",
    "description": "项目的日志Agent，当需要对错误日志进行排查时，使用这个log-agent。",
    "system_prompt": LOG_AGENT_INSTRUCTIONS,
    "tools": [log_query],
}

from prometheus_agent import (
    PROMETHEUS_AGENT_INSTRUCTIONS,
    prom_query_range,
    prom_query_instant,
    prom_list_targets,
    prom_metadata,
)
# Create prometheus sub-agent
prom_sub_agent = {
    "name": "prometheus-agent",
    "description": "项目的指标与告警Agent，用于 PromQL 查询与健康度诊断。",
    "system_prompt": PROMETHEUS_AGENT_INSTRUCTIONS,
    "tools": [
        prom_query_range,
        prom_query_instant,
        prom_list_targets,
        prom_metadata,
    ],
}

from mysql_agent import (
    MYSQL_AGENT_INSTRUCTIONS,
    mysql_execute,
    mysql_search_objects,
)
mysql_sub_agent = {
    "name": "mysql-agent",
    "description": "项目的数据库Agent，用于执行SQL查询/变更与对象检索。",
    "system_prompt": MYSQL_AGENT_INSTRUCTIONS,
    "tools": [
        mysql_execute,
        mysql_search_objects,
    ],
}

from prompts import (
    SRE_WORKFLOW_INSTRUCTIONS, 
    SRE_TASK_DESCRIPTION_PREFIX,
    SRE_SUBAGENT_DELEGATION_INSTRUCTIONS,
    )

# Limits
max_concurrent_research_units = 3
max_researcher_iterations = 3

# Get current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Combine orchestrator instructions (RESEARCHER_INSTRUCTIONS only for sub-agents)
INSTRUCTIONS = (
    SRE_WORKFLOW_INSTRUCTIONS
    + "\n\n"
    + "=" * 80
    + "\n\n"
    + SRE_SUBAGENT_DELEGATION_INSTRUCTIONS.format(
        max_concurrent_research_units=max_concurrent_research_units,
        max_researcher_iterations=max_researcher_iterations,
    )
)



base_url = os.getenv("OPENAI_COMPAT_BASE_URL")
api_key = os.getenv("OPENAI_COMPAT_API_KEY")

model = ChatOpenAI(base_url=base_url, api_key=api_key, model="gpt-5.2")

# Create the agent
agent = create_deep_agent(
    model=model,
    # tools=[tavily_search, think_tool],
    system_prompt=INSTRUCTIONS,
    subagents=[wiki_sub_agent, log_sub_agent, prom_sub_agent, mysql_sub_agent],
    # interrupt_on={
    #     "delete_file": True,  # Default: approve, edit, reject
    #     "read_file": False,   # No interrupts needed
    #     "task": {"allowed_decisions": ["approve", "edit", "reject"]},  # No editing
    # }
)
