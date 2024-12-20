# YAML Diff Tool

This tool allows you to compare a customized `values.yaml` file against the upstream defaults, highlighting the differences.

## Table of Contents
- [Installation](#installation)
    - [Helm Plugin Installation](#helm-plugin-installation)
    - [Manual Installation](#manual-installation)
- [Usage](#usage)
    - [Command Line Interface](#command-line-interface)
    - [Examples](#examples)
- [Info](#info)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Helm Plugin Installation

```sh
helm plugin install https://github.com/jessesimpson36/yamldifftool.git
````

Then you may access the cli by using the command

```sh
helm yamldiff
```

### Manual Installation

To run the application, you need python3 installed and to run
```
pip install -r requirements.txt
```


## Usage

### Command line interface

Format:
```
python3 yamldifftool.py <base_values.yaml>  <customized_values.yaml> --output <output_filename>
```

### Examples
```
python3 yamldifftool.py test/default_values.yaml test/large_copied_values.yaml --output test/output.yaml
```

A new file will be written named `test/output.yaml` (or you can specify your own filename with -o)

The new file will only contain entries without the defaults.

In this case, compare the contents of `test/large_copied_values.yaml` with the defaults to produce the following output.

```yaml
global:
  badOption:
    jesse:
    - hi
    - there
  image:
    tag: 8.2.2
  ingress:
    annotations:
      nginx.ingress.kubernetes.io/ssl-redirect: brrr
  elasticsearch:
    prefix: zeebe-re
  zeebePort: 265
  identity:
    auth:
      webModeler:
        redirectUrl: http:ost:8084
zeebe:
  env:
  - name: ZEEBE_BROKER_DATA_SNAPSHOTPERIOD
    value: 5m
  - name: ZEEBE_BROKER_DATA_DISKUSAGECOMMANDWATERMARK
    value: '0.85'
  - name: ZEEBE_BROKER_DATA_DISKUSAGEREPLICATIONWATERMARK
    value: '0.87'
  - name: JESSE_HI
    value: hi
```

## Info
This tool helps you compare a customized values.yaml file with the upstream defaults and outputs the differences.  

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.  

## License
This project is licensed under the MIT License.

