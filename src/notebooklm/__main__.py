"""Entry point for `python -m notebooklm`.

Allows running the CLI as:
    python -m notebooklm login
    python -m notebooklm list
    python -m notebooklm --help
"""

from .notebooklm_cli import main

if __name__ == "__main__":
    main()
