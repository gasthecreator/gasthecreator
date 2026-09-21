import random, math
random.seed(7)
W,H=1200,320
def ridge(seed,base,amp,color,op=1):
    r=random.Random(seed); pts=[]
    ph=[r.random()*6 for _ in range(3)]
    for x in range(0,W+20,20):
        y=base+amp*(math.sin(x/170+ph[0])*.55+math.sin(x/70+ph[1])*.3+math.sin(x/33+ph[2])*.15)
        pts.append(f"{x},{y:.1f}")
    return f'<polygon fill="{color}" opacity="{op}" points="0,{H} {" ".join(pts)} {W},{H}"/>'
def banner(dark):
    if dark:
        sky=[("0","#090b26"),("0.55","#241a4a"),("0.85","#6a3a55"),("1","#c4663f")]
        ridges=[(1,238,14,"#3a2748",.95),(2,262,16,"#241a3d",1),(3,286,14,"#120f2a",1)]
        title="#f4efe6"; sub="#c9c3e6"; chip="#f4efe6"
        orb='<circle cx="930" cy="92" r="30" fill="#f6f1e2"/><circle cx="930" cy="92" r="70" fill="url(#glow)"/>'
        glowc="#c9d4ff"
        nstars=90
    else:
        sky=[("0","#b9d6f2"),("0.6","#dbe9f7"),("0.88","#f6e3d0"),("1","#f2b58f")]
        ridges=[(1,238,14,"#b9a6c4",.9),(2,262,16,"#8d7fa8",1),(3,286,14,"#5a5482",1)]
        title="#1a2350"; sub="#3d4775"; chip="#1a2350"
        orb='<circle cx="930" cy="110" r="34" fill="#fff4dc"/><circle cx="930" cy="110" r="90" fill="url(#glow)"/>'
        glowc="#ffd9a0"
        nstars=0
    stars=""
    for i in range(nstars):
        x=random.uniform(0,W); y=random.uniform(0,190); r=random.choice([.7,.9,1.2,1.6])
        d=random.uniform(2.5,6); b=random.uniform(0,5)
        stars+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#fff" class="s" style="animation-duration:{d:.1f}s;animation-delay:-{b:.1f}s"/>'
    stops="".join(f'<stop offset="{o}" stop-color="{c}"/>' for o,c in sky)
    rd="".join(ridge(*r) for r in ridges)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Gideon Sanni, Software Engineer">
<style>
.s{{animation:tw 4s ease-in-out infinite}}@keyframes tw{{0%,100%{{opacity:.25}}50%{{opacity:1}}}}
.orb{{animation:fl 9s ease-in-out infinite}}@keyframes fl{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-6px)}}}}
.in{{animation:up 1.2s cubic-bezier(.2,.7,.2,1) both}}@keyframes up{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}
.d2{{animation-delay:.25s}}.d3{{animation-delay:.5s}}
</style>
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">{stops}</linearGradient>
<radialGradient id="glow"><stop offset="0" stop-color="{glowc}" stop-opacity=".45"/><stop offset="1" stop-color="{glowc}" stop-opacity="0"/></radialGradient>
<clipPath id="r"><rect width="{W}" height="{H}" rx="18"/></clipPath></defs>
<g clip-path="url(#r)"><rect width="{W}" height="{H}" fill="url(#sky)"/>{stars}
<g class="orb">{orb}</g>{rd}
<g font-family="Georgia,'Times New Roman',serif">
<text x="70" y="128" font-size="66" fill="{title}" letter-spacing="-1">Gideon Sanni</text>
<text x="72" y="170" font-size="21" fill="{sub}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" letter-spacing="1">Software Engineer · Distributed systems · Kubernetes · AI pipelines</text>
<text x="72" y="206" font-size="16" fill="{sub}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" opacity=".85">Grambling State University · Grambling, LA</text></g></g></svg>'''
for d in (True,False):
    open(f"assets/banner-{'dark' if d else 'light'}.svg","w").write(banner(d))

# stack panel
groups=[("Languages",["Go","Python","TypeScript","Rust","Solidity","SQL"]),
("Backend &amp; data",["Kafka","Cassandra","PostgreSQL","FastAPI","Node.js"]),
("Infrastructure",["Kubernetes","Istio","Linkerd","Docker","Prometheus"]),
("AI &amp; verification",["LLM pipelines","xUnit / Jest","Property testing","Foundry"])]
def stack(dark):
    bg,line,lab,txt,chipbg=("#12122c","#2f2b57","#a9a3d6","#f4efe6","#1e1b40") if dark else ("#f4f8fd","#cbd8ea","#4c5a8a","#1a2350","#e4edf9")
    y=44; out=""; 
    for g,items in groups:
        out+=f'<text x="28" y="{y}" font-size="12" fill="{lab}" letter-spacing="2" font-family="ui-monospace,Menlo,monospace">{g.upper().replace("&AMP;","&amp;")}</text>'
        x=28; yy=y+14
        for it in items:
            w=len(it)*8.2+24
            out+=f'<rect x="{x:.0f}" y="{yy}" width="{w:.0f}" height="28" rx="14" fill="{chipbg}" stroke="{line}"/><text x="{x+w/2:.0f}" y="{yy+19}" font-size="13" text-anchor="middle" fill="{txt}" font-family="-apple-system,Segoe UI,Helvetica,sans-serif">{it}</text>'
            x+=w+10
        y+=74
    h=y-8
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {h}" width="760" height="{h}" role="img" aria-label="Tech stack"><rect width="760" height="{h}" rx="16" fill="{bg}" stroke="{line}"/>{out}</svg>'
for d in (True,False):
    open(f"assets/stack-{'dark' if d else 'light'}.svg","w").write(stack(d))
