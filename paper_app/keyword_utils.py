from __future__ import annotations

import re
from typing import Protocol


class KeywordGroupLike(Protocol):
    label: str
    aliases: list[str]


def normalize_keyword(text: str) -> str:
    """Normalize keyword text for case and separator-insensitive matching."""
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def keyword_matches(text: str, keyword: str) -> bool:
    if not keyword:
        return False

    parts = [part for part in re.split(r"[^a-zA-Z0-9]+", keyword) if part]
    if not parts:
        return False

    if len(parts) == 1:
        pattern = rf"\b{re.escape(parts[0])}\b"
    else:
        separator = r"[^a-zA-Z0-9]*"
        pattern = r"\b" + separator.join(re.escape(part) for part in parts) + r"\b"

    return bool(re.search(pattern, text, flags=re.IGNORECASE))


def keyword_group_matches(text: str, keyword_group: KeywordGroupLike) -> bool:
    return any(keyword_matches(text, alias) for alias in keyword_group.aliases)


def find_keyword_matches(text: str, keyword_groups: list[KeywordGroupLike]) -> list[str]:
    return [keyword_group.label for keyword_group in keyword_groups if keyword_group_matches(text, keyword_group)]
