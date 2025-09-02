# Planned Changes Upcoming to SeesTrees

## Extract Tree Parsing Logic

Currently, tree parsing is embedded inside `sees_trees.py`, coupled with emoji rendering
& CLI output

### TODO

1. Create a new module: `tree_parser.py`
2. Move all logic related to walking the file system & buidling the tree structure into this file
3. Strip emoji, color, & CLI formatting
4. Build `renderer.py` to render the tree with symbolic overlays

```
# ~/Hub/SeesTrees/src/engine/tree_parser.py
#   - handles filesystem traversal and builds the semantic tree
#   - node.py – defines your TreeNode class or data structure
#   - __init__.py - initializes the package
```

#### Purpose

- This isolates the semantic structure from the presentation layer. Once the tree is cleaned,
  it can be rendered multiple ways (CLI, VSCode, SVG, etc) without rewriting logic