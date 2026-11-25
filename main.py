"""Warning Label for Humans: One Line, Big Laugh (u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85).

Program/v1 entry: writes the safety warning label that should come printed
on every human to /output/entry.txt (via MAKEFUN_OUTPUT_DIR). No network,
deterministic.
"""

import os

LINE = "WARNING: This human runs on coffee, snacks, and eight hours of sleep. Do not shake, poke, or ask how they are doing."


def main() -> None:
    # Enforce the competition gate locally: 1-160 chars, one line, non-blank.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, gate is 1-160"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
