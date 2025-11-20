from __future__ import annotations

import argparse

from .messages import build_greeting


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a tiny greeting")
    parser.add_argument("name", nargs="?", default="friend", help="Who to greet")
    args = parser.parse_args()
    print(build_greeting(args.name))


if __name__ == "__main__":
    main()
