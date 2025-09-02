# ~/SeesTrees/src/engine/glyphs_map.py

class Colors:
    FOLDER = '\033[1;34m'
    CONFIG = '\033[1;33m'
    PYTHON = '\033[1;32m'
    DOCS = '\033[1;36m'
    JSON = '\033[1;35m'
    LOCK = '\033[1;31m'
    IMAGE = '\033[38;5;213m'
    NPM = '\033[38;5;208m'
    HTML = '\033[38;5;202m'
    CSS = '\033[38;5;39m'
    JS = '\033[38;5;220m'
    TS = '\033[38;5;45m'
    YAML = '\033[38;5;177m'
    SQL = '\033[38;5;147m'
    CSV = '\033[38;5;107m'
    PYTHON_ENV = '\033[38;5;46m'
    NODE_ENV = '\033[38;5;214m'
    DOCKER_ENV = '\033[38;5;33m'
    RUBY_ENV = '\033[38;5;196m'
    GO_ENV = '\033[38;5;75m'
    JAVA_ENV = '\033[38;5;166m'
    PHP_ENV = '\033[38;5;105m'
    GIT_ADD = '\033[38;5;40m'
    GIT_MOD = '\033[38;5;214m'
    GIT_DEL = '\033[38;5;196m'
    GIT_REN = '\033[38;5;105m'
    GIT_UNT = '\033[38;5;245m'
    GLOW_START = '\033[7m'
    GLOW_END = '\033[27m'
    BLINK = '\033[5m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

GLYPH_MARKERS = {
    "TEXT_ENV": "📄",
    "PYTHON_VENV": "🟢",
    "PYTHON_POETRY": "🔵",
    "NODE_ENV": "🟠",
    "DOCKER_ENV": "🐳",
    "RUBY_ENV": "💎",
    "GO_ENV": "🔹",
    "JAVA_ENV": "☕",
    "PHP_ENV": "🐘",
    "POWER_SOURCE": "⚡",
    "POWER_FLOW": "✨",
    "GIT_ADD": "⚡",
    "GIT_MOD": "🔌",
    "GIT_DEL": "💥",
    "GIT_REN": "➡️",
    "GIT_UNT": "⭕"
}

GLYPH_FILES = {
    '.py': ('🐍', GLYPH_MARKERS['PYTHON_VENV']),
    '.toml': ('⚙️', GLYPH_MARKERS['PYTHON_POETRY']),
    '.ts': ('📘📜', GLYPH_MARKERS['NODE_ENV']),
    '.js': ('🟠📜', GLYPH_MARKERS['NODE_ENV']),
    '.jsx': ('🟠📜⚛️', GLYPH_MARKERS['NODE_ENV']),
    '.tsx': ('📘📜⚛️', GLYPH_MARKERS['NODE_ENV']),
    '.rb': ('💎', GLYPH_MARKERS['RUBY_ENV']),
    '.go': ('🔹', GLYPH_MARKERS['GO_ENV']),
    '.java': ('☕', GLYPH_MARKERS['JAVA_ENV']),
    '.php': ('🐘', GLYPH_MARKERS['PHP_ENV']),
    '.dockerfile': ('🐳', GLYPH_MARKERS['DOCKER_ENV']),
    '.txt': ('📄', GLYPH_MARKERS['TEXT_ENV'])
}
