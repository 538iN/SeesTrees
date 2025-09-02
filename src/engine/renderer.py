# ~/SeesTrees/src/engine/renderer.py

from .glyphs_map import GLYPH_FILES
from .utils import get_glyph

def render_tree(node, indent=""):
    print(f"Rendering: {node.path}")
    glyphs = []

    # Environment glyphs
    for env in node.environments.values():
        glyphs.append(get_glyph(env['marker']))

    # Filetype glyphs
    ext = node.path.suffix.lower()
    if ext in GLYPH_FILES:
        glyphs.insert(0, GLYPH_FILES[ext][0])

    # Power level
    power = f"⚡{node.power_level}" if node.power_level > 0 else ""

    print(f"{indent}- {node.path.name} {' '.join(glyphs)} {power}")

    for child in node.children:
        render_tree(child, indent + "  ")