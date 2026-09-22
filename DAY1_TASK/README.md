# Day 1 Task — Chatbot vs Workflow vs AI Agent

## Overview

This project compares three approaches for solving the same student
placement tracking problem:

1. Plain LLM Chatbot
2. Rule-Based Workflow
3. AI Agent with Tool Usage

The scenario uses private student placement data stored in a JSON file.

---

## Project Structure

```text
DAY1_TASK/
│
├── agent/
│   ├── agent.py
│   └── tools.py
│
├── chatbot/
│   └── chatbot.py
│
├── data/
│   └── student_data.json
│
├── Output/
│
├── workflow/
│   └── workflow.py
│
├── .gitignore
├── analysis.md
├── README.md
└── requirements.txt
