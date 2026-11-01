import { useEffect, useState } from "react";
import {
  Activity, Search, BrainCircuit, ShieldCheck, FileText,
  LayoutDashboard, Globe, Zap, ArrowUpRight, Loader2,
  CircleCheck, CircleAlert, Menu
} from "lucide-react";

import {
  checkHealth, searchWeb, runResearch,
  verifyClaim, generateReport
} from "./services/api";

type Tab = "overview" | "search" | "research" | "verify" | "reports";

function App() {
  const [activeTab, setActiveTab] = useState<Tab>("overview");
  const [apiStatus, setApiStatus] = useState("Checking");
  const [query, setQuery] = useState("");
  const [claim, setClaim] = useState("");
  const [reportQuestion, setReportQuestion] = useState("");
  const [result, setResult] = useState<unknown>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    checkHealth()
      .then(() => setApiStatus("Online"))
      .catch(() => setApiStatus("Offline"));
  }, []);

  function changeTab(tab: Tab) {
    setActiveTab(tab);
    setResult(null);
    setError("");
  }

  async function execute(action: () => Promise<unknown>) {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const data = await action();
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }

  const navigation = [
    { id: "overview" as Tab, label: "Overview", icon: LayoutDashboard },
    { id: "search" as Tab, label: "Web Search", icon: Search },
    { id: "research" as Tab, label: "Research Agent", icon: BrainCircuit },
    { id: "verify" as Tab, label: "Claim Verification", icon: ShieldCheck },
    { id: "reports" as Tab, label: "Reports", icon: FileText }
  ];

  const descriptions: Record<Tab, string> = {
    overview: "Your central intelligence workspace.",
    search: "Discover information across the public web.",
    research: "Investigate a topic using multiple web sources.",
    verify: "Examine claims against retrieved source evidence.",
    reports: "Generate downloadable research reports."
  };

  return (
    <div className="workspace">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-icon"><BrainCircuit size={25} /></div>
          <div>
            <h2>WEBMIND<span> AI</span></h2>
            <small>INTELLIGENCE PLATFORM</small>
          </div>
        </div>

        <div className="nav-label">WORKSPACE</div>

        <nav>
          {navigation.map(({ id, label, icon: Icon }) => (
            <button
              key={id}
              className={`nav-item ${activeTab === id ? "active" : ""}`}
              onClick={() => changeTab(id)}
            >
              <Icon size={18} />
              <span>{label}</span>
              {activeTab === id && <ArrowUpRight size={15} />}
            </button>
          ))}
        </nav>

        <div className="sidebar-bottom">
          <div className="connection">
            <span className={`status-dot ${apiStatus === "Online" ? "online" : ""}`} />
            <div>
              <strong>Backend API</strong>
              <small>{apiStatus}</small>
            </div>
          </div>
          <p>WEBMIND AI · VERSION 1.0</p>
        </div>
      </aside>

      <main className="main-area">
        <header className="topbar">
          <div className="breadcrumb">
            <Menu size={18} />
            <span>Workspace</span>
            <span className="breadcrumb-separator">/</span>
            <strong>{navigation.find(item => item.id === activeTab)?.label}</strong>
          </div>
          <div className="topbar-right">
            <span className="live-indicator"><span /> SYSTEM {apiStatus.toUpperCase()}</span>
          </div>
        </header>

        <div className="page-content">
          <div className="page-heading">
            <div>
              <div className="eyebrow">INTELLIGENCE WORKSPACE</div>
              <h1>
                {activeTab === "overview" ? "Welcome to WebMind AI" :
                 navigation.find(item => item.id === activeTab)?.label}
              </h1>
              <p>{descriptions[activeTab]}</p>
            </div>
            <div className="date-chip"><Activity size={15} /> LIVE WORKSPACE</div>
          </div>

          {activeTab === "overview" && (
            <>
              <section className="hero-panel">
                <div className="hero-content">
                  <div className="hero-tag"><Zap size={14} /> AI-POWERED WEB INTELLIGENCE</div>
                  <h2>Beyond Search.<br /><span>Into Intelligence.</span></h2>
                  <p>
                    Search, investigate, analyze and organize web information
                    through one unified research workspace.
                  </p>
                  <button className="primary-button" onClick={() => changeTab("research")}>
                    Start a Research <ArrowUpRight size={17} />
                  </button>
                </div>
                <div className="hero-graphic">
                  <div className="orbit orbit-one" />
                  <div className="orbit orbit-two" />
                  <div className="core"><BrainCircuit size={52} /></div>
                  <div className="orbit-node node-one"><Search /></div>
                  <div className="orbit-node node-two"><Globe /></div>
                  <div className="orbit-node node-three"><ShieldCheck /></div>
                </div>
              </section>

              <div className="section-heading">
                <div>
                  <h2>Intelligence Modules</h2>
                  <p>Explore the platform capabilities</p>
                </div>
              </div>

              <div className="module-grid">
                {[
                  { id: "search" as Tab, icon: Search, title: "Web Search", text: "Retrieve relevant web search results.", color: "cyan" },
                  { id: "research" as Tab, icon: BrainCircuit, title: "Research Agent", text: "Collect and analyze multiple sources.", color: "purple" },
                  { id: "verify" as Tab, icon: ShieldCheck, title: "Claim Verification", text: "Assess claims using retrieved evidence.", color: "green" },
                  { id: "reports" as Tab, icon: FileText, title: "Report Builder", text: "Generate PDF and Markdown reports.", color: "orange" }
                ].map(({ id, icon: Icon, title, text, color }) => (
                  <button className="module-card" key={id} onClick={() => changeTab(id)}>
                    <div className={`module-icon ${color}`}><Icon size={22} /></div>
                    <h3>{title}</h3>
                    <p>{text}</p>
                    <span className="module-link">Open module <ArrowUpRight size={15} /></span>
                  </button>
                ))}
              </div>
            </>
          )}

          {activeTab === "search" && (
            <section className="tool-panel">
              <div className="panel-icon cyan"><Search /></div>
              <h2>Web Intelligence Search</h2>
              <p>Enter a topic to retrieve relevant web sources.</p>
              <form onSubmit={e => { e.preventDefault(); execute(() => searchWeb(query)); }}>
                <input value={query} onChange={e => setQuery(e.target.value)}
                  placeholder="Example: Latest developments in artificial intelligence" />
                <button className="primary-button" disabled={loading || !query.trim()}>
                  {loading ? <Loader2 className="spin" /> : <Search size={17} />}
                  Search Web
                </button>
              </form>
            </section>
          )}

          {activeTab === "research" && (
            <section className="tool-panel">
              <div className="panel-icon purple"><BrainCircuit /></div>
              <h2>Autonomous Research Agent</h2>
              <p>Investigate a question and collect information from multiple sources.</p>
              <form onSubmit={e => { e.preventDefault(); execute(() => runResearch(query)); }}>
                <textarea value={query} onChange={e => setQuery(e.target.value)}
                  placeholder="Enter a detailed research question..." rows={5} />
                <button className="primary-button" disabled={loading || query.trim().length < 5}>
                  {loading ? <Loader2 className="spin" /> : <BrainCircuit size={17} />}
                  Run Research
                </button>
              </form>
            </section>
          )}

          {activeTab === "verify" && (
            <section className="tool-panel">
              <div className="panel-icon green"><ShieldCheck /></div>
              <h2>Evidence Assessment</h2>
              <p>Submit a claim to find and assess relevant web evidence. This tool does not establish definitive truth.</p>
              <form onSubmit={e => { e.preventDefault(); execute(() => verifyClaim(claim)); }}>
                <textarea value={claim} onChange={e => setClaim(e.target.value)}
                  placeholder="Enter the claim you want to examine..." rows={5} />
                <button className="primary-button" disabled={loading || claim.trim().length < 5}>
                  {loading ? <Loader2 className="spin" /> : <ShieldCheck size={17} />}
                  Assess Claim
                </button>
              </form>
            </section>
          )}

          {activeTab === "reports" && (
            <section className="tool-panel">
              <div className="panel-icon orange"><FileText /></div>
              <h2>Research Report Generator</h2>
              <p>Run research and export the resulting report.</p>
              <textarea value={reportQuestion} onChange={e => setReportQuestion(e.target.value)}
                placeholder="Enter your report topic or research question..." rows={5} />
              <div className="report-actions">
                <button className="primary-button" disabled={loading || reportQuestion.trim().length < 5}
                  onClick={() => execute(() => generateReport(reportQuestion, "pdf"))}>
                  {loading ? <Loader2 className="spin" /> : <FileText size={17} />}
                  Generate PDF
                </button>
                <button className="secondary-button" disabled={loading || reportQuestion.trim().length < 5}
                  onClick={() => execute(() => generateReport(reportQuestion, "markdown"))}>
                  Generate Markdown
                </button>
              </div>
            </section>
          )}

          {loading && (
            <div className="loading-panel"><Loader2 className="spin" /> Processing your request...</div>
          )}

          {error && (
            <div className="error-panel">
              <CircleAlert size={19} />
              <div><strong>Request failed</strong><p>{error}</p></div>
            </div>
          )}

          {result !== null && (
            <section className="result-panel">
              <div className="result-heading">
                <div><CircleCheck size={19} /><strong>Response received</strong></div>
                <span>API RESULT</span>
              </div>
              <pre>{typeof result === "string" ? result : JSON.stringify(result, null, 2)}</pre>
            </section>
          )}

          <footer>
            <span>WEBMIND AI</span>
            <span>Beyond Search. Into Intelligence.</span>
            <span>Research workspace · 2026</span>
          </footer>
        </div>
      </main>
    </div>
  );
}

export default App;
