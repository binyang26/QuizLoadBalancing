import random
import time

# jumlah server
N = 5

# generate distribusi tidak merata (uneven)
loads = [random.randint(10, 100) for _ in range(N)]

# hitung total dan ideal load
total_load = sum(loads)
ideal_load = total_load / N

print("Initial Load Distribution :", loads)
print("Total Load                :", total_load)
print("Ideal Load     :", round(ideal_load, 2))
print("=" * 60)

# inisialisasi step dan waktu
step = 0
start_time = time.time()

# proses redistribusi
while True:
    step += 1
    step_start = time.time()

    # cari server max & min
    max_index = loads.index(max(loads))
    min_index = loads.index(min(loads))

    max_load = loads[max_index]
    min_load = loads[min_index]
    gap = max_load - min_load

    print(f"\n[STEP {step}]")
    print(f"Max Server (index {max_index}) : {max_load}")
    print(f"Min Server (index {min_index}) : {min_load}")
    print(f"Load Gap                      : {gap}")

    # cek kondisi ideal
    if gap <= 1:
        print("✔ Ideal distribution reached!")
        break

    # hitung jumlah transfer
    transfer = gap // 2

    if transfer == 0:
        print("⚠ No more transfer possible")
        break

    print(f"Transfer Load                : {transfer}")

    # redistribusi beban
    loads[max_index] -= transfer
    loads[min_index] += transfer

    # waktu per step
    step_time = time.time() - step_start

    print(f"Updated Distribution         : {loads}")
    print(f"Step Execution Time          : {round(step_time, 6)} seconds")

# total waktu eksekusi
total_time = time.time() - start_time

print("\n" + "=" * 60)
print("Final Distribution :", loads)
print("Total Steps        :", step)
print("Total Execution Time:", round(total_time, 6), "seconds")