yamltools
=========
Uses ``collections.OrderedDict`` in the conversion process from YAML <-> JSON
so that order is preserved for dictionary (hash) keys and some pretty options
set for indenting.

Installation::

    pip install git+https://github.com/sorl/yamltools.git


Usage::

    from yamltools import yaml_to_json, json_to_yaml


    print(yaml_to_json(yaml_data))
    print(json_to_yaml(json_data))


Available methods::

    yamltools.yaml_to_json
    yamltools.json_to_yaml
    yamltools.dump
    yamltools.load

