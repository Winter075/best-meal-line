"""The Best Meal You Ever Had — one sentence, written to /output/entry.txt."""

import os
from pathlib import Path

LINE = (
    "The best meal I ever had was day-old bread and salted butter in my "
    "grandfather's kitchen; his hands shook as he tore it, and he still "
    "passed me the bigger half."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
