# ~/SeesTrees/src/engine/tree_parser.py
#   - handles filesystem traversal & builds semantic tree

import os
from pathlib import Path
from .node import TreeNode, GitStatus
from .utils import should_ignore, calculate_power_level

class EnvironmentMarkers:
    PYTHON_VENV = "PY_VENV"
    PYTHON_POETRY = "PY_POETRY"
    NODE_ENV = "NODE_ENV"
    DOCKER_ENV = "DOCKER_ENV"
    RUBY_ENV = "RUBY_ENV"
    GO_ENV = "GO_ENV"
    JAVA_ENV = "JAVA_ENV"
    PHP_ENV = "PHP_ENV"
    POWER_SOURCE = "POWER_SOURCE"
    POWER_FLOW = "POWER_FLOW"

class EnvironmentDetector:
    ENV_CONFIGS = {
        'python': {
            'files': ['venv', 'env', '.venv', 'pyproject.toml', 'requirements.txt'],
            'marker': EnvironmentMarkers.PYTHON_VENV,
            'power_level': 3
        },
        'node': {
            'files': ['package.json'],
            'marker': EnvironmentMarkers.NODE_ENV,
            'power_level': 3
        },
        'docker': {
            'files': ['Dockerfile', 'docker-compose.yml', 'docker-compose.yaml'],
            'marker': EnvironmentMarkers.DOCKER_ENV,
            'power_level': 4
        },
        'ruby': {
            'files': ['Gemfile'],
            'marker': EnvironmentMarkers.RUBY_ENV,
            'power_level': 2
        },
        'go': {
            'files': ['go.mod'],
            'marker': EnvironmentMarkers.GO_ENV,
            'power_level': 2
        },
        'java': {
            'files': ['pom.xml', 'build.gradle', 'build.gradle.kts'],
            'marker': EnvironmentMarkers.JAVA_ENV,
            'power_level': 3
        },
        'php': {
            'files': ['composer.json'],
            'marker': EnvironmentMarkers.PHP_ENV,
            'power_level': 2
        }
    }

    @staticmethod
    def detect_environments(directory):
        environments = {}
        
        for env_name, config in EnvironmentDetector.ENV_CONFIGS.items():
            if any(os.path.exists(os.path.join(directory, f)) for f in config['files']):
                if env_name == 'python' and os.path.exists(os.path.join(directory, 'pyproject.toml')):
                    try:
                        with open(os.path.join(directory, 'pyproject.toml'), 'r') as f:
                            if '[tool.poetry]' in f.read():
                                config['marker'] = EnvironmentMarkers.PYTHON_POETRY
                    except:
                        pass
                
                environments[env_name] = {
                    'type': env_name,
                    'marker': config['marker'],
                    'power_level': config['power_level']
                }
        
        return environments

def build_tree(directory: Path, ignore_patterns=None) -> TreeNode:
    print(f"Building: {directory}")
    if ignore_patterns is None:
        ignore_patterns = GitStatus.parse_gitignore(directory)

    entries = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
    entries = [entry for entry in entries if not should_ignore(entry, ignore_patterns)]

    children = []
    for entry in entries:
        if entry.is_dir():
            envs = EnvironmentDetector.detect_environments(entry)
            power = calculate_power_level(entry, envs)
            child_node = build_tree(entry, ignore_patterns)
            child_node.environments = envs
            child_node.power_level = power
            children.append(child_node)
        else:
            envs = EnvironmentDetector.detect_environments(entry.parent)
            power = calculate_power_level(entry, envs)
            children.append(TreeNode(entry, [], envs, power))

    return TreeNode(directory, children)