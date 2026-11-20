# Read a rack inventory with Python

A handoff lists three assets. A technician needs the names of the switches. In Python, a list can hold the records in order, and a dictionary lets you look up a field by name. Use Python 3 in Ubuntu.

```bash
python3 - <<'PY'
assets = [
    {"name": "sw-a", "role": "switch"},
    {"name": "web-a", "role": "server"},
    {"name": "sw-b", "role": "switch"},
]
for asset in assets:
    if asset["role"] == "switch":
        print(asset["name"])
PY
```

You should see sw-a and sw-b. Predict what changes if you replace the comparison value with server, then run it again. A zero-line result for an unknown role means the loop found zero matches. A KeyError for a misspelled field means the program couldn't read that field.

**Exam connection.** This practices Linux+ objective 4.3 through list iteration and dictionary lookup. The input is a local example, so it requires no access to network equipment.

[Table of contents](../README.md)
