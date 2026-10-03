"""Markdown to HTML — Render a Markdown file to a single HTML page with a small default stylesheet."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='markdown_to_html',
        description='Render a Markdown file to a single HTML page with a small default stylesheet.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Markdown to HTML')
    print('Notes to a page you can open locally.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
