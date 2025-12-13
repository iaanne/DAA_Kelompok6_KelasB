import json, argparse, time
from pathlib import Path
from typing import Any

# -------------------- ALGORITMA KNAPSACK --------------------

def greedy_knapsack(instance: Any, project: str) -> Any:
    """Algoritma Greedy (Density-based) untuk Knapsack 0/1"""
    if "knapsack" in project.lower():
        capacity = instance['capacity']
        items = instance['items'].copy()
        
        # Hitung density (nilai/bobot) untuk setiap item
        for item in items:
            item['density'] = item['value'] / item['weight']
        
        # Urutkan item berdasarkan density descending
        items.sort(key=lambda x: x['density'], reverse=True)
        
        selected_items = []
        total_value = 0
        total_weight = 0
        
        # Pilih item dengan density tertinggi selama kapasitas memungkinkan
        for item in items:
            if total_weight + item['weight'] <= capacity:
                selected_items.append(item)
                total_value += item['value']
                total_weight += item['weight']
        
        return {
            'items': selected_items,
            'total_value': total_value,
            'total_weight': total_weight,
            'algorithm': 'greedy'
        }
    
    raise NotImplementedError(f"greedy_knapsack not implemented for project={project}")


def dp_knapsack(instance: Any, project: str) -> Any:
    """Algoritma Dynamic Programming untuk Knapsack 0/1"""
    if "knapsack" in project.lower():
        capacity = instance['capacity']
        items = instance['items']
        n = len(items)
        
        # Inisialisasi tabel DP
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
        
        # Isi tabel DP
        for i in range(1, n + 1):
            item_weight = items[i-1]['weight']
            item_value = items[i-1]['value']
            for w in range(capacity + 1):
                # Jika item i tidak dipilih
                dp[i][w] = dp[i-1][w]
                # Jika item i dipilih (jika muat)
                if item_weight <= w:
                    dp[i][w] = max(dp[i][w], dp[i-1][w-item_weight] + item_value)
        
        # Rekonstruksi solusi
        selected_items = []
        w = capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]:
                # Item i-1 dipilih
                selected_items.append(items[i-1])
                w -= items[i-1]['weight']
        
        selected_items.reverse()
        
        return {
            'items': selected_items,
            'total_value': dp[n][capacity],
            'total_weight': sum(item['weight'] for item in selected_items),
            'algorithm': 'dp'
        }
    
    raise NotImplementedError(f"dp_knapsack not implemented for project={project}")


def branch_and_bound_knapsack(instance: Any, project: str) -> Any:
    """Algoritma Branch and Bound untuk Knapsack 0/1"""
    if "knapsack" in project.lower():
        capacity = instance['capacity']
        items = instance['items'].copy()
        
        # Urutkan item berdasarkan density (nilai/bobot) descending
        for item in items:
            item['density'] = item['value'] / item['weight']
        items.sort(key=lambda x: x['density'], reverse=True)
        
        # Fungsi untuk menghitung batas atas (upper bound)
        def calculate_bound(level, current_value, current_weight):
            bound = current_value
            total_weight = current_weight
            
            for i in range(level, len(items)):
                if total_weight + items[i]['weight'] <= capacity:
                    total_weight += items[i]['weight']
                    bound += items[i]['value']
                else:
                    # Tambahkan pecahan dari item (relaxed knapsack)
                    if capacity - total_weight > 0:
                        remaining_capacity = capacity - total_weight
                        bound += items[i]['value'] * (remaining_capacity / items[i]['weight'])
                    break
            return bound
        
        max_value = 0
        best_items = []
        
        # Stack untuk DFS
        stack = [(-1, 0, 0, [])]  # (level, current_value, current_weight, current_items)
        
        while stack:
            level, current_value, current_weight, current_items = stack.pop()
            
            if current_value > max_value:
                max_value = current_value
                best_items = current_items
            
            if level == len(items) - 1:
                continue
            
            next_level = level + 1
            next_item = items[next_level]
            
            # Branch 2: Mengambil item (jika muat)
            if current_weight + next_item['weight'] <= capacity:
                new_value = current_value + next_item['value']
                new_weight = current_weight + next_item['weight']
                new_items = current_items + [next_item]
                bound = calculate_bound(next_level + 1, new_value, new_weight)
                if bound > max_value:
                    stack.append((next_level, new_value, new_weight, new_items))
            
            # Branch 1: Tidak mengambil item
            bound = calculate_bound(next_level + 1, current_value, current_weight)
            if bound > max_value:
                stack.append((next_level, current_value, current_weight, current_items))
        
        return {
            'items': best_items,
            'total_value': max_value,
            'total_weight': sum(item['weight'] for item in best_items),
            'algorithm': 'branch_and_bound'
        }
    
    raise NotImplementedError(f"branch_and_bound_knapsack not implemented for project={project}")


# -------------------- EVALUATOR --------------------

def evaluate(instance: Any, output: Any, project: str) -> float:
    """Kembalikan metrik kualitas (gap terhadap optimal).
    Untuk knapsack: gap = 0 jika optimal, > 0 jika suboptimal."""
    
    if "knapsack" in project.lower():
        # Hitung solusi optimal dengan DP untuk pembanding
        optimal_solution = dp_knapsack(instance, project)
        optimal_value = optimal_solution['total_value']
        solution_value = output['total_value']
        
        # Hitung gap: (optimal - solution) / optimal
        if optimal_value > 0:
            gap = (optimal_value - solution_value) / optimal_value
        else:
            gap = 0.0
        
        return gap
    
    return 0.0


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--instance', required=True, help='Path ke berkas JSON di folder data/')
    p.add_argument('--algo', choices=['greedy','dp','bnb'], default='dp', 
                   help='greedy=Greedy, dp=Dynamic Programming, bnb=Branch&Bound')
    args = p.parse_args()
    
    inst = json.load(open(args.instance, 'r', encoding='utf-8'))
    project = inst.get("project", "unknown")
    
    t0 = time.perf_counter()
    if args.algo == 'greedy':
        out = greedy_knapsack(inst, project)
    elif args.algo == 'dp':
        out = dp_knapsack(inst, project)
    else:  # args.algo == 'bnb'
        out = branch_and_bound_knapsack(inst, project)
    dt = (time.perf_counter() - t0) * 1000.0
    
    gap = evaluate(inst, out, project)
    
    print(f"Project={project} Algo={args.algo} Time_ms={dt:.2f} Gap={gap:.4f}")
    print(f"Total_Value={out['total_value']} Total_Weight={out['total_weight']}")
    print(f"Selected_Items={len(out['items'])} items")
    print(f"Algorithm={out['algorithm']}")


if __name__ == '__main__':
    main()