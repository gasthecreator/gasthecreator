<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg?v=7">
  <img src="assets/banner-light.svg?v=7" alt="Gideon Sanni, Software Engineer" width="100%">
</picture>

**I build fault-tolerant systems, Kubernetes automation, and AI pipelines that verify their own work.**

[Portfolio](https://gasthecreator.github.io/portfolio/) · [LinkedIn](https://www.linkedin.com/in/gideonadeniyisanni/) · [Email](mailto:gideonsanni2023@gmail.com) · [Résumé](https://gasthecreator.github.io/portfolio/assets/resume.pdf)

</div>

<br>

## Now

- **Solera Holdings, summer 2026.** Engineered two automation workflows in C# and .NET, including an approval-triggered AI feedback pilot that generated 127 fix pull requests and 300+ issues for one target repository. AI fixes were blocked unless a failing test proved them.
- **Grambling State University.** B.S. in Computer Science, graduating May 2028.
- **Building.** SafeLink (offline-first emergency app), TierFS (tiered storage for macOS), Vigil (breast-cancer follow-up research) and Tripwire (DeFi exploit containment).
- **Ask my portfolio.** [My website](https://gasthecreator.github.io/portfolio/) has an AI assistant (the "Ask about Gideon" button) that answers questions about my projects, skills and experience. It runs Gemma 4 on Cloudflare Workers AI behind a rate-limited Worker, answers only from the site's own content, and says so when it doesn't know. Its code and test set are in [`worker/`](https://github.com/gasthecreator/portfolio/tree/main/worker).

<br>

## Selected work

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Feedback Automation Pipeline</h3>
      <sub><code>.NET 10</code> · <code>Kubernetes</code> · <code>GitHub Actions</code></sub>
      <p>A Solera pilot that gives user feedback a much faster path to a reviewable fix: after a single approval, it produces an AI-generated pull request, with lease-based reliability and a failing-test proof gate.</p>
      <b>127 AI-authored fix PRs</b> and 300+ issues for one target repository. Internal project.
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://praecept.ai">Praecept</a></h3>
      <sub><code>Node.js</code> · <code>Supabase Auth</code> · <code>LLM pipeline</code></sub>
      <p>A verified map of common-law doctrine that lawyers can read and reason from. I built the production auth system and the LLM extraction pipeline behind its review workflow.</p>
      <b>Live at praecept.ai</b>, by invitation. Source is private.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/gasthecreator/safelink-sentinel">SafeLink</a></h3>
      <sub><code>React Native</code> · <code>BLE</code> · <code>Swift / Kotlin</code></sub>
      <p>An offline-first emergency app: phones relay help requests and road closures over Bluetooth and give directions from maps stored on the phone. It began at the BE Smart Hackathon, where I built the FastAPI backend.</p>
      <b>Top 5 of 64 teams.</b> Offline A* routing matches an independent Dijkstra search within 1 s across 40 seeded trips per mode. Pre-release: not yet tested between two real phones.
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
      <h3><a href="https://github.com/gasthecreator/tierfs">TierFS</a></h3>
      <sub><code>C/C++17</code> · <code>FUSE-T</code> · <code>AES-256-GCM</code></sub>
      <p>A tiered-storage filesystem for macOS that offloads cold files to other devices and recalls them on demand, and never trusts a copy it has not verified. Crash-injection and mutation-tested engines.</p>
      <b>Work in progress:</b> the FUSE mount layer is still unproven.
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/gasthecreator/vigil">Vigil</a></h3>
      <sub><code>Python</code> · <code>PyTorch</code> · <code>JAX</code></sub>
      <p>A research platform for breast-cancer follow-up that estimates tumor kinetics from lab trends with neural posterior estimators and censor-aware evaluation.</p>
      <b>0.79 IPCW AUC at best</b> (XGBoost, synthetic cohorts). Research prototype, not a medical device.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/gasthecreator/pharos">Pharos</a></h3>
      <sub><code>Go</code> · <code>Kafka</code> · <code>Cassandra</code></sub>
      <p>Distributed adverse-event ingestion for clinical trials that survives site outages, duplicate retries and out-of-order events.</p>
      <b>101 ms p95</b> under multi-datacenter load. Five real correctness bugs caught before shipping.
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/gasthecreator/tripwire">Tripwire</a></h3>
      <sub><code>Rust</code> · <code>Solidity</code> · <code>Foundry</code></sub>
      <p>A Rust detection engine that pauses a vault through an on-chain Guardian contract, taking response from human minutes to seconds.</p>
      <b>257 passing tests</b> (220 Rust, 37 Foundry), including fuzzing, replays of four historical exploits and a live reentrancy simulation.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://gasthecreator.github.io/portfolio/#archive">More in the archive</a></h3>
      <sub><code>Release Checklist Automation</code> · <code>The Refraction</code></sub>
      <p>The rest of the archive is on my portfolio.</p>
      <a href="https://gasthecreator.github.io/portfolio/">Open the portfolio</a>
    </td>
  </tr>
</table>

<br>

## Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg?v=7">
  <img src="assets/stack-light.svg?v=7" alt="Languages: Python, TypeScript, Go, Rust, C and C++, C#, Java, JavaScript, SQL, Solidity, Swift, Kotlin. Backend and data: FastAPI, Node.js, Express, ASP.NET Core, .NET, PostgreSQL, SQLite, Supabase, Redis, Kafka, Cassandra. Infrastructure: Kubernetes, Docker, Prometheus, OpenTelemetry, Istio, Linkerd. AI and ML: PyTorch, scikit-learn, XGBoost, JAX, NumPyro/NUTS, ONNX Runtime. Agentic tools: LLM agents, MCP, Claude, Cursor, GitHub Copilot, Gemini, Antigravity, OpenAI Codex. Mobile and verification: React Native, Foundry, Alloy." width="760">
</picture>

<br>

## Languages

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/langs-dark.svg?v=7">
  <img src="assets/langs-light.svg?v=7" alt="Languages by lines committed under my name across all my repositories: Python, Go, JavaScript, C and C++, TypeScript, Rust and Solidity." width="720">
</picture>

<sub>Counted from commits under my name across all my repositories, including private and team work and code written with AI coding agents. My Solera work (C# / .NET) lives in private employer repos and isn't counted here.</sub>

<br>

## How I work

I like problems where the failure modes are the interesting part: partitions, retries, cascades, exploits. I test against real infrastructure instead of mocks, write down what a system does *not* claim, and prefer proof over confidence.

<br>

<div align="center">

<sub>Let's build something that keeps working.</sub>

</div>
