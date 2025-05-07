import yaml

def fix_yaml(path="broken-ci.yml"):
    with open(path, "r") as f:
        content = yaml.safe_load(f)
    
    # Basic fix for demonstration
    content['jobs']['build']['steps'][0]['run'] = 'echo "Hello from fixed build"'
    
    with open(path, "w") as f:
        yaml.dump(content, f)
