# 🤖 Text Summarization Agent

An AI-powered text summarization agent built using Google's Agent Development 
Kit (ADK) and Gemini 2.0 Flash, deployed on Google Cloud Run.

## ✨ Features
- Summarizes any text in 3 styles:
  - **Concise** — 2-3 sentence summary
  - **Bullet** — key points as bullet list
  - **Detailed** — comprehensive paragraph summary
- Built with ADK's tool-calling architecture
- Deployed as a live web app on Cloud Run

## 🛠 Tech Stack
- Google Agent Development Kit (ADK)
- Gemini 2.0 Flash (LLM)
- Python 3.12
- Google Cloud Run (deployment)
- Vertex AI

## 🔄 Workflow
1. User provides text and optional style (concise/bullet/detailed)
2. Agent calls the `summarize_text` tool to validate input
3. Tool returns processed text back to the agent
4. Gemini LLM generates the summary based on style
5. Agent returns clean, structured summary to the user

## 🚀 Live Demo
https://text-summarizer-784066446437.us-central1.run.app
```

---

### 🔄 Workflow Diagram (for LinkedIn post)
```
User Input (text + style)
        ↓
Text Summarizer Agent (Gemini 2.0 Flash)
        ↓
calls → summarize_text tool
        ↓
validates input → returns text + style + char_count
        ↓
LLM generates summary based on style
        ↓
User receives clean summary ✅
```

---

### 💼 Resume One-liner
```
Built and deployed a Text Summarization Agent using Google ADK, 
Gemini 2.0 Flash, and Cloud Run — supporting concise, bullet, 
and detailed summarization styles via tool-calling architecture.
```

---

### 📣 LinkedIn Caption (for your post around March 31)
```
🚀 Built my first AI Agent using Google's Agent Development Kit (ADK)!

A Text Summarization Agent powered by Gemini 2.0 Flash — deployed 
live on Google Cloud Run.

🔧 How it works:
→ User sends text
→ Agent calls a custom tool to validate input
→ Gemini generates a concise, bullet, or detailed summary

Tech: Google ADK | Gemini 2.0 Flash | Cloud Run | Python | Vertex AI

🔗 Live Demo: [[Text Summarizer Agent](https://text-summarizer-784066446437.us-central1.run.app)]


#AIAgents #GoogleADK #Gemini #CloudRun #Python #GenerativeAI
