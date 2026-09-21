"""Builds assets/langs-{dark,light}.svg from the lines I authored, across every repo I can access (public, private, org).

Run locally (needs the gh CLI, logged in with repo access):  python3 langs.py
Only the aggregate percentages are published. Repo names and code never leave the machine.
"""
import collections, os, re, subprocess, tempfile

REPOS = ["gasthecreator/Cascade-Operator", "gasthecreator/disaster-sentinel", "gasthecreator/Leetcode", "gasthecreator/pharos",
         "gasthecreator/portfolio", "gasthecreator/tripwire", "Praecept-ai/praecept", "Praecept-ai/api", "Praecept-ai/prototype"]
AUTHORS = ["gideonsanni2023@gmail.com", "gsanni@Gideons"]
LANG = {".py": "Python", ".js": "JavaScript", ".jsx": "JavaScript", ".mjs": "JavaScript", ".cjs": "JavaScript", ".ts": "TypeScript",
        ".tsx": "TypeScript", ".go": "Go", ".rs": "Rust", ".sol": "Solidity", ".sql": "SQL"}
SKIP = re.compile(r"(node_modules|vendor|dist/|build/|\.min\.|lock|generated|zz_|\.pb\.|snapshots?/|fixtures?/|/data/)", re.I)
PALETTE = ["#c4663f", "#8e7fd0", "#e0a15a", "#5f8fd0", "#b56fa6", "#6fb59a", "#9aa5c8"]

totals = collections.Counter()
with tempfile.TemporaryDirectory() as tmp:
    for repo in REPOS:
        dest = os.path.join(tmp, repo.split("/")[1])
        subprocess.run(["gh", "repo", "clone", repo, dest, "--", "-q"], capture_output=True)
        args = ["git", "-C", dest, "log", "--all", "--no-merges", "--numstat", "--format="] + [f"--author={a}" for a in AUTHORS]
        for line in subprocess.run(args, capture_output=True, text=True).stdout.splitlines():
            parts = line.split("\t")
            if len(parts) != 3 or parts[0] == "-" or SKIP.search(parts[2]):
                continue
            lang = LANG.get(os.path.splitext(parts[2])[1].lower())
            if lang:
                totals[lang] += int(parts[0])

top = totals.most_common(7)
total = sum(n for _, n in top)

def svg(dark):
    bg, line, txt, sub, track = ("#12122c", "#2f2b57", "#f4efe6", "#a9a3d6", "#1e1b40") if dark else ("#f4f8fd", "#cbd8ea", "#1a2350", "#4c5a8a", "#e4edf9")
    rows, y = "", 40
    for i, (lang, n) in enumerate(top):
        pct = n / total * 100
        w = max(8, 470 * pct / 100)
        rows += (f'<text x="28" y="{y+13}" font-size="14" fill="{txt}" font-family="-apple-system,Segoe UI,Helvetica,sans-serif">{lang}</text>'
                 f'<rect x="150" y="{y}" width="470" height="18" rx="9" fill="{track}"/>'
                 f'<rect x="150" y="{y}" width="{w:.0f}" height="18" rx="9" fill="{PALETTE[i]}"/>'
                 f'<text x="640" y="{y+13}" font-size="13" fill="{sub}" font-family="ui-monospace,Menlo,monospace">{pct:.1f}%</text>')
        y += 34
    h = y + 6
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 {h}" width="720" height="{h}" role="img" aria-label="Languages by lines I wrote across all my repositories">'
            f'<rect width="720" height="{h}" rx="16" fill="{bg}" stroke="{line}"/>'
            f'<text x="28" y="26" font-size="12" fill="{sub}" letter-spacing="2" font-family="ui-monospace,Menlo,monospace">LANGUAGES BY LINES I WROTE</text>{rows}</svg>')

for dark in (True, False):
    open(f"assets/langs-{'dark' if dark else 'light'}.svg", "w").write(svg(dark))
print([(k, v, round(v / total * 100, 1)) for k, v in top])
