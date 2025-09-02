# ~/Hub/SeesTrees/sees_trees.py

from pathlib import Path
from src.engine.node import TreeNode, GitStatus
from src.engine.renderer import render_tree
from src.engine.glyphs_map import Colors, GLYPH_FILES, GLYPH_MARKERS
from src.engine.tree_parser import build_tree


def generate_power_grid_effect(power_level, text):
    if power_level <= 0:
        return text
    
    effects = {
        1: f"{Colors.GLOW_START}{text}{Colors.GLOW_END}",
        2: f"{Colors.BOLD}{text}{Colors.RESET}",
        3: f"{Colors.BOLD}{Colors.GLOW_START}{text}{Colors.GLOW_END}{Colors.RESET}",
        4: f"{Colors.BOLD}{Colors.GLOW_START} {text} {Colors.GLOW_END}{Colors.RESET}",
        5: f"{Colors.BLINK}{Colors.BOLD}{Colors.GLOW_START} {text} {Colors.GLOW_END}{Colors.RESET}"
    }
    
    return effects.get(min(power_level, 5), text)

def get_file_icon(file_path):
    ext = file_path.suffix.lower()
    name = file_path.name.lower()
    
    if name.startswith('.') or name in ['dockerfile', 'makefile']:
        return "⚙️", Colors.CONFIG
    
    if name in ['package.json', 'package-lock.json']:
        return "📦", Colors.NPM
    
    if name in ['readme.md', 'changelog.md', 'license']:
        return "📚", Colors.DOCS

    return GLYPH_FILES.get(ext, ("📄", Colors.RESET))

def get_status_marker(status, power_level):
    markers = {
        'A': f"{Colors.GIT_ADD}{GLYPH_MARKERS.GIT_ADD * power_level}{Colors.RESET}",
        'M': f"{Colors.GIT_MOD}{GLYPH_MARKERS.GIT_MOD * power_level}{Colors.RESET}",
        'D': f"{Colors.GIT_DEL}{GLYPH_MARKERS.GIT_DEL * power_level}{Colors.RESET}",
        'R': f"{Colors.GIT_REN}{GLYPH_MARKERS.GIT_REN * power_level}{Colors.RESET}",
        '??': f"{Colors.GIT_UNT}{GLYPH_MARKERS.GIT_UNT * power_level}{Colors.RESET}"
    }
    return markers.get(status, '')


def main():
    repo_path = Path.cwd()
    git_status = GitStatus(repo_path)
    ignore_patterns = git_status.parse_gitignore(repo_path)
    
    print(f"\nRepository: {repo_path}")
    print(f"Branch: {git_status.branch}")
    print(f"Last Commit: {git_status.last_commit}")
    print("\n" + "=" * 50 + "\n")
    
    tree = build_tree(repo_path, ignore_patterns)
    render_tree(tree)

if __name__ == "__main__":
    main()
