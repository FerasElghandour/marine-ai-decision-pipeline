"""Offline example using the public implementation; see README for evidence scope."""
import sys,json,pathlib,os
repo=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(repo));sys.path.insert(0,str(repo/'src'));os.chdir(repo)
import ast
nb=json.loads((repo/'analysis.ipynb').read_text());scope={'json':json,'TOOL_REGISTRY':{},'HARVEST_MIN_RINGS':11,'CONFIDENCE_THRESHOLD':.8}
for cell in nb['cells']:
 if cell['cell_type']!='code':continue
 tree=ast.parse(''.join(cell['source']))
 for node in tree.body:
  if isinstance(node,ast.FunctionDef) and node.name in ['register_tool','harvest_decision']:exec(compile(ast.Module(body=[node],type_ignores=[]),'analysis.ipynb','exec'),scope)
cases=[{'predicted_rings':12,'confidence':.9},{'predicted_rings':12,'confidence':.7},{'predicted_rings':8,'confidence':.9}]
print(json.dumps({"fixture":"supplied hypothetical predictions, not RF outputs or valid harvest policy","decisions":[scope['harvest_decision'](json.dumps(case)) for case in cases]}))
