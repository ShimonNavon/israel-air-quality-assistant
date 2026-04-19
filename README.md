<div align="center">

# Israel Air Quality Assistant

<p>
  A small <strong>LangGraph-based</strong> project that demonstrates
  <strong>manual tool calling</strong>, <strong>structured outputs</strong>,
  and a simple <strong>workflow-driven assistant</strong>.
</p>

<p>
  The assistant accepts a city in Israel, retrieves air-quality data,
  interprets it, and returns structured health guidance instead of loose text.
</p>

<p>
  <img alt="LangGraph" src="https://img.shields.io/badge/LangGraph-Workflow-blue">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-green">
  <img alt="Structured Output" src="https://img.shields.io/badge/Output-Structured-orange">
  <img alt="Tool Calling" src="https://img.shields.io/badge/Tool%20Calling-Manual-purple">
</p>

</div>

---

## Project Goal

The goal of this project is to build a small assistant for Israeli cities that demonstrates how a workflow can explicitly call a tool, process the returned data, and produce a reliable structured result.

<p><strong>One-sentence version:</strong> We are building a small assistant that turns air-quality data for Israeli cities into reliable, structured health advice.</p>

---

## Main Learning Goals

<ul>
  <li><strong>Manual tool calling</strong> — the workflow explicitly calls the air-quality tool in code.</li>
  <li><strong>Structured outputs</strong> — the result follows a fixed schema instead of free text.</li>
  <li><strong>Basic LangGraph workflow design</strong> — the app is built as a simple graph with clear steps.</li>
</ul>

---

## How It Works

<pre>
User Input (city)
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
Structured output shown to user
</pre>

---

## Project Structure

<pre>
israel-air-quality-assistant/
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
└── tests/
</pre>

---

## Core Components

<table>
  <tr>
    <th align="left">Component</th>
    <th align="left">Purpose</th>
  </tr>
  <tr>
    <td><code>get_air_quality(city)</code></td>
    <td>Retrieves air-quality data for a requested Israeli city.</td>
  </tr>
  <tr>
    <td><code>interpret_air_quality(city, aqi)</code></td>
    <td>Converts raw AQI into category, jogging safety, and health advice.</td>
  </tr>
  <tr>
    <td><code>AirQualityReport</code></td>
    <td>Defines the structured output contract of the assistant.</td>
  </tr>
  <tr>
    <td>LangGraph workflow</td>
    <td>Coordinates the nodes and state transitions from input to final output.</td>
  </tr>
</table>

---

## Manual Tool Calling Explained

In this project, tool calling is <strong>manual</strong> because the developer explicitly decides when the tool is invoked and how the returned data is processed.

<pre><code>raw_result = get_air_quality(city)</code></pre>

That call is written directly in the workflow logic. The model is not autonomously deciding whether or when to call the tool. This is the central concept of the project.

---

## Structured Output Schema

The assistant returns a fixed result shape with fields such as:

<ul>
  <li><code>city</code></li>
  <li><code>aqi</code></li>
  <li><code>category</code></li>
  <li><code>jogging_safe</code></li>
  <li><code>advice</code></li>
</ul>

This makes the output reliable, predictable, and easy to validate.

---

## How to Run

<pre><code>.venv/bin/python -m app.main</code></pre>

The application will prompt for a city name and then return a structured air-quality report.

---

## Example Output

<pre>
Air Quality Report
------------------
City: Tel Aviv
AQI: 42
Category: Good
Jogging safe: True
Advice: Air quality is good. Outdoor activity is safe for most people.
</pre>

---

## Notes on Data Source

<blockquote>
  The live version may use modeled air-quality data rather than direct official station measurements.
  This is useful for demonstrating real external tool integration, but it is not the same as local
  government sensor-grade monitoring.
</blockquote>

---

## Future Improvements

<ul>
  <li>Replace modeled AQI with official Israeli monitoring station data.</li>
  <li>Add tests for interpretation logic and workflow behavior.</li>
  <li>Add a web interface or API layer.</li>
  <li>Expand the graph with validation and fallback nodes.</li>
</ul>

---

<div align="center">
  Built as a learning project for <strong>Manual Tool Calling Basics</strong> with <strong>LangGraph</strong>.
</div>
