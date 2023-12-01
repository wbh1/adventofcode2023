#!/usr/bin/env python3
from argparse import ArgumentParser
from importlib import import_module

parser = ArgumentParser(prog="aoc.py", description="2023 AoC Solution Runner")
parser.add_argument("day", help="which day to run")
args = parser.parse_args()

day = getattr(import_module(f"solutions.day{args.day}"), f"Day{args.day}")()

day.solve()
