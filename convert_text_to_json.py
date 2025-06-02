import json
from pathlib import Path
from datetime import datetime

input_path = Path("input/input.txt")
output_path = Path("data/aliance_data.json")

if not input_path.exists():
    print("input/input.txt nenalezen")
    exit(1)

data = {
    "meta": {
        "vytvoreno": datetime.now().strftime("%d. %m. %Y, %H:%M:%S")
    },
    "aliance": {
        "hodnost": 7,
        "zisk_expy": 3274432,
        "do_pristi": {
            "expy": 725568,
            "procento": 48.4
        },
        "procento_aktualni": 51.6
    },
    "valky": [
        {
            "nepritel": "NGTY",
            "skore": "20:170",
            "uzemi_nase": 12087,
            "uzemi_jejich": 413861,
            "ziskane_expy": 695534
        }
    ],
    "hraci": [],
    "pokroky": [],
    "aliancni_pokroky": [
        "Guerillové války (10)",
        "Offshore banka (10)",
        "Dynamické pancéřování tanku (8)"
    ]
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("aliance_data.json vytvořen.")
