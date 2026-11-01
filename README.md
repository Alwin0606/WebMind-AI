# 🌐 WebMind AI
### Beyond Search. Into Intelligence.

<p align="center">
  <strong>AI-Powered Web Research & Intelligence Platform</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/TypeScript-Frontend-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/Vite-Build%20Tool-646CFF?style=for-the-badge&logo=vite&logoColor=white" />
</p>

<p align="center">
  <em>Transforming scattered web information into structured research intelligence.</em>
</p>

---

## 🚀 Overview

**WebMind AI** is a web intelligence and research platform designed to go beyond traditional search engines.

It combines web search, webpage extraction, content analysis, multi-source research, claim relevance assessment, and automated report generation into one unified workspace.

Instead of simply collecting links, WebMind AI helps users retrieve information, analyze source content, organize findings, and generate structured research reports.

### 🎯 Vision

Build an intelligent research environment that makes discovering, analyzing, and organizing information faster and more accessible.

---

## ✨ Core Features

| Module | Capabilities |
|---|---|
| 🔎 Web Search | Retrieve relevant web search results |
| 🕷️ Web Crawler | Extract readable content from webpages |
| 🧠 Content Intelligence | Analyze text, identify keywords, and generate extractive summaries |
| 🤖 Research Agent | Conduct multi-source research and consolidate findings |
| 🛡️ Claim Verification | Assess keyword relevance between claims and source content |
| 📄 Report Generator | Generate research reports in PDF and Markdown formats |
| 📊 Research Workspace | Access research modules through a unified dashboard |

### 🔎 Intelligent Web Search
- Search the web using a dedicated search engine integration.
- Retrieve titles, URLs, and descriptions.
- Organize search results for further investigation.

### 🕷️ Web Content Extraction
- Retrieve webpage content.
- Extract readable text from supported HTML pages.
- Apply URL validation and request-size restrictions.

### 🧠 Content Intelligence
- Extract important keywords.
- Analyze text structure and statistics.
- Generate extractive summaries.
- Estimate reading time.

### 🤖 Autonomous Research Agent
- Search for information across multiple sources.
- Retrieve and analyze available webpage content.
- Assess source relevance.
- Consolidate research findings.
- Report retrieval failures and limitations.

### 🛡️ Claim Relevance Assessment
- Compare a claim against supplied source content.
- Identify matched and missing keywords.
- Calculate a keyword-overlap score.
- Provide a relevance classification.

> **Important:** Keyword overlap is not factual verification. A high relevance score does not prove that a claim is true.

### 📄 Automated Research Reports
- Generate PDF reports.
- Generate Markdown reports.
- Organize research findings into structured output.

---

## 🏗️ System Architecture

```text
                 WEBMIND AI
                      |
          React + TypeScript Frontend
                      |
               Vite Development
                      |
                FastAPI Backend
                      |
       +--------------+--------------+
       |              |              |
    Web Search     Web Crawler    Intelligence
       |              |              |
       +--------------+--------------+
                      |
              Research Agent
                      |
             Relevance Assessment
                      |
               Report Generator
                      |
                PDF / Markdown
```

### Technology Stack

**Frontend**
- React
- TypeScript
- Vite
- CSS
- Lucide React

**Backend**
- Python 3.13
- FastAPI
- Uvicorn
- Requests
- BeautifulSoup
- Trafilatura
- DDGS
- ReportLab

---

## 📂 Project Structure

```text
WebMind-AI/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   └── research_agent.py
│   │   │
│   │   ├── crawler/
│   │   │   └── engine.py
│   │   │
│   │   ├── intelligence/
│   │   │   └── analyzer.py
│   │   │
│   │   ├── reports/
│   │   │   └── builder.py
│   │   │
│   │   ├── search/
│   │   │   └── engine.py
│   │   │
│   │   ├── verification/
│   │   │   ├── engine.py
│   │   │   └── routes.py
│   │   │
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   │
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.ts
│
├── docs/
│
├── .gitignore
├── LICENSE
└── README.md
```

*The structure above illustrates the main project modules. Include additional files and configuration folders as they are added to the repository.*

---

## ⚙️ Installation & Setup

### Prerequisites

Make sure you have installed:

- Python 3.13
- Node.js and npm
- Git
- Visual Studio Code

### 1. Clone the Repository

```bash
git clone https://github.com/Alwin0606/WebMind-AI.git

cd WebMind-AI
```

### 2. Set Up the Backend

Create a virtual environment:

```powershell
py -3.13 -m venv backend\.venv
```

Activate it:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.\backend\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r backend\requirements.txt
```

Start the backend:

```powershell
python -m uvicorn backend.app.main:app --reload
```

Backend URL:

`http://127.0.0.1:8000`

### 3. Set Up the Frontend

Open another terminal:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm.cmd install
```

Start the frontend:

```powershell
npm.cmd run dev
```

Frontend URL:

`http://127.0.0.1:5173`

---

## 🔌 API Reference

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Backend health status |
| GET | `/api/v1/search/` | Web search |
| POST | `/api/v1/research/run` | Autonomous research |
| POST | `/api/v1/verification/verify` | Claim relevance assessment |
| POST | `/api/v1/reports/generate` | PDF or Markdown report generation |

### Interactive API Documentation

FastAPI automatically provides interactive API documentation:

`http://127.0.0.1:8000/docs`

Use Swagger UI to inspect endpoints and test API requests.

---

## 🔐 Security Considerations

WebMind AI includes initial URL validation and webpage retrieval safeguards.

Security measures include:
- HTTP/HTTPS URL validation.
- Rejection of local and non-public IP destinations.
- Request timeouts.
- Response-size limits.
- HTML content-type validation.
- Redirects disabled during webpage retrieval.

**Production hardening still required:** DNS rebinding protection, controlled network egress, stronger rate limiting, concurrency limits, authentication, and deployment security reviews.

---

## 🧪 Current Implementation & Limitations

WebMind AI is an actively developing project.

The current implementation uses:
- Search-engine retrieval.
- Rule-based text analysis.
- Extractive summarization.
- Keyword-overlap relevance assessment.
- Multi-source research orchestration.
- PDF and Markdown report generation.

It does not currently claim to provide definitive fact-checking or LLM-powered reasoning. Research quality depends on source availability, extraction success, and the relevance of retrieved content.

---

## 🛣️ Future Roadmap

- [ ] LLM-powered research and summarization.
- [ ] Retrieval-Augmented Generation (RAG).
- [ ] Vector database integration.
- [ ] PostgreSQL persistent storage.
- [ ] User authentication and role management.
- [ ] Advanced source credibility analysis.
- [ ] Evidence-based claim verification.
- [ ] Research history and saved projects.
- [ ] Docker-based deployment.
- [ ] Cloud deployment and scalability improvements.

---

## 🎯 Use Cases

- Academic and technical research.
- Market and industry research.
- Technology trend analysis.
- Multi-source information gathering.
- Content investigation.
- Structured research documentation.

---

## 👨‍💻 Developer

**Developed as an AI-powered web intelligence and research platform.**

GitHub: [Alwin0606](https://github.com/Alwin0606)

Repository: [WebMind AI](https://github.com/Alwin0606/WebMind-AI)

---

## 📜 License

Refer to the repository's `LICENSE` file for licensing terms.

---

<p align="center">
  <strong>🌐 WebMind AI</strong>
  <br/>
  <em>Beyond Search. Into Intelligence.</em>
  <br/><br/>
  Built to make web research smarter, structured, and more accessible.
</p>
