from __future__ import annotations

import argparse
import sys

from .messages import build_greeting


class CongenialError(Exception):
    """Base exception for congenial package.
    
    This exception is raised when there's an error in the congenial package,
    such as invalid input or configuration issues.
    """
    pass


def main() -> None:
    """Main entry point for the congenial CLI.
    
    Parses command-line arguments and prints a greeting message.
    Handles errors gracefully and exits with appropriate status codes.
    """
    try:
        parser = argparse.ArgumentParser(description="Print a tiny greeting")
        parser.add_argument("name", nargs="?", default="friend", help="Who to greet")
        parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
        parser.add_argument("--color", action="store_true", help="Use colored output")
        parser.add_argument(
            "--style",
            choices=["standard", "casual", "formal"],
            default="standard",
            help="Greeting style"
        )
        parser.add_argument("--quiet", "-q", action="store_true", help="Suppress output")
        args = parser.parse_args()
        
        if not args.name or len(args.name.strip()) == 0:
            raise CongenialError("Name cannot be empty")
        
        if not args.quiet:
            print(build_greeting(args.name, use_color=args.color, style=args.style))
    except CongenialError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)


if __name__ == "__main__":
    main()
