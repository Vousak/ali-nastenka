import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

base = Path(__file__).parent
data_path = base / "data/aliance_data.json"
template_path = base / "templates"
output_path = base / "docs/index.html"

env = Environment(loader=FileSystemLoader(str(template_path)))
template = env.get_template("nastenka_template.html")

with open(data_path, "r", encoding="utf-8") as f:
    data = json.load(f)

html = template.render(**data)
output_path.parent.mkdir(parents=True, exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Nástěnka vygenerována.")
