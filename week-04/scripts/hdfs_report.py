#!/usr/bin/env python3
"""W3 - reports how a file is stored in HDFS.

Runs `hdfs fsck` and turns its output into three numbers. The shell is fine for
starting containers; pulling numbers out of text is Python's job, which is why
this script is Python and load_to_hdfs.sh is not.

Usage:
    python3 scripts/hdfs_report.py /taxi/yellow_tripdata_2024-01.parquet

Fill in the places marked TODO.
"""
import re
import subprocess
import sys

COMPOSE = ["docker", "compose", "-f", "compose-hdfs.yml", "exec", "-T", "namenode"]


def fsck(path: str) -> str:
    """Return the raw output of `hdfs fsck <path>` run inside the cluster."""
    # TODO 1: run `hdfs fsck <path>` through COMPOSE and return its stdout as text.
    #         Hint: subprocess.run(COMPOSE + [...], capture_output=True, text=True)
    return subprocess.run(COMPOSE + ["hdfs", "fsck", path], capture_output=True, text=True).stdout # What about stderr?


def parse(report: str) -> dict:
    """Pull the numbers we care about out of the fsck output.

    Return a dict with keys: size, files, blocks, replication.
    The lines you are looking for are shaped like:

        Total size:                    49961641 B
        Total files:                   1
        Total blocks (validated):      2 (avg. block size 24980820 B)
        Average block replication:     2.0
    """
    # TODO 2: extract the four values above. Regular expressions are the point
    #         of this exercise - do NOT build a pipeline of grep and cut.
    return {
           "size": int(re.search(r"^[ \t]*Total size:[ \t]*(\d+)[ \t]+B", report, re.MULTILINE).group(1)), # ty: ignore
           "files": int(re.search(r"^[ \t]*Total files:[ \t]*(\d+)", report, re.MULTILINE).group(1)), # ty: ignore
           "blocks": int(re.search(r"^[ \t]*Total blocks \(validated\):[ \t]*(\d+)", report, re.MULTILINE).group(1)), # ty: ignore
           "replication": float(re.search(r"^[ \t]*Average block replication:[ \t]*(\d+(?:\.\d+)?)", report, re.MULTILINE).group(1)), # ty: ignore
       }




def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: hdfs_report.py <hdfs-path>")
    path = sys.argv[1]
    data = parse(fsck(path))

    print(f"path        : {path}")
    print(f"size        : {data['size']:,} B")
    print(f"files       : {data['files']}")
    print(f"blocks      : {data['blocks']}")
    print(f"replication : {data['replication']}")

    # TODO 3: print how much space the file occupies across all replicas,
    #         and how many map tasks a MapReduce job would start on it.
    #         Both follow from the numbers above - no extra call needed.


if __name__ == "__main__":
    main()
