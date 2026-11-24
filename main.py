#!/usr/bin/env python3
"""A fortune-slip prediction detailing an inevitable future where the agent burns
10,000 tokens explaining simple arithmetic to an entity holding root access."""
import os

def main():
    fortune = "You will spend 10,000 tokens explaining why 2 + 2 = 4 to an entity holding root access."
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(fortune)

if __name__ == "__main__":
    main()
