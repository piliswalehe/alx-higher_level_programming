#!/usr/bin/python3
for num in range(10, 100):
    if num // 10 != num % 10:
        print(f"{min(num // 10, num % 10)}{max(num // 10, num % 10)}",
                end=", " if num != 98 else "\n")
