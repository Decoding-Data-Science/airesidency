# AI Residency

This repository contains notebooks, scripts and other resources from the DDS AI
Residency program.  Materials range from Python fundamentals and deep learning
tutorials to examples using frameworks such as LangChain and LangGraph.  Use
these samples and demos as references for building chatbots, exploring
retrieval‑augmented generation (RAG) techniques and experimenting with
agentic workflows.

# DDS AI Residency — Code, Notebooks & Demos

This repository is the **hands-on lab archive** for the Decoding Data Science (DDS) **AI Residency** program.  
It contains the exact notebooks, scripts, and mini-projects used across cohorts — from **Python foundations** and **prompt engineering**, through **RAG + evaluation**, and ending with **agentic systems + MCP**.

> Recommended flow: **Prompting → Python + Data → LLM Apps → RAG → Evaluation → Agents → Multi-Agents → MCP → Ship**

---

## Quick Start

### Open in Google Colab (no installation)
1. Go to: https://colab.research.google.com
2. Open any notebook directly from GitHub:
   - Replace the URL pattern:  
     `https://colab.research.google.com/github/Decoding-Data-Science/airesidency/blob/main/<NOTEBOOK>.ipynb`

### Repo Navigation (Folders)
- `python_for_ai/` — Python fundamentals for AI builders  
- `fast_api/` — API deployment demos  
- `aws-bedrock/` — Bedrock examples + integrations  
- `langchain_airesidency/` — LangChain apps, tools, memory, agents  
- `langgraph/` — LangGraph workflows, corrective RAG, agent graphs  
- `ragmc/` — Retrieval-Augmented Generation demos and variants  
- `mcp_handson/` — MCP hands-on labs (late-stage: tool ecosystem + integration)  
- `crewai-first/` — Multi-agent systems with CrewAI  
- `kahoot/` — Quizzes used in sessions  
- `math_llm/` — (Historical) LLM + math experiments  

---

## Program Map (Day-by-Day Learning Path)

This is the suggested **day-level** flow we use in the Residency.  
Each day points to the *type of files you’ll find in this repo* and how they connect.

### Day 0 — Builder Setup + Prompt Engineering Foundations
Goal: stop “prompt luck” and build repeatable prompting habits.

**What you learn**
- Zero-shot / few-shot / structured prompting
- System vs user instructions, grounding, constraints
- Output formatting, safety & guardrails mindset

**Where to look in this repo**
- `tools_agents.ipynb`, `tools_multi_agents.ipynb` (tools + thinking patterns)
- Notebooks that contain “assistant” patterns (e.g., weather assistants, first chatbots)

---

### Day 1 — Python for AI Builders
Goal: write clean Python to ship AI apps fast.

**Key notebooks**
- `Variables.ipynb`
- `Lesson_2_Repeating_tasks_with_for_loops.ipynb`
- `Using_files_in_Python.ipynb`
- `strating_with_data_in_python.ipynb`
- `xtracting_restaurant_information_from_journal_entries.ipynb`
- `Lesson_3_Reading_journals_from_food_critics.ipynb`

**Outcome**
- You can manipulate text/data, structure outputs, read files, and prepare inputs for LLM pipelines.

---

### Day 2 — From Python to Your First LLM App (Chatbots)
Goal: build a working chatbot end-to-end, then ship a UI version.

**Core demos**
- `first_chatbot_19jul.ipynb`
- `first_chatbot_19jul_gradio.ipynb`
- `first_python_chatbot_logo_HF.ipynb`
- `python_tutor_03_01.ipynb`, `python_tutor_22_02.ipynb` (teaching/assistant style bots)

**LLM providers used across cohorts**
- Groq demos:
  - `groq_colab.ipynb`, `groq_colab_5july.ipynb`, `groq_sdk.ipynb`
  - `groq_colab_5july_withgradio.ipynb`
- Bedrock demos:
  - `aws-bedrock/`

**Outcome**
- You can move from notebook → working assistant → basic Gradio/HF deployment.

---

### Day 3 — Embeddings & Vector Databases
Goal: understand embeddings as the foundation for retrieval, memory, and agent grounding.

**Key notebooks**
- `Vector_embedding.ipynb`
- `weavite_Vector_embedding23_jan.ipynb`
- `weavite_Vector_embedding29mar.ipynb`

**Outcome**
- You can generate embeddings, store/search vectors, and prepare for RAG.

---

### Day 4 — RAG: Your First Retrieval-Augmented Generation System
Goal: stop hallucinations by grounding responses in your documents.

**Core notebooks**
- `your_firstRAG.ipynb`
- `your_firstRAG_cohort7.ipynb`
- `your_firstRAG_cohort7_updated.ipynb`
- `rag_llamaindex.ipynb`
- `Copy_of_rag_llamaindex.ipynb`
- `first_rag_llamaindex_c7.ipynb`

**Index + vector store demos**
- `Cohort_6_PineconeIndexDemo.ipynb`
- `Copy_of_PineconeIndexDemo.ipynb`
- `MC_11_PineconeIndexDemo.ipynb`

**Outcome**
- You can ingest docs → chunk → embed → retrieve → answer with citations/grounding.

---

