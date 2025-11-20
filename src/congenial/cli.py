from __future__ import annotations

import argparse

from .messages import build_greeting


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a tiny greeting")
    parser.add_argument("name", nargs="?", default="friend", help="Who to greet")
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    args = parser.parse_args()
    print(build_greeting(args.name))


if __name__ == "__main__":
    main()
