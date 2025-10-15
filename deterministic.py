import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def median_of_medians(arr):
    if len(arr) <= 5:
        return insertion_sort(arr)[len(arr) // 2]

    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [insertion_sort(group)[len(group) // 2] for group in groups]

    return median_of_medians(medians)

def partition(arr, pivot):
    low, high, equal = [], [], []
    for x in arr:
        if x < pivot:
            low.append(x)
        elif x > pivot:
            high.append(x)
        else:
            equal.append(x)
    return low, equal, high

def deterministic_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = median_of_medians(arr)
    low, equal, high = partition(arr, pivot)

    if k <= len(low):
        return deterministic_quickselect(low, k)
    elif k <= len(low) + len(equal):
        return pivot
    else:
        return deterministic_quickselect(high, k - len(low) - len(equal))

sizes = [100, 500, 1000, 5000, 10000, 20000, 50000]
times = []
print(f"{'Input Size':>12} | {'Time (seconds)':>15}")
print("-" * 32)

for n in sizes:
    arr = [random.randint(0, 100000) for i in range(n)]
    k = n // 2  # median position
    start = time.time()
    median = deterministic_quickselect(arr, k)
    end = time.time()
    elapsed = end - start
    times.append(elapsed)
    print(f"{n:>12} | {elapsed:>15.6f}") 
times_normalized = [t / max(times) for t in times]
theoretical = [n / max(sizes) for n in sizes]
    
plt.figure(figsize=(8,5))
plt.plot(sizes, times_normalized, marker='o', linestyle='-', color='b', label='Experimental (normalized)')
plt.plot(sizes, theoretical, marker='x', linestyle='--', color='r', label='Theoretical O(n)')
plt.title("Deterministic Quickselect: Experimental vs Theoretical")
plt.xlabel("Input Size")
plt.ylabel("Normalized Time")
plt.legend()
plt.grid(True)
plt.show()

