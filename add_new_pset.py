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

# support various prog lang naming
ALIASES = {
    "py": "python",
    "c++": "cpp",
    "cc": "cpp",
    "jv": "java",
    "ts": "typescript",
}

# -------------------------------------------------------------------

STOPWORDS = {
    "of", "the", "a", "an", "in", "on", "at", "with", "to", "and", "or", "by",
    "for", "from", "is", "are", "be", "that", "this"
}

SUBS = {
    # data-structure & algo nouns
    "array": "arr",
    "arrays": "arrs",
    "subarray": "subarr",
    "subarrays": "subarrs",
    "number": "num",
    "numbers": "nums",
    "integer": "int",
    "integers": "ints",
    "string": "str",
    "strings": "strs",
    "substring": "substr",
    "substrings": "substrs",
    "character": "char",
    "characters": "chars",
    "list": "lst",
    "lists": "lsts",
    "tree": "tree",
    "trees": "trees",
    "without": "wo",
    "minimum": "min",
    "maximum": "max",
}


def slugify(title: str) -> str:
    words = re.findall(r"[A-Za-z0-9']+", title.lower())

    out = []
    for w in words:
        if w in STOPWORDS:
            continue
        w = SUBS.get(w, w)
        out.append(w)

    return "_".join(out)


def build_paths(title: str, lang_key: str):
    if lang_key not in LANG_INFO:
        sys.exit(f"❌ Unknown language '{lang_key}'. Known: {list(LANG_INFO)}")
    folder, ext, *_ = LANG_INFO[lang_key]
    slug = slugify(title)
    file_path = pathlib.Path(folder) / f"{slug}{ext}"
    return file_path


def ensure_file(path: pathlib.Path):
    if path.exists():
        abs_path = path.resolve()
        print(f"⚠️File already exists:")
        print(abs_path.as_uri())
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    header = textwrap.dedent("")
    path.write_text(header)

    abs_path = path.resolve()
    print(f"📝Created file:")
    print(abs_path.as_uri())
    return True


def make_link(path: pathlib.Path, lang_key: str) -> str:
    """Return the <a href=…><img …></a> snippet for one language/file."""
    _, _, icon_folder, icon_name = LANG_INFO[lang_key]
    return (
        f'<a href="{path.as_posix()}">'
        f'<img src="https://raw.githubusercontent.com/devicons/devicon/'
        f'master/icons/{icon_folder}/{icon_name}.svg" width="40px"></a>'
    )


def make_row(num: int, title: str, links: list[str]) -> str:
    """Compose a full Markdown table row from number, title, and link list."""
    return f"| {num} | {title} | {' '.join(links)} |"


def update_readme(new_link: str, num: int, title: str):
    start, end = "<!-- LEETCODE TABLE START -->", "<!-- LEETCODE TABLE END -->"
    lines = README.read_text().splitlines()
    i_start, i_end = lines.index(start), lines.index(end)

    head = lines[: i_start + 1]  # up to and incl. START marker
    tail = lines[i_end:]  # from END marker to EOF

    is_entry = re.compile(r'^\|\s*\d+')
    table = [l for l in lines[i_start + 1: i_end] if is_entry.match(l)]

    found = False
    for i, row in enumerate(table):
        if row.lstrip("| ").startswith(str(num)):
            found = True
            cells = [c.strip() for c in row.strip("|").split("|", 2)]
            links = cells[2].split() if cells[2] else []
            if new_link not in links:
                links.append(new_link)
                table[i] = make_row(num, title, links)
            break

    if not found:
        table.append(make_row(num, title, [new_link]))

    table.sort(key=lambda r: int(r.split("|")[1].strip()))

    header = "| # | Title | Lang |"
    separator = "|---|-------|------|"
    README.write_text(
        "\n".join(head + [header, separator] + table + tail) + "\n"
    )
    print("✅ README updated")


def check_done_before(num, lang_key):
    start, end = "<!-- LEETCODE TABLE START -->", "<!-- LEETCODE TABLE END -->"
    lines = README.read_text().splitlines()
    i_start, i_end = lines.index(start), lines.index(end)
    folder, ext, *_ = LANG_INFO[lang_key]

    is_entry = re.compile(r'^\|\s*\d+')
    table = [l for l in lines[i_start + 1: i_end] if is_entry.match(l)]

    for i, row in enumerate(table):
        cells = [c.strip() for c in row.strip("|").split("|", 2)]
        if cells[0] == str(num):
            print(f"Found duplicated row: {cells}")
            cells = [c.strip() for c in row.strip("|").split("|", 2)]
            links = cells[2]
            for path in re.findall(r'href="([^"]+)"', links):  # grab each <a href="…">
                if pathlib.Path(path).suffix == ext:
                    print(f"⚠️  Already solved in {lang_key} → {path}")
                    print(pathlib.Path(path).resolve().as_uri())  # or return it
                    return True

    print(f"✅ First time solving this problem in {lang_key}")
    return False


def main():
    lang_key = sys.argv[-1].lower()
    lang_key = ALIASES.get(lang_key, lang_key)
    if lang_key not in LANG_INFO:
        sys.exit("Usage: add_new_pset.py <number>. <Title> <language>")
    num = int(sys.argv[1][:-1])
    title = " ".join(sys.argv[2:-1])
    if check_done_before(num, lang_key):
        return
    file_path = build_paths(title, lang_key)
    file_created = ensure_file(file_path)
    if not file_created:
        return
    link = make_link(file_path, lang_key)
    update_readme(link, num, title)


if __name__ == "__main__":
    main()
