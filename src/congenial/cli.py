from __future__ import annotations

import argparse

from .messages import build_greeting


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a tiny greeting")
    parser.add_argument("name", nargs="?", default="friend", help="Who to greet")
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    parser.add_argument("--color", action="store_true", help="Use colored output")
    args = parser.parse_args()
    print(build_greeting(args.name, use_color=args.color))


if __name__ == "__main__":
    main()
