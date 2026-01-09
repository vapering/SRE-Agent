# 🤖 Deep SRE Agent & Flash Sale Mall

[中文文档](README_CN.md)

**Deep SRE Agent** is a cutting-edge intelligent SRE (Site Reliability Engineering) experimental platform designed to explore the application of LLMs (Large Language Models) in the field of SRE.

This project builds a complete microservices-based e-commerce system (**Flash Sale Mall**) and equips it with an intelligent operations agent (**Deep SRE Agent**) based on the [deepagents](https://github.com/langchain-ai/deepagents) framework.

The Agent can act like a human SRE engineer, proactively inspecting the system, analyzing logs, querying metrics, diagnosing databases, and even performing root cause analysis through natural language.

---

## 🎥 Demo

<video src="https://private-user-images.githubusercontent.com/5309375/532890975-ae0139c2-8fb0-4d21-84ca-55769f423f8f.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc3OTkxNDMsIm5iZiI6MTc2Nzc5ODg0MywicGF0aCI6Ii81MzA5Mzc1LzUzMjg5MDk3NS1hZTAxMzljMi04ZmIwLTRkMjEtODRjYS01NTc2OWY0MjNmOGYubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDEwNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAxMDdUMTUxNDAzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZTQwZWY5YWFkYzk4Yjk1MDU5YzZjY2ViMWMzODQyNDYyMDI4ZDFmN2Q4ZGU2OThjMGM3NDFhNjFhZDA4YTNhZCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.FnKDsYhwLZJiD1CnuaqJj41O1WoAexjH6JP98IsWqiw" data-canonical-src="https://private-user-images.githubusercontent.com/5309375/532890975-ae0139c2-8fb0-4d21-84ca-55769f423f8f.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc3OTkxNDMsIm5iZiI6MTc2Nzc5ODg0MywicGF0aCI6Ii81MzA5Mzc1LzUzMjg5MDk3NS1hZTAxMzljMi04ZmIwLTRkMjEtODRjYS01NTc2OWY0MjNmOGYubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDEwNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAxMDdUMTUxNDAzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZTQwZWY5YWFkYzk4Yjk1MDU5YzZjY2ViMWMzODQyNDYyMDI4ZDFmN2Q4ZGU2OThjMGM3NDFhNjFhZDA4YTNhZCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.FnKDsYhwLZJiD1CnuaqJj41O1WoAexjH6JP98IsWqiw" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px" draggable="true">

  </video>

<video src="https://private-user-images.githubusercontent.com/5309375/532891100-e1df096c-c1ea-49c7-ae54-fefffcfa8939.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc3OTkxNDMsIm5iZiI6MTc2Nzc5ODg0MywicGF0aCI6Ii81MzA5Mzc1LzUzMjg5MTEwMC1lMWRmMDk2Yy1jMWVhLTQ5YzctYWU1NC1mZWZmZmNmYTg5MzkubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDEwNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAxMDdUMTUxNDAzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MGM0MDRjMjc1ZTJhNjY1ODQwODFlZTBmNWMxNmY0ZWRiMTQ0MWE0MTA5YWYxODY0MDk3NjVhMDE4NGFiMWNiMCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.qngfbyXjdYOW8y3iyADBWyFxIQMniETeEA-HBTAyhwo" data-canonical-src="https://private-user-images.githubusercontent.com/5309375/532891100-e1df096c-c1ea-49c7-ae54-fefffcfa8939.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc3OTkxNDMsIm5iZiI6MTc2Nzc5ODg0MywicGF0aCI6Ii81MzA5Mzc1LzUzMjg5MTEwMC1lMWRmMDk2Yy1jMWVhLTQ5YzctYWU1NC1mZWZmZmNmYTg5MzkubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDEwNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAxMDdUMTUxNDAzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MGM0MDRjMjc1ZTJhNjY1ODQwODFlZTBmNWMxNmY0ZWRiMTQ0MWE0MTA5YWYxODY0MDk3NjVhMDE4NGFiMWNiMCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.qngfbyXjdYOW8y3iyADBWyFxIQMniETeEA-HBTAyhwo" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px" draggable="true">

  </video>

> If the video does not play, please check [packages/](packages/) directly.

---

## 🏗️ Overall Architecture

The project adopts a layered architecture design, from bottom to top: Target Business System, Observability Infrastructure, MCP Adapter Layer, and Intelligent Agent Layer.

```mermaid
graph TD
    subgraph "🤖 Intelligent Agent Layer"
        UI[Deep Agents UI :3300] --> Agent[Deep SRE Agent :2024]
        Agent --> |Orchestrate| Wiki[Wiki Agent]
        Agent --> |Orchestrate| Log[Log Agent]
        Agent --> |Orchestrate| Metric[Prometheus Agent]
        Agent --> |Orchestrate| DB[MySQL Agent]
    end

    subgraph "🔌 MCP Adapter Layer"
        Wiki --> |SSE/HTTP| WikiMCP[DeepWiki MCP]
        Log --> |SSE/HTTP| LokiMCP[Loki MCP :7080]
        Metric --> |HTTP| PromMCP[Prometheus MCP :18090]
        DB --> |HTTP| DBHub[DBHub/MySQL MCP :18081]
    end

    subgraph "📊 Observability Infrastructure"
        PromMCP --> Prometheus[Prometheus :9090]
        LokiMCP --> Loki[Loki :3100]
        Prometheus --> Grafana[Grafana :3000]
        Promtail --> Loki
    end

    subgraph "🛒 Target System (Flash Sale Mall)"
        Frontend[Frontend :5173] --> Backend[Backend :3001]
        Backend --> MySQL[MySQL :3306]
        Backend --> Redis[Redis :6379]
        Backend --> Kafka[Kafka :9092]
        Backend -.-> |Logs| Promtail
        Backend -.-> |Metrics| Prometheus
        Backend -.-> |Traces| OAP
    end
```

### Core Components

1.  **Flash Sale Mall (Target System)**
    *   A high-concurrency flash sale mall based on Spring Boot 3 + React 18.
    *   Integrated full-link monitoring: Micrometer (Metrics), Logback (Logs), tempo (Traces).
    *   See: [README_flashMall.md](README_flashMall.md)

2.  **Observability Stack**
    *   **Prometheus**: Metric storage and querying.
    *   **Loki**: Log aggregation and retrieval.
    *   **tempo**: Distributed tracing.
    *   **Grafana**: Unified monitoring dashboard.

3.  **MCP Layer (Model Context Protocol Layer)**
    *   Acts as a standard bridge between LLM and infrastructure.
    *   **Prometheus MCP**: Allows Agent to execute PromQL.
    *   **Loki MCP**: Allows Agent to use LogQL to query logs.
    *   **DBHub**: Allows Agent to execute SQL to query data.
    *   **tempo MCP**: Allows Agent to query topology and traces.

4.  **Sub-Agent Layer**
    *   **Prometheus Agent**: Focuses on metric query and analysis, generating PromQL and interpreting monitoring data.
    *   **Log Agent**: Focuses on log retrieval, using LogQL to filter error stacks and exceptions.
    *   **MySQL Agent**: Focuses on database diagnosis, executing SQL to query business data or slow queries.
    *   **Wiki Agent**: Focuses on knowledge base retrieval, providing system architecture documents and SRE runbook support.

5.  **Deep SRE Agent (Main Intelligent Agent)**
    *   A Multi-Agent system orchestrator based on LangGraph.
    *   Responsible for receiving user instructions, decomposing tasks, scheduling sub-agents, and summarizing reasoning results.

---

## 🚀 Quick Start

### 1. Prerequisites
*   **Docker & Docker Compose**: Core dependency, used to start all services.
*   **API Key**: Requires OPENAI or other compatible LLM API Key.

### 2. Configure Agent
Copy the environment variable template and fill in your API Key:
```bash
cp deep_sre_agent/.env.example deep_sre_agent/.env.dev
# Edit .env.dev and fill in keys, etc.
```

### 3. One-Click Start
Use Docker Compose to bring up the entire environment (including Mall, Monitoring, MCP Services, Agent, and UI):

```bash
docker compose up -d --build
```

> **Note**: The first startup requires downloading multiple images and building the Agent environment, which may take tens of minutes.

### 4. Access the System

| Service Name | URL / Port | Description |
| :--- | :--- | :--- |
| **Deep Agents UI** | http://localhost:3300 | **Agent Entry**, chat with SRE Agent here |
| **Flash Sale Mall** | http://localhost:5173 | Mall Frontend, test flash sales here |
| **LangGraph API** | http://localhost:2024 | Agent Backend API (for UI) |
| **Backend API** | http://localhost:3001 | Mall Backend API |
| **Grafana** | http://localhost:3000 | Monitoring Dashboard (Account: admin / admin123) |
| **Prometheus** | http://localhost:9090 | Native Metric Query Interface |

---

## 💻 Development Guide

### SRE Agent Development
Agent code is located in the `deep_sre_agent/` directory.
*   **Architecture**: Uses LangGraph to orchestrate multi-agent collaboration.
*   **Debugging**:
    *   Recommended to use Jupyter Notebook (`research_agent.ipynb`) for interactive debugging.
    *   Or run `langgraph dev` locally to start the API server.
*   **Extension**: Create a new Agent directory under `deep_sre_agent/` and write `mcp_client.py` to connect to new MCP services.

### Mall Business Development
Business code is located in `backend-spring/` (Backend) and `src/` (Frontend).
*   **Backend**: Spring Boot 3.3, Java 21.
*   **Frontend**: React 18, Vite, TailwindCSS.
*   **Local Run**: Refer to the development guide in [README_flashMall.md](README_flashMall.md).

---

## 🔌 Service Port Mapping

| Container Service | Port | Usage |
| :--- | :--- | :--- |
| `deep-agents-ui` | **3300** | Agent Chat Interface (Next.js) |
| `deep-sre-agent` | **2024** | Agent Core Logic (LangGraph API) |
| `flashsale-frontend` | **5173** | Mall Frontend (Nginx/Vite) |
| `flashsale-backend` | **3001** | Mall Backend (Spring Boot) |
| `flashsale-grafana` | **3000** | Monitoring Visualization |
| `flashsale-prometheus`| **9090** | Metric Storage |
| `flashsale-loki` | **3100** | Log Storage |
| `flashsale-mysql` | **3306** | Business Database |
| `flashsale-redis` | **6379** | Cache & Rate Limiting |
| `flashsale-kafka` | **9092** | Message Queue |
| `prometheus-mcp` | **18090** | Prometheus MCP Adapter |
| `dbhub` (MySQL MCP) | **18081** | SQL Execution Adapter |
| `loki-mcp` | **7080** | Loki MCP Adapter |

---

## 🤝 Contribution & License

Issues and PRs are welcome!

*   **License**: [MIT License](LICENSE)

---
**Deep SRE Agent** - Make operations smarter, make systems more reliable.
