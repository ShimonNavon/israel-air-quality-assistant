<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Israel Air Quality Assistant - README</title>
  <style>
    :root {
      --bg: #0b1020;
      --panel: #121933;
      --panel-2: #1a2244;
      --text: #edf2ff;
      --muted: #b9c3e6;
      --accent: #7cc4ff;
      --accent-2: #8ef0c7;
      --border: #2c3768;
      --code: #0f1530;
      --warn: #ffd166;
    }

    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Inter, Arial, Helvetica, sans-serif;
      background: linear-gradient(180deg, #0b1020 0%, #0f1730 100%);
      color: var(--text);
      line-height: 1.6;
    }

    .container {
      max-width: 980px;
      margin: 0 auto;
      padding: 40px 20px 80px;
    }

    .hero {
      background: linear-gradient(135deg, rgba(124,196,255,0.12), rgba(142,240,199,0.08));
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 28px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.25);
      margin-bottom: 24px;
    }

    h1, h2, h3 {
      line-height: 1.2;
      margin-top: 0;
    }

    h1 {
      font-size: 2.2rem;
      margin-bottom: 12px;
    }

    h2 {
      font-size: 1.35rem;
      margin-top: 34px;
      margin-bottom: 12px;
      color: var(--accent);
    }

    h3 {
      font-size: 1.05rem;
      margin-top: 22px;
      margin-bottom: 10px;
      color: var(--accent-2);
    }

    p, li {
      color: var(--muted);
      font-size: 1rem;
    }

    .tag {
      display: inline-block;
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(124,196,255,0.12);
      border: 1px solid var(--border);
      color: var(--text);
      font-size: 0.9rem;
      margin-right: 8px;
      margin-bottom: 8px;
    }

    .card {
      background: rgba(18,25,51,0.9);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 20px;
      margin-top: 16px;
    }

    code {
      background: rgba(124,196,255,0.08);
      padding: 2px 6px;
      border-radius: 6px;
      color: var(--text);
    }

    pre {
      background: var(--code);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 16px;
      overflow-x: auto;
      color: #dbe6ff;
      font-size: 0.95rem;
    }

    ul {
      padding-left: 22px;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
    }

    .note {
      border-left: 4px solid var(--warn);
      padding: 12px 14px;
      background: rgba(255,209,102,0.08);
      border-radius: 10px;
      color: var(--text);
    }

    .footer {
      margin-top: 36px;
      color: #97a6d8;
      font-size: 0.92rem;
      text-align: center;
    }

    .mono {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }
  </style>
</head>
<body>
  <div class="container">
    <section class="hero">
      <h1>Israel Air Quality Assistant</h1>
      <p>
        A small LangGraph-based project that demonstrates <strong>manual tool calling</strong>,
        <strong>structured outputs</strong>, and a simple <strong>workflow-driven assistant</strong>.
        The assistant accepts a city in Israel, retrieves air-quality data, interprets it, and returns
        structured health guidance instead of loose free-form text.
      </p>
      <div>
        <span class="tag">LangGraph</span>
        <span class="tag">LangChain Concepts</span>
        <span class="tag">Manual Tool Calling</span>
        <span class="tag">Structured Output</span>
        <span class="tag">Python</span>
      </div>
    </section>

    <section class="card">
      <h2>Project Goal</h2>
      <p>
        The goal of this project is to build a small assistant for Israeli cities that demonstrates
        how a workflow can explicitly call a tool, process the returned data, and produce a reliable
        structured result.
      </p>
      <p><strong>One-sentence version:</strong> We are building a small assistant that turns air-quality data for Israeli cities into reliable, structured health advice.</p>
    </section>

    <section class="card">
      <h2>Main Learning Goals</h2>
      <ul>
        <li><strong>Manual tool calling</strong> — the workflow explicitly calls the air-quality tool in code.</li>
        <li><strong>Structured outputs</strong> — the result follows a fixed schema instead of free text.</li>
        <li><strong>Basic LangGraph workflow design</strong> — the app is built as a simple graph with clear steps.</li>
      </ul>
    </section>

    <section class="card">
      <h2>How It Works</h2>
      <pre class="mono">User Input (city)
        ↓
LangGraph StateGraph
        ↓
fetch_air_quality node
        ↓
get_air_quality tool
        ↓
build_report node
        ↓
interpret_air_quality service
        ↓
Structured output shown to user</pre>
    </section>

    <section class="card">
      <h2>Project Structure</h2>
      <pre class="mono">israel-air-quality-assistant/
├── app/
│   ├── graph/
│   │   └── workflow.py
│   ├── tools/
│   │   └── air_quality.py
│   ├── schemas/
│   │   └── air_quality.py
│   ├── services/
│   │   └── interpreter.py
│   └── main.py
└── tests/</pre>
    </section>

    <section class="card">
      <h2>Core Components</h2>
      <div class="grid">
        <div class="card">
          <h3>Tool</h3>
          <p><code>get_air_quality(city)</code> retrieves air-quality data for a requested Israeli city.</p>
        </div>
        <div class="card">
          <h3>Interpreter</h3>
          <p><code>interpret_air_quality(city, aqi)</code> converts raw AQI into category, jogging safety, and advice.</p>
        </div>
        <div class="card">
          <h3>Schema</h3>
          <p><code>AirQualityReport</code> defines the structured output contract of the assistant.</p>
        </div>
        <div class="card">
          <h3>Workflow</h3>
          <p>The LangGraph workflow coordinates the nodes and state transitions from input to final output.</p>
        </div>
      </div>
    </section>

    <section class="card">
      <h2>Manual Tool Calling Explained</h2>
      <p>
        In this project, tool calling is <strong>manual</strong> because the developer explicitly decides
        when the tool is invoked and how the returned data is processed.
      </p>
      <pre class="mono">raw_result = get_air_quality(city)</pre>
      <p>
        That call is written directly in the workflow logic. The model is not autonomously deciding whether
        or when to call the tool. This is the central concept of the project.
      </p>
    </section>

    <section class="card">
      <h2>Structured Output Schema</h2>
      <p>The assistant returns a fixed result shape with fields such as:</p>
      <ul>
        <li><code>city</code></li>
        <li><code>aqi</code></li>
        <li><code>category</code></li>
        <li><code>jogging_safe</code></li>
        <li><code>advice</code></li>
      </ul>
      <p>This makes the output reliable, predictable, and easy to validate.</p>
    </section>

    <section class="card">
      <h2>Data Source Note</h2>
      <div class="note">
        The current live version may use modeled air-quality data rather than direct official station
        measurements. This is useful for demonstrating real external tool integration, but it is not the same
        as local government sensor-grade monitoring.
      </div>
    </section>

    <section class="card">
      <h2>How to Run</h2>
      <pre class="mono">.venv/bin/python -m app.main</pre>
      <p>The application will prompt for a city name and then return a structured air-quality report.</p>
    </section>

    <section class="card">
      <h2>Example Output</h2>
      <pre class="mono">Air Quality Report
------------------
City: Tel Aviv
AQI: 42
Category: Good
Jogging safe: True
Advice: Air quality is good. Outdoor activity is safe for most people.</pre>
    </section>

    <section class="card">
      <h2>Future Improvements</h2>
      <ul>
        <li>Replace modeled AQI with official Israeli monitoring station data.</li>
        <li>Add tests for interpretation logic and workflow behavior.</li>
        <li>Add a web interface or API layer.</li>
        <li>Expand the graph with validation and fallback nodes.</li>
      </ul>
    </section>

    <div class="footer">
      Built as a learning project for Manual Tool Calling Basics with LangGraph.
    </div>
  </div>
</body>
</html>
