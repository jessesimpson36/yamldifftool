## Ever see a massive customized values.yaml and only want to see how it differs from upstream?


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
python3 yamldifftool.py default_values.yaml ugly.yaml --output output
```

A new file will be written named `output` (or you can specify your own filename with -o)

The new file will only contain entries without the defaults.

In this case, compare the contents of ugly.yaml with the following output

```
global:
  elasticsearch:
    prefix: zeebe-re
  identity:
    auth:
      webModeler:
        redirectUrl: http:ost:8084
  image:
    tag: 8.2.2
  ingress:
    annotations:
      nginx.ingress.kubernetes.io/ssl-redirect: brrr
  zeebePort: 265
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
