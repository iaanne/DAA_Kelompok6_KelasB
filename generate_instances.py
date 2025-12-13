# generate_instances.py
import json, random
from pathlib import Path

BASE = Path(__file__).resolve().parent / 'data'
BASE.mkdir(exist_ok=True)

def save(name, obj):
    p = BASE / name
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    return p

def make_knapsack_lab_inventory(n_items=15, capacity=50, seed=3640):
    """
    Generate knapsack instance bertema inventaris laboratorium.
    Setiap item memiliki ID unik, value, dan weight dengan rasio bervariasi.
    
    Args:
        n_items: jumlah item (default 15)
        capacity: kapasitas knapsack (default 50)
        seed: random seed untuk reproducibility
    """
    rnd = random.Random(seed)
    
    items = []
    for i in range(1, n_items + 1):
        item = {
            "id": f"LAB-A-{i:03d}",
            "value": rnd.randint(10, 50),  # nilai item 10-50
            "weight": rnd.randint(2, 20)    # bobot item 2-20
        }
        items.append(item)
    
    instance = {
        "project": "knapsack_01_labA",
        "capacity": capacity,
        "description": f"Lab Inventory A - {n_items} items with varying value/weight ratios",
        "items": items
    }
    
    return instance

def main():
    print("Generating knapsack instance for Kelompok 6...")
    
    # Generate instance dengan 15 items (bisa diubah sesuai kebutuhan)
    instance = make_knapsack_lab_inventory(n_items=15, capacity=50, seed=3642)
    
    filename = 'knapsack_labA_inv.json'
    saved_path = save(filename, instance)
    
    print(f"✓ {filename} created successfully!")
    print(f"  Location: {saved_path}")
    print(f"  Items: {len(instance['items'])}")
    print(f"  Capacity: {instance['capacity']}")
    print(f"  Project: {instance['project']}")
    print("\nInstance siap digunakan untuk eksperimen knapsack 0/1!")

if __name__ == '__main__':
    main()