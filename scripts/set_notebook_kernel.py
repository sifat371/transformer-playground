import nbformat, sys
nb_path = sys.argv[1]
kernel_name = sys.argv[2] if len(sys.argv) > 2 else "python3"

nb = nbformat.read(nb_path, as_version=4)
nb.setdefault("metadata", {})
nb["metadata"].setdefault("kernelspec", {})
nb["metadata"]["kernelspec"]["name"] = kernel_name
nb["metadata"]["kernelspec"]["display_name"] = f"Python ({kernel_name})"
nbformat.write(nb, nb_path)
print("Updated", nb_path, "→ kernel:", kernel_name)