# ShellRosetta API Documentation

## Core Functions

### `lnx2ps(command: str, use_ml: bool = True, use_plugins: bool = True) -> str`

Translates a Linux command to PowerShell equivalent with optional ML and plugin support.

**Parameters:**

- `command` (str): The Linux command to translate
- `use_ml` (bool): Whether to use machine learning suggestions (default: True)
- `use_plugins` (bool): Whether to use plugin translations (default: True)

**Returns:**

- `str`: The PowerShell equivalent command

**Example:**

```python
from shellrosetta.core import lnx2ps

result = lnx2ps("ls -alh | grep error")
# Returns: "Get-ChildItem -Force | Format-List | Select-String error"

# Disable ML and plugins for core-only translation
result = lnx2ps("ls -la", use_ml=False, use_plugins=False)
```

### `ps2lnx(command: str, use_ml: bool = True, use_plugins: bool = True) -> str`

Translates a PowerShell command to Linux equivalent with optional ML and plugin support.

**Parameters:**

- `command` (str): The PowerShell command to translate
- `use_ml` (bool): Whether to use machine learning suggestions (default: True)
- `use_plugins` (bool): Whether to use plugin translations (default: True)

**Returns:**

- `str`: The Linux equivalent command

**Example:**

```python
from shellrosetta.core import ps2lnx

result = ps2lnx("Get-ChildItem -Force | Select-String error")
# Returns: "ls -a | grep error"
```

## Advanced Command Parsing

### `parser.parse(command: str) -> ASTNode`

Parse a command string into an Abstract Syntax Tree.

**Parameters:**

- `command` (str): The command to parse

**Returns:**

- `ASTNode`: The parsed command tree

**Example:**

```python
from shellrosetta.parser import parser

ast = parser.parse("ls -la | grep error")
flags = parser.extract_flags(ast)
args = parser.extract_arguments(ast)
cmd_name = parser.get_command_name(ast)
```

### `parser.extract_flags(node: ASTNode) -> List[str]`

Extract all flags from an AST node.

### `parser.extract_arguments(node: ASTNode) -> List[str]`

Extract all arguments from an AST node.

### `parser.get_command_name(node: ASTNode) -> str`

Get the command name from an AST node.

## Machine Learning Engine

### `ml_engine.learn_pattern(command: str, translation: str, direction: str, success: bool = True) -> None`

Learn a new command pattern for future translations.

**Parameters:**

- `command` (str): The original command
- `translation` (str): The translated command
- `direction` (str): Translation direction ("lnx2ps" or "ps2lnx")
- `success` (bool): Whether the translation was successful

**Example:**

```python
from shellrosetta.ml_engine import ml_engine

ml_engine.learn_pattern("ls -la", "Get-ChildItem -Force | Format-List", "lnx2ps", success=True)
```

### `ml_engine.get_best_translation(command: str, direction: str) -> Optional[str]`

Get the best learned translation for a command.

**Parameters:**

- `command` (str): The command to translate
- `direction` (str): Translation direction

**Returns:**

- `Optional[str]`: The best translation or None if not found

### `ml_engine.get_suggestions(partial_command: str, direction: str, limit: int = 5) -> List[Tuple[str, float]]`

Get suggestions for a partial command.

**Parameters:**

- `partial_command` (str): The partial command
- `direction` (str): Translation direction
- `limit` (int): Maximum number of suggestions

**Returns:**

- `List[Tuple[str, float]]`: List of (translation, confidence) tuples

### `ml_engine.analyze_patterns() -> Dict[str, Any]`

Analyze learned patterns for insights.

**Returns:**

- `Dict[str, Any]`: Analysis including total patterns, success rate, command types, etc.

## Plugin System

### `plugin_manager.translate_with_plugins(command: str, direction: str) -> Optional[str]`

Try to translate using plugins first, fall back to core.

**Parameters:**

- `command` (str): The command to translate
- `direction` (str): Translation direction

**Returns:**

- `Optional[str]`: Plugin translation or None if no plugin handles it

### `plugin_manager.list_plugins() -> List[Dict[str, Any]]`

List all loaded plugins.

**Returns:**

- `List[Dict[str, Any]]`: List of plugin metadata

