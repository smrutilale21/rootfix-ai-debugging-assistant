# 🛠️ RootFixAI — Debugging & Root Cause Assistant

An AI-powered debugging assistant that helps developers, students, and freelancers convert messy code errors into **structured root-cause reports** with fixes, explanations, assumptions, and actionable insights.

---

# 🚀 Overview

Debugging can be time-consuming and frustrating, especially when dealing with unclear errors, stack traces, or unfamiliar code.

**RootFixAI** solves this by transforming raw debugging inputs into a **clear, structured, and reusable debugging report**.

---

# 🎯 Problem Statement

Developers often struggle with:

* Understanding error messages and stack traces
* Identifying the exact root cause
* Fixing issues efficiently
* Learning how to avoid similar bugs

Most tools provide answers, but not **structured, reusable insights**.

---

# 💡 Solution

RootFixAI takes:

* Buggy code
* Error / traceback
* Expected behavior
* Additional context

And generates a **complete debugging report** including:

* Root cause
* Severity
* Fixed code
* Explanation
* Assumptions
* Prevention tips
* Confidence score

---

# ✨ Key Features

* 🔍 Analyze buggy code and error messages
* 🧠 Identify root cause and bug type
* 🚨 Detect severity (Low / Medium / High / Critical)
* 💻 Generate corrected code
* 📘 Explain why the fix works
* ⚠️ Provide assumptions when information is incomplete
* 🛡️ Suggest prevention tips
* 🎓 Include beginner-friendly learning notes
* 📊 Confidence score + explanation
* 📂 Sample bugs for quick demo
* ⚠️ Language mismatch warning
* 🕘 Session history tracking
* ⬇️ Download full debugging report as JSON

---

# 🧩 System Architecture

```text
User Input (code + error + context)
        ↓
Prompt Builder
        ↓
LLM (Debug Analysis)
        ↓
Structured Output (Pydantic Schema)
        ↓
Report Builder (custom JSON structure)
        ↓
Streamlit UI + Download Report
```

---

# 🏗️ Project Structure

```text
ai-root-cause-assistant-hackathon/
│
├── app.py              # Streamlit UI
├── agent.py            # LLM interaction logic
├── prompts.py          # Prompt templates
├── schemas.py          # Pydantic structured output
├── sample_bugs.py      # Demo test cases
├── utils.py            # JSON parsing + report builder
├── logger.py           # Logging configuration
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ How It Works

```text
1. User provides:
   - Code
   - Error / traceback
   - Expected behavior
   - Context

2. System builds prompt and sends to LLM

3. LLM returns structured debugging analysis

4. System validates output using Pydantic

5. Custom report is generated (input + output + metadata)

6. Report is displayed and can be downloaded
```

---

# 📦 Example Output (Simplified)

```json
{
  "timestamp": "...",
  "input": {
    "code": "...",
    "error": "TypeError...",
    "expected_behavior": "...",
    "context": "..."
  },
  "debug_report": {
    "root_cause": "...",
    "fixed_code": "...",
    "assumptions": [],
    "confidence_score": 90,
    "confidence_explanation": "..."
  }
}
```

---

# 🛠️ Tech Stack

* Python
* Streamlit
* OpenAI API
* Pydantic
* python-dotenv

---

# ▶️ Setup Instructions

## 1. Create virtual environment

```bash
python -m venv venv
```

## 2. Activate environment (Windows)

```bash
venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Create `.env` file

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

## 5. Run application

```bash
streamlit run app.py
```

---

# 🎥 Demo Flow

1. Open the app
2. Select **JavaScript ReferenceError** sample
3. Review auto-filled inputs
4. Click **Analyze Bug**
5. Show:

   * Root cause
   * Fixed code
   * Assumptions
   * Confidence explanation
6. Show session history
7. Download JSON report

---

# ⚠️ Limitations

* Does not execute code
* AI-generated fixes should be reviewed before use
* Accuracy depends on input quality

---

# 🚀 Future Scope

* Add code execution sandbox
* Add RAG using past debugging reports
* Integrate with GitHub issues / Jira
* Build team-level debugging knowledge base

---

# 🧠 Key Insight

This project is not just a debugging tool —
it is a **structured debugging report generator**, turning one-time AI responses into reusable knowledge.

---

