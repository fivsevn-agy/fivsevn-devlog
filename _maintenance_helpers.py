"""Small one-time internal fixes against reviewed source; no external requests."""
from pathlib import Path
import sys
root=Path(sys.argv[1])
p=root/'scripts/apply_draft_frontmatter.py';s=p.read_text()
assert 'title: {title}' in s
s=s.replace('import re\n','import re\nimport json\n')
s=s.replace('title: {title}\n','title: {json.dumps(title, ensure_ascii=False)}\n')
p.write_text(s)
p=root/'scripts/update_module_indexes.py';s=p.read_text()
s=s.replace('from pathlib import Path\n','from pathlib import Path\nfrom datetime import date\n\nimport yaml\n')
s=s.replace('"exclude_dirs": {"assets", "_drafts", "ai-discourse-analysis"}', '"exclude_dirs": {"assets", "_drafts", "_wordpress", "ai-discourse-analysis"}')
start=s.index('    """Parse simple YAML front matter');end=s.index('\n\ndef normalize_date',start)
s=s[:start]+'''    """Read real YAML scalars; quoting and multiline values retain their meaning."""
    lines = text.lstrip("\\ufeff").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return None
    try:
        meta = yaml.safe_load("\\n".join(lines[1:end])) or {}
    except yaml.YAMLError:
        return None
    if not isinstance(meta, dict):
        return None
    return {str(k): str(v) for k, v in meta.items() if v is not None and not isinstance(v, (list, dict))}
''' + s[end:]
s=s.replace('    return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"','    try:\n        return date(int(year), int(month), int(day)).isoformat()\n    except ValueError:\n        return None')
s=s.replace('return pattern.sub(replacement, text), True','return pattern.sub(lambda _: replacement, text), True')
p.write_text(s)
p=root/'.github/workflows/update-indexes.yml';s=p.read_text()
marker='      - name: Update module indexes\n'
assert marker in s
s=s.replace(marker,'      - uses: actions/setup-python@v5\n        with:\n          python-version: "3.11"\n\n      - name: Install metadata parser\n        run: python -m pip install pyyaml\n\n'+marker)
p.write_text(s)
