import os
import feedparser
from bs4 import BeautifulSoup
from html import escape
from datetime import datetime

# Créer le dossier 'flux' s'il n'existe pas
flux_dir = "./flux"
os.makedirs(flux_dir, exist_ok=True)

# URLs des flux RSS
rss_urls = {
    "cert": "https://www.cert.ssi.gouv.fr/feed/",
    "developpez": "https://www.developpez.com/index/rss",
    "devops": "https://devops.com/feed/",
    "aws_devops": "https://aws.amazon.com/fr/blogs/devops/feed/",
    "hashicorp_terraform": "https://www.hashicorp.com/blog/products/terraform/feed.xml",
    "hashicorp_consul": "https://www.hashicorp.com/blog/products/consul/feed.xml",
    "hashicorp_vault": "https://www.hashicorp.com/blog/products/vault/feed.xml",
    "docker": "https://www.docker.com/feed/",
    "kubernetes": "https://kubernetes.io/feed.xml",
    "RHEL": "https://www.redhat.com/en/rss/blog",
    "JDHacker": "https://www.journalduhacker.net/rss",
    "Almalinux": "https://almalinux.org/blog/index.xml",
    "Debian": "https://www.debian.org/News/news"
}

# Structure de base du fichier HTML pour chaque flux
html_template = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Flux RSS {title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }}
        .entry {{
            border-bottom: 1px solid #ccc;
            padding: 10px 0;
        }}
        .title {{
            font-size: 1.5em;
            color: #333;
        }}
        .published {{
            color: #666;
        }}
        .summary {{
            margin-top: 10px;
        }}
    </style>
</head>
<body>
    <h1>Flux RSS {title}</h1>
    {entries}
</body>
</html>
"""

# Fonction pour nettoyer les résumés HTML
def clean_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    for img in soup.find_all("img"):
        img.decompose()
    return soup.get_text()

# Fonction pour convertir les dates en objets datetime
def parse_date(entry):
    if 'published_parsed' in entry:
        return datetime(*entry.published_parsed[:6])
    elif 'updated_parsed' in entry:
        return datetime(*entry.updated_parsed[:6])
    return datetime.min

# Fonction pour générer le contenu HTML pour un flux donné
def generate_html(feed, title):
    entries_html = ""
    sorted_entries = sorted(feed.entries, key=parse_date, reverse=True)
    
    for entry in sorted_entries:
        entry_title = escape(entry.title)
        link = entry.link
        published = entry.published if 'published' in entry else 'N/A'
        summary = clean_html(entry.summary if 'summary' in entry else 'No summary available')
        
        entries_html += f"""
        <div class="entry">
            <div class="title"><a href="{link}">{entry_title}</a></div>
            <div class="published">{published}</div>
            <div class="summary">{escape(summary)}</div>
        </div>
        """
    return html_template.format(title=title, entries=entries_html)

# Générer les fichiers HTML pour chaque flux RSS ( Dictionnaire )
for key, url in rss_urls.items():
    feed = feedparser.parse(url)
    title = {
        "cert": "CERT-FR",
        "developpez": "Developpez.com",
        "devops": "DevOps.com",
        "aws_devops": "AWS DevOps",
        "hashicorp_terraform": "HashiCorp Terraform",
        "hashicorp_consul": "HashiCorp Consul",
        "hashicorp_vault": "HashiCorp Vault",
        "docker": "Docker",
        "kubernetes": "Kubernetes",
        "RHEL": "RHEL",
        "JDHacker": "JDHacker",
        "Almalinux": "Almalinux",
        "Debian": "Debian"
    }[key]
    html_content = generate_html(feed, title)
    
    # Écrire le contenu dans un fichier HTML dans le dossier 'flux'
    with open(os.path.join(flux_dir, f"{key}.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

# Créer le fichier index.html
index_html = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Index des Flux RSS</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            text-align: center;
        }}
        .link {{
            margin: 20px;
        }}
    </style>
</head>
<body>
    <h1>Index des Flux RSS</h1>
    <div class="link">
        <a href="flux/cert.html">Flux RSS CERT-FR</a>
    </div>
    <div class="link">
        <a href="flux/developpez.html">Flux RSS Developpez.com</a>
    </div>
    <div class="link">
        <a href="flux/devops.html">Flux RSS DevOps.com</a>
    </div>
    <div class="link">
        <a href="flux/aws_devops.html">Flux RSS AWS DevOps</a>
    </div>
    <div class="link">
        <a href="flux/hashicorp_terraform.html">Flux RSS HashiCorp Terraform</a>
    </div>
    <div class="link">
        <a href="flux/hashicorp_consul.html">Flux RSS HashiCorp Consul</a>
    </div>
    <div class="link">
        <a href="flux/hashicorp_vault.html">Flux RSS HashiCorp Vault</a>
    </div>
    <div class="link">
        <a href="flux/docker.html">Flux RSS Docker</a>
    </div>
    <div class="link">
        <a href="flux/kubernetes.html">Flux RSS Kubernetes</a>
    </div>
    <div class="link">
        <a href="flux/RHEL.html">Flux RSS RHEL</a>
    </div>
    <div class="link">
        <a href="flux/JDhacker.html">Flux RSS JDhacker</a>
    </div>
    <div class="link">
        <a href="flux/Almalinux.html">Flux RSS Almalinux</a>
    </div>
    <div class="link">
        <a href="flux/Debian.html">Flux RSS Debian</a>
    </div>
</body>
</html>
"""

# Écrire le contenu dans le fichier index.html à la racine
with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print("Les fichiers HTML ont été créés avec succès.")
