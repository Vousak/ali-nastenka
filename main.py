import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

# Cesty
base_dir = Path(__file__).parent
data_path = base_dir / 'data' / 'aliance_data.json'
template_path = base_dir / 'templates'
output_path = base_dir / 'output' / 'nastenka.html'

# Načtení dat
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Načtení šablony
env = Environment(loader=FileSystemLoader(str(template_path)))
template = env.get_template('nastenka_template.html')

# Vygenerování HTML
output = template.render(data=data)

# Uložení výstupu
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(output)

print("Nástěnka byla úspěšně vygenerována.")
