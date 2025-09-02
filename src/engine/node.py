# ~/SeesTrees/src/engine/node.py

from pathlib import Path
import subprocess
from .utils import get_default_ignore_patterns

class TreeNode:
    def __init__(self, path: Path, children=None, environments=None, power_level=0):
        self.path = path
        self.children = children or []
        self.environments = environments or {}
        self.power_level = power_level

    def add_child(self, node):
        self.children.append(node)
        
class GitStatus:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.status = self._run_git_command(['git', 'status', '--porcelain'])
        self.branch = self._run_git_command(['git', 'branch', '--show-current'])
        self.last_commit = self._run_git_command(['git', 'log', '-1', '--format=%h %s'])
        
        self.status = {
            line[3:]: line[:2].strip()
            for line in self.status.splitlines()
        } if self.status else {}
        
    def _run_git_command(self, command):
        try:
            result = subprocess.run(command, cwd=self.repo_path, capture_output=True, text=True)
            return result.stdout.strip()
        except:
            return ""

    def get_file_status(self, file_path):
        try:
            relative_path = str(Path(file_path).relative_to(self.repo_path))
            if isinstance(self.status, dict):
                return self.status.get(relative_path, '')
            else:
                return ''
        except ValueError:
            return ''

    @staticmethod
    def parse_gitignore(repo_path):
        patterns = get_default_ignore_patterns()
        gitignore_path = Path(repo_path) / '.gitignore'
        
        if gitignore_path.exists():
            with open(gitignore_path, 'r') as f:
                patterns.update(
                    line.strip()[:-1] if line.strip().endswith('/') else line.strip()
                    for line in f
                    if line.strip() and not line.startswith('#')
                )
        
        return patterns