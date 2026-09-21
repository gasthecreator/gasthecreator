"""Builds assets/langs-{dark,light}.svg from real language byte counts across public, non-fork repos."""
import json, os, subprocess, urllib.request

OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "gasthecreator")
SKIP_REPOS = {OWNER}  # the profile repo itself
SKIP_LANGS = {"Makefile", "Dockerfile", "Go Template", "Edge", "Shell", "HTML", "CSS", "CQL"}
TOKEN = os.environ.get("GITHUB_TOKEN") or subprocess.run(["gh", "auth", "token"], capture_output=True, text=True).stdout.strip()

def api(path):
    req = urllib.request.Request(f"https://api.github.com{path}", headers={"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"})
    return json.load(urllib.request.urlopen(req))

totals = {}
for repo in api(f"/users/{OWNER}/repos?per_page=100&type=owner"):
    if repo["fork"] or repo["archived"] or repo["name"] in SKIP_REPOS:
        continue
    for lang, n in api(f"/repos/{OWNER}/{repo['name']}/languages").items():
        if lang not in SKIP_LANGS:
            totals[lang] = totals.get(lang, 0) + n

top = sorted(totals.items(), key=lambda kv: -kv[1])[:6]
total = sum(n for _, n in top)
PALETTE = ["#c4663f", "#8e7fd0", "#e0a15a", "#5f8fd0", "#b56fa6", "#6fb59a"]

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
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 {h}" width="720" height="{h}" role="img" aria-label="Languages by lines written across my public repositories">'
            f'<rect width="720" height="{h}" rx="16" fill="{bg}" stroke="{line}"/>'
            f'<text x="28" y="26" font-size="12" fill="{sub}" letter-spacing="2" font-family="ui-monospace,Menlo,monospace">LANGUAGES BY CODE WRITTEN</text>{rows}</svg>')

for dark in (True, False):
    open(f"assets/langs-{'dark' if dark else 'light'}.svg", "w").write(svg(dark))
print(top)
