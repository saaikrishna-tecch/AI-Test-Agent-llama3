# AI-Test-Agent-llama3
# 🚀 Offline AI Test Script Generator

An intelligent **offline Generative AI agent** that converts manual test steps into **automation scripts** using Selenium, Cucumber, and TestNG.

This project leverages a **local LLM (via Ollama)** to generate test scripts, validate results, and suggest fixes — all without internet dependency.

---

## 🧠 Features

* ✅ Generate Selenium automation scripts from test steps
* ✅ Supports **Actual vs Expected validation**
* ✅ Generates:

  * Cucumber Feature Files
  * Java Step Definitions
  * Selenium Test Code
* ✅ Suggests fixes for failed test cases
* ✅ Works completely **offline using local LLM**
* ✅ Simple UI using Streamlit

---

## ⚙️ Tech Stack

* **Python** – Backend logic
* **Ollama (Local LLM)** – AI code generation
* **LangChain** – LLM integration
* **Streamlit** – User interface
* **Selenium + Cucumber + TestNG** – Test automation

---

## 🏗️ Project Architecture

```
User Input (Test Steps + Actual/Expected)
                ↓
        Python AI Agent
                ↓
        Local LLM (Ollama)
                ↓
        Code Generation Engine
                ↓
   Selenium + Cucumber Scripts
```

---

## 📥 Input Example

```
Tes
```
