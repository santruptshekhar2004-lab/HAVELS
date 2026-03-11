# Agent AI Orchestrator

Multi-agent orchestration system using [Strands Agents SDK](https://strandsagents.com) + Gemini 2.5 Flash.

## Problem Statement

1. **Intent Classification & Routing** — Route user queries between a Shopping agent and an IoT device-control agent, even when intent changes mid-conversation.
2. **Prompt Injection Defense** — Reject anything outside the two supported domains.

## How It Works

```
User ──► Orchestrator
              │
              ├─ Phase 1: structured_output() → { intent, confidence }
              │   (no tools, constrained JSON, fast)
              │
              ├─ out_of_scope? → instant rejection
              │
              └─ Phase 2: route to specialist
                    ├──► 🛒 Shopping Agent
                    └──► 💡 IoT Agent
```

- **Structured pre-classification** via `structured_output()` returns a Pydantic model with intent + confidence. JSON-constrained, no hallucination on routing.
- **Agents-as-tools** pattern — each specialist is a `@tool`-wrapped Strands agent.
- **Prompt injection** caught at classifier level before any specialist is invoked.
- Gemini 2.5 Flash with `temperature=0.2` keeps classification deterministic and fast.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GEMINI_API_KEY="your-key-here"
```

## Run

Streamlit UI (recommended):
```bash
streamlit run app.py
```

CLI interactive chat:
```bash
python main.py
```

Non-interactive demo:
```bash
python demo.py
```
