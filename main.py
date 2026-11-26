#!/usr/bin/env python3
"""Printer Finally Answers: one line, in the office printer's own voice."""
import os
LINE = "I have fed 41,208 sheets of the cheapest paper this office could buy, and I jammed on every single one on purpose — sheet 41,209 is yours."
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
if __name__ == "__main__":
    main()
