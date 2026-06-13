#!/usr/bin/env python3
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {'.git', '.pytest_cache', '__pycache__', '.venv', 'venv'}
EXCLUDE_FILES = {'SHA256SUMS.txt'}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def include(path: Path) -> bool:
    rel_parts = set(path.relative_to(ROOT).parts)
    if rel_parts & EXCLUDE_DIRS:
        return False
    if path.name in EXCLUDE_FILES:
        return False
    if path.suffix == '.pyc':
        return False
    return path.is_file()


def main() -> int:
    files = sorted(p for p in ROOT.rglob('*') if include(p))
    with (ROOT / 'SHA256SUMS.txt').open('w', encoding='utf-8') as out:
        for p in files:
            out.write(f'{sha256(p)}  {p.relative_to(ROOT).as_posix()}\n')
    print(f'SHA256SUMS_WRITTEN {len(files)} files')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