### `plugin_manager.install_plugin(plugin_path: str) -> bool`

Install a plugin from a file path.

**Parameters:**

- `plugin_path` (str): Path to the plugin file

**Returns:**

- `bool`: True if installation successful

## Configuration

### `config.get(key: str, default=None) -> Any`

Get a configuration value.

**Parameters:**

- `key` (str): Configuration key
- `default`: Default value if key not found

**Returns:**

- Configuration value

**Example:**

```python
from shellrosetta.config import config

show_notes = config.get('show_notes', True)
```

### `config.set(key: str, value: Any) -> None`

Set a configuration value.

**Parameters:**

- `key` (str): Configuration key
- `value`: Value to set

**Example:**

```python
from shellrosetta.config import config

config.set('color_output', False)
```

## Utilities

### `colored(text: str, color: str) -> str`

Return colored text if color output is enabled.

**Parameters:**

- `text` (str): Text to colorize
- `color` (str): Color code from `Colors` class

**Returns:**

- `str`: Colored text or original text

**Example:**

```python
from shellrosetta.utils import colored, Colors

colored_text = colored("Hello World", Colors.OKGREEN)
```

### `sanitize_command(command: str) -> Optional[str]`

Sanitize command input for safe processing.

**Parameters:**

- `command` (str): Command to sanitize

**Returns:**

- `Optional[str]`: Sanitized command or None if dangerous

**Example:**

```python
from shellrosetta.utils import sanitize_command

safe_cmd = sanitize_command("ls -la; rm -rf /")  # Returns None
safe_cmd = sanitize_command("ls -la")  # Returns "ls -la"
```

## Web API

### `run_api_server(host='0.0.0.0', port=5000, debug=False) -> None`

Start the ShellRosetta web API server.

**Parameters:**

- `host` (str): Host to bind to (default: '0.0.0.0')
- `port` (int): Port to bind to (default: 5000)
- `debug` (bool): Enable debug mode (default: False)

**Example:**

```python
from shellrosetta.api import run_api_server

run_api_server(port=8080)
```

## Creating Custom Plugins

To create a custom plugin, inherit from `CommandPlugin`:

```python
from shellrosetta.plugins import CommandPlugin

class MyCustomPlugin(CommandPlugin):
    def get_name(self) -> str:
        return "my_custom"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def get_supported_commands(self) -> List[str]:
        return ["my_command"]
    
    def translate(self, command: str, direction: str) -> Optional[str]:
        if "my_command" in command:
            return "translated_command"
        return None

# Create plugin instance
my_plugin = MyCustomPlugin()
```

## Adding Custom Mappings

To add custom command mappings, modify the mapping dictionaries in `mappings.py`:

```python
# Add to LINUX_TO_PS for Linux to PowerShell mappings
LINUX_TO_PS["my_command"] = ("My-PowerShell-Command", "Optional note")

# Add to PS_TO_LINUX for PowerShell to Linux mappings
PS_TO_LINUX["My-PowerShell-Command"] = ("my_command", "Optional note")
```

## Extending Flag Mappings

To add flag mappings for a new command:

```python
# Add flag mapping dictionary
MY_COMMAND_FLAGS_MAP = {
    "": "",
    "-a": "-All",
    "-v": "-Verbose",
    "-av": "-All -Verbose",
}

# Update fallback_flag_translate function in core.py
elif cmd == "my_command":
    base = "My-PowerShell-Command"
    flagmap = MY_COMMAND_FLAGS_MAP
```

## Web API Endpoints

When running the web server, the following endpoints are available:

- `GET /` - Web interface
- `POST /api/translate` - Command translation
- `GET /api/stats` - Usage statistics
- `GET /api/plugins` - Plugin listing
- `POST /api/learn` - Manual pattern learning
- `POST /api/cleanup` - Clean up old patterns

### Example API Usage

```python
import requests

# Translate a command
response = requests.post('http://localhost:5000/api/translate', json={
    'command': 'ls -la',
    'direction': 'lnx2ps'
})
result = response.json()
print(result['translation'])

# Get statistics
response = requests.get('http://localhost:5000/api/stats')
stats = response.json()
print(f"Total patterns: {stats['total_translations']}")
```
