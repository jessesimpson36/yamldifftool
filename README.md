## Ever see a massive customized values.yaml and only want to see how it differs from upstream?


### Helm plugin installation

```sh
helm plugin install https://github.com/jessesimpson36/yamldifftool.git
```

Then you may access the cli by using the command

```sh
helm yamldiff
```

instead of `python3 yamldifftool.py ...`


### Installation

To run the application, you need python3 installed and to run
```
pip install -r requirements.txt
```


### Info

Format:
```
python3 yamldifftool.py <base_values.yaml>  <customized_values.yaml> --output <output_filename>
```

```
python3 yamldifftool.py test/default_values.yaml test/ugly.yaml --output test/output.yaml
```

A new file will be written named `test/output.yaml` (or you can specify your own filename with -o)

The new file will only contain entries without the defaults.

In this case, compare the contents of `test/ugly.yaml` with the defaults to produce the following output.

```
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