### Day 5 — LLM Evaluation & Quality
Goal: measure quality like an engineer, not by vibes.

**Key notebooks**
- `1_evaluation_recipe.ipynb`
- `1_evaluation_recipe-c7.ipynb`

**Outcome**
- You can define evaluation signals (accuracy, relevance, faithfulness), test changes, and iterate systematically.

---

### Day 6 — LangChain Core (Chains, Tools, Memory)
Goal: turn prompts into *applications* with structure: tools, memory, retrieval, routing.

**Key notebooks**
- `langchain_agent.ipynb`
- `Memory_management_for_AI_Apps_Agents_using_Langchain.ipynb`
- `Memory_management_for_AI_Apps_Agents_using_Langchain6thsep.ipynb`
- LangChain chain + agent variants:
  - `Langchain_chains_agent_6thsep.ipynb`
  - `Langchain_chains_agent_12thapr.ipynb`
  - `Langchain_chains_agent_12thjul.ipynb`
  - `Langchain_chains_agent_15thov.ipynb`
  - `Langchain_chains_agent_1feb-2025.ipynb`
  - `Langchain_chains_agent_1febnew.ipynb`

**Outcome**
- You can build **tool-using assistants** and control behavior with memory and routing.

---

### Day 7 — LangGraph: Agentic Workflows & Corrective RAG
Goal: build *stateful* agent systems with robust control flow.

**Key notebooks**
- `simplegraph20sep.ipynb`
- `simplegraph20thfeb.ipynb`
- `Copy_of_simplegraph20sep.ipynb`
- `Langraph_with_tools_cohort7.ipynb`
- `Building_an_Agentic_Corrective_RAG_System_with_LangGraph.ipynb`

**Outcome**
- You can model multi-step workflows (states, retries, tool calls, verification loops).

---

### Day 8 — Multi-Agent Systems (CrewAI)
Goal: orchestrate specialists that collaborate on a goal (planner/writer/reviewer/tool-runner).

**Key notebooks**
- `crewai_21stnov2024.ipynb`
- `crewai_15thfeb.ipynb`
- `crewai_26th.ipynb`
- `crewai_multiagent_2025_level_1.ipynb`
- `crewai_multiagent_2025.ipynb`
- `crewai_multiagent_Gitex_level_2_.ipynb`
- `crewai_multiagent_Gitex_level_2_29th_nov_.ipynb`
- `multi_agent_collaboration.ipynb`

**Reference PDF**
- `Ship_Your_Multi-Agent_System_Building_a_Collaborative_Writer_App_with_CrewAI.pdf`

**Outcome**
- You can design roles, tasks, tool access, and evaluation for multi-agent pipelines.

---

### Day 9 — MCP Hands-On (Late Stage)
Goal: connect agents to real tools reliably, like production systems.

**Where to look**
- `mcp_handson/`

**Why MCP comes late**
- MCP becomes powerful only after you understand:
  - tool calling + structured outputs  
  - routing + memory  
  - evaluation + safety boundaries  
  - multi-agent orchestration

**Outcome**
- You can standardize tool integrations and scale beyond one-off scripts.

---

## Applied Demo Tracks (Real Use Cases)

These notebooks are used as mini-projects and concept reinforcement.

### Weather Assistants (tools + function calling + deployment readiness)
- `Weather_assistant26jul.ipynb`
- `weather_assistant14thsep.ipynb`
- `weather_assistant24thmay.ipynb`
- `weather_assistant4thoct.ipynb`
- `Weather_functioncall (1).ipynb`
- `Another_copy_of_weather_assistant.ipynb`

### Financial Market Assistants
- `stock_market_14thsep.ipynb`
- `stock_market_26_jul.ipynb`
- `stock_market_28th_sep.ipynb`
- Folder: `Creating AI Financial Market Assistant Using AI Agents/`

### Fine-tuning / Transformers (Optional / Advanced)
- `hf_transformer.ipynb`
- `huggingface_practice.ipynb`
- `Text_Summary_T5_Fine_Tuned.ipynb`
- `lora_finetuning.yml`

---

## Recommended Learning Order (If You’re Self-Studying)

1. **Prompting & tool mindset**  
2. **Python foundations** (files, loops, data basics)  
3. **First chatbot + Gradio** (ship something)  
4. **Embeddings**  
5. **RAG + Pinecone/LlamaIndex**  
6. **Evaluation recipes**  
7. **LangChain (tools/memory/routing)**  
8. **LangGraph (workflows + corrective loops)**  
9. **CrewAI multi-agents**  
10. **MCP hands-on** (production-grade tool ecosystem)

---

## How to Use This Repo During Cohort

- Use notebooks as **reference implementations** (not copy-paste only).
- Every major concept has at least one of:
  - a **minimal demo**
  - a **cohort-specific variant**
  - a **shipping version** (Gradio / deployment)

**Tip for trainers:** Prefer the most recent cohort notebook variant when duplicates exist.

---

## License / Usage

These materials are provided for DDS AI Residency learning and internal cohort use.  
If you want to reuse for training delivery or workshops, request permission from DDS.

---

## Support

- Ask in the cohort community channel (preferred)
- Tag your mentor with the notebook name + error screenshot + what you tried
