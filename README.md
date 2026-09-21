<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg?v=3">
  <img src="assets/banner-light.svg?v=3" alt="Gideon Sanni, Software Engineer" width="100%">
</picture>

**I build fault-tolerant systems, Kubernetes automation, and AI pipelines that verify their own work.**

[Portfolio](https://gasthecreator.github.io/portfolio/) · [LinkedIn](https://www.linkedin.com/in/gideonadeniyisanni/) · [Email](mailto:gideonsanni2023@gmail.com) · [Résumé](https://gasthecreator.github.io/portfolio/assets/resume.pdf)

</div>

<br>

## Now

- **Solera Holdings, summer 2026.** Shipped two AI-driven pipelines that save 500+ engineering hours a month, built so AI-generated fixes must clear a failing-test proof and a human approval gate. The feedback pilot produced 127 AI-authored fix PRs.
- **Grambling State University.** B.S. in Computer Science & Cybersecurity, graduating May 2028.
- **Building.** Tripwire, automated exploit containment for DeFi protocols.

<br>

## Selected work

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/gasthecreator/pharos">Pharos</a></h3>
      <sub><code>Go</code> · <code>Kafka</code> · <code>Cassandra</code></sub>
      <p>Distributed adverse-event ingestion for clinical trials that survives site outages, duplicate retries and out-of-order events.</p>
      <b>101 ms p95</b> under multi-datacenter load. Five real correctness bugs caught before shipping.
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/gasthecreator/Cascade-Operator">Cascade Operator</a></h3>
      <sub><code>Go</code> · <code>Kubernetes</code> · <code>Istio / Linkerd</code></sub>
      <p>A Kubernetes operator that detects cascading failures and tightens the service mesh before they spread.</p>
      <b>63.2% → 31.8%</b> fan-out error rate in a live-cluster k6 benchmark.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/gasthecreator/tripwire">Tripwire</a></h3>
      <sub><code>Rust</code> · <code>Solidity</code> · <code>Foundry</code></sub>
      <p>A Rust detection engine that pauses a vault through an on-chain Guardian contract, taking response from human minutes to seconds.</p>
      <b>55 tests</b> across detection and contracts, including fuzzing and a live reentrancy simulation.
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/BE-Hackathon-2025/SafeLink-">SafeLink</a></h3>
      <sub><code>FastAPI</code> · <code>Bluetooth mesh</code> · <code>AI</code></sub>
      <p>Offline-first disaster alerts over a Bluetooth mesh. I built the real-time ingestion and dispatch backend.</p>
      <b>Top 5 of 64 teams</b>, with alert latency down 70%. <a href="https://safelink-dashboard.onrender.com/">Live demo</a>
    </td>
  </tr>
</table>

<br>

## Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg?v=3">
  <img src="assets/stack-light.svg?v=3" alt="Languages: Go, Python, TypeScript, Rust, C#, Solidity, SQL. Backend and data: Kafka, Cassandra, PostgreSQL, FastAPI, Node.js. Infrastructure: Kubernetes, Istio, Linkerd, Docker, Prometheus. AI and verification: LLM pipelines, xUnit and Jest, property testing, Foundry. Professional (Solera): C#, .NET, ASP.NET Core, xUnit, Open XML." width="760">
</picture>

<br>

## Languages

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/langs-dark.svg?v=3">
  <img src="assets/langs-light.svg?v=3" alt="Languages by lines I wrote across all my repositories: Go, JavaScript, TypeScript, Rust, SQL, Python and Solidity." width="720">
</picture>

<sub>Counted from commits I authored across all my repositories, including private and team work. My Solera work (C# / .NET) lives in private employer repos and isn't counted here.</sub>

<br>

## How I work

I like problems where the failure modes are the interesting part: partitions, retries, cascades, exploits. I test against real infrastructure instead of mocks, write down what a system does *not* claim, and prefer proof over confidence.

<br>

<div align="center">

<sub>Let's build something that keeps working.</sub>

</div>
