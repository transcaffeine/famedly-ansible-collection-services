import yaml
import os

def load_dir_rec(path):
  for node in os.scandir(path):
    if node.is_dir():
      load_dir(node.path)
    else:
      for k,v in yaml.safe_load(open(node.path)).items():
        globals()[k] = v # we just add *all* the kv pairs to the scope netbox will use to access it's config

load_dir_rec(os.environ.get('NETBOX_YAML_CONFIG_DIR','/opt/netbox/config'))
