# Agent AI Orchestrator

Multi-agent orchestration system using [Strands Agents SDK](https://strandsagents.com) + Gemini 2.5 Pro.

## Problem Statement

1. **Intent Classification & Routing** — Correctly route user queries between a Shopping agent and an IoT device-control agent, even when intent changes mid-conversation ("turn on the AC" → "no, I want to buy an AC").
2. **Prompt Injection Defense** — Reject anything outside the two supported domains. Attempts to override instructions, extract the system prompt, or ask off-topic questions are blocked.

## How It Works

```
User ──► Orchestrator Agent ──┬──► Shopping Agent
                              └──► IoT Agent
```

- The **Orchestrator** is a Strands agent whose system prompt strictly limits it to two domains. It uses the "agents-as-tools" pattern — each specialist agent is wrapped with `@tool` and passed to the orchestrator.
- The orchestrator reads the **latest** user message to determine current intent (handles mid-conversation switches).
- Out-of-scope or injection attempts get a flat rejection — no tool is called.
- Gemini 2.5 Pro with `temperature=0.2` keeps classification deterministic and fast.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GEMINI_API_KEY="your-key-here"
```

## Run

Interactive chat:
```bash
python main.py
```

Non-interactive demo (runs all test cases):
```bash
python demo.py
```

## Latency

Orchestrator classification + specialist response typically lands in the 200-400ms range depending on Gemini API latency. The low temperature and concise system prompts keep token counts minimal.
