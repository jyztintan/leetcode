#!/usr/bin/env python3

"""
Usage
-----
$ python new_problem.py 1438 "Longest Continuous Subarray" python

• Creates  Python/1438_longest_continuous_subarray.py   (if absent)
"""

import pathlib, sys, re, textwrap

# ---------- CONFIG -------------------------------------------------
README = pathlib.Path("README.md")

LANG_INFO = {  # canonical lang → (folder, extension, devicon_folder, icon_name)
    "python": ("Python", ".py", "python", "python-original"),
    "cpp": ("C++", ".cpp", "cplusplus", "cplusplus-original"),
    "go": ("Go", ".go", "go", "go-original"),
    "java": ("Java", ".java", "java", "java-original"),
    "typescript": ("TypeScript", ".ts", "typescript", "typescript-original"),
    "sql": ("postgreSQL", ".sql", "postgresql", "postgresql-original"),
}


# -------------------------------------------------------------------

def slugify(title: str) -> str:
    return re.sub(r"\s+", "_", title.strip().lower())


def build_paths(num: int, title: str, lang_key: str):
    if lang_key not in LANG_INFO:
        sys.exit(f"❌  Unknown language '{lang_key}'. Known: {list(LANG_INFO)}")
    folder, ext, *_ = LANG_INFO[lang_key]
    slug = slugify(title)
    file_path = pathlib.Path(folder) / f"{slug}{ext}"
    return file_path


def ensure_file(path: pathlib.Path, num: int, title: str):
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    header = textwrap.dedent("")
    path.write_text(header)

    abs_path = path.resolve()  # now *absolute*
    print(f"📝 Created file:")
    print(abs_path.as_uri())


def make_row(num: int, title: str, path: pathlib.Path, lang_key: str) -> str:
    _, _, icon_folder, icon_name = LANG_INFO[lang_key]
    link = (
        f'<a href="{path.as_posix()}">'
        f'<img src="https://raw.githubusercontent.com/devicons/devicon/'
        f'master/icons/{icon_folder}/{icon_name}.svg" width="40px"></a>'
    )
    return f"| {num} | {title} | {link} |"


def update_readme(row: str, num: int):
    start, end = "<!-- LEETCODE TABLE START -->", "<!-- LEETCODE TABLE END -->"
    lines = README.read_text().splitlines()
    i_start, i_end = lines.index(start), lines.index(end)

    head = lines[: i_start + 1]          # up to and incl. START marker
    tail = lines[i_end :]                # from END marker to EOF

    import re
    is_entry = re.compile(r'^\|\s*\d+')
    table = [l for l in lines[i_start + 1 : i_end] if is_entry.match(l)]

    # replace or append current row
    table = [r for r in table if not r.lstrip("| ").startswith(str(num))]
    table.append(row)
    table.sort(key=lambda r: int(r.split("|")[1].strip()))

    header    = "| # | Title | Lang |"
    separator = "|---|-------|------|"
    README.write_text(
        "\n".join(head + [header, separator] + table + tail) + "\n"
    )
    print("✅  README updated")


def main():
    if len(sys.argv) != 4:
        sys.exit("Usage: add_new_pset.py <number>. <Title> <language>")
    num = int(sys.argv[1][:-1])
    title = sys.argv[2]
    lang_key = sys.argv[3].lower()

    file_path = build_paths(num, title, lang_key)
    ensure_file(file_path, num, title)
    row = make_row(num, title, file_path, lang_key)
    update_readme(row, num)


if __name__ == "__main__":
    main()
