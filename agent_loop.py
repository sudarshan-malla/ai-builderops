from diagnose import diagnose_ci_error
from patcher import fix_yaml
from git_ops import commit_and_push

print("🤖 Diagnosing...")
print(diagnose_ci_error("latest_error.json"))

print("🛠️ Fixing YAML...")
fix_yaml()

print("🚀 Pushing Fix...")
commit_and_push(".")
