# ~/SeesTrees/src/engine/utils.py

import fnmatch
from .glyphs_map import GLYPH_MARKERS

def get_default_ignore_patterns():
    return {
        '.git', '.svn', '.hg',
        '.vscode-test', '.vscode-linux-x64-*',
        'node_modules.asar', 'node_modules.asar.unpacked',
        'node_modules', '__pycache__', '.pytest_cache',
        'build', 'dist', '*.pyc', '*.pyo', '*.pyd',
        '.idea', '.vs', '*.swp', '*.swo',
        '.DS_Store', 'Thumbs.db',
        '*.log', '*.sqlite',
        '.env', '.venv', 'env/', 'venv/', 'ENV/',
        'out', '.history', '*.vsix', '.vscode-test.*'
    }

def should_ignore(path, ignore_patterns):
    if not ignore_patterns:
        return False
        
    try:
        abs_path = str(path.absolute())
        if any(vscode_dir in abs_path for vscode_dir in ['vscode-linux-x64', 'node_modules.asar', 'completions']):
            return True
            
        path_str = str(path.relative_to(path.parent))
        
        if path_str in ignore_patterns:
            return True
            
        for pattern in ignore_patterns:
            if (pattern.startswith('*') and fnmatch.fnmatch(path_str, pattern)) or \
               (pattern.startswith('/') and fnmatch.fnmatch(str(path), pattern[1:])) or \
               fnmatch.fnmatch(path_str, pattern) or \
               (path.is_dir() and fnmatch.fnmatch(f"{path_str}/", f"{pattern}/")):
                return True
                    
    except ValueError:
        return False
    
    return False

def calculate_power_level(path, environments):
    power_level = 0
    
    if path.name in ['package.json', 'pyproject.toml', 'Dockerfile']:
        power_level += 3
    
    if path.suffix in ['.py', '.ts', '.js']:
        power_level += 2
        
    if path.suffix in ['.json', '.yml', '.toml']:
        power_level += 1
        
    if environments:
        power_level += max(env['power_level'] for env in environments.values())
    
    return min(power_level, 5)

def get_glyph(marker):
    return GLYPH_MARKERS.get(marker, "")