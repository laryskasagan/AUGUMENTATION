import sys
import nbformat
from nbclient import NotebookClient

path = sys.argv[1]
nb = nbformat.read(path, as_version=4)

for cell in nb.cells:
    if cell.get("cell_type") == "code":
        cell["outputs"] = []
        cell["execution_count"] = None

client = NotebookClient(
    nb,
    timeout=1800,
    kernel_name="python3",
    resources={"metadata": {"path": "."}},
)
client.execute()

nbformat.write(nb, path)
print("EXECUTED_OK")
