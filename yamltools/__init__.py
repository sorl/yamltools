import json
import yaml
from collections import OrderedDict


# solutions taken from:
# http://stackoverflow.com/questions/5121931/in-python-how-can-you-load-yaml-mappings-as-ordereddicts


def load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)


def dump(data, stream=None, Dumper=yaml.Dumper, **kwargs):
    class OrderedDumper(Dumper):
        pass

    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())
    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwargs)


def yaml_to_json(yaml_data, load_kwargs={}, dump_kwargs={}):
    dump_kwargs.setdefault('indent', 4)
    data = load(yaml_data, **load_kwargs)
    return json.dumps(data, **dump_kwargs)


def json_to_yaml(json_data, load_kwargs={}, dump_kwargs={}):
    load_kwargs.setdefault('object_pairs_hook', OrderedDict)
    data = json.loads(json_data, **load_kwargs)
    dump_kwargs.setdefault('default_flow_style', False)
    dump_kwargs.setdefault('indent', 4)
    return dump(data, **dump_kwargs)
