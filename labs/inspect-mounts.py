"""Show named volumes and destinations in a docker inspect JSON array."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capture", type=Path)
    args = parser.parse_args()
    with args.capture.open(encoding="utf-8") as stream:
        containers = json.load(stream)
    for container in containers:
        print(container["Name"].lstrip("/"), container["State"]["Status"])
        volumes = [mount for mount in container["Mounts"] if mount["Type"] == "volume"]
        if not volumes:
            print("  No volume mounts reported")
        for mount in volumes:
            access = "rw" if mount["RW"] else "ro"
            print(f"  {mount['Name']} -> {mount['Destination']} ({access})")


if __name__ == "__main__":
    main()
