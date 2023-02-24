# Get Config Value

Version: 0.1.0

Given a JSON/YAML/TOML file, extract a value given by the key.

## Usage

```yaml

# It is better practice to use the SHA hash of this tag rather than the tag itself.
- uses: ajparsons/get-config-value@v0
  id: example-step 
  with:
    file: '' 
    key: '' 
    venv_path: '/tmp/get-config-value-venv'  # default

```

## Inputs

### file

Config file to read

### key

Key to get, dot-seperated levels ('first_level.2.value')

### venv_path

Venv path for action (optional)

Default: /tmp/get-config-value-venv

## Outputs

### value

Returned value

