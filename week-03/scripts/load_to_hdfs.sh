#!/usr/bin/env bash
# W3 - loads the yearly dataset into HDFS.
# Runs INSIDE the cluster, where the hdfs client and its configuration live:
#   docker compose -f compose-hdfs.yml exec namenode bash /scripts/load_to_hdfs.sh | tee out/02-load.log
# Must be re-runnable: after the cluster is destroyed you want to restore
# the state with one command, not twelve.
#
# Fill in the places marked TODO.
set -euo pipefail

HDFS_DIR="/taxi"
LOCAL_DIR="${1:-/mnt/host}"

echo "== creating target directory in HDFS =="
# TODO 1: create $HDFS_DIR in HDFS, ignoring the case where it already exists.
#         Hint: hdfs dfs -mkdir -p
hdfs dfs -mkdir -p $HDFS_DIR

echo "== uploading files =="
for f in "$LOCAL_DIR"/yellow_tripdata_2024-*.parquet; do
  echo "  -> $(basename "$f")"
  # TODO 2: upload $f into $HDFS_DIR, overwriting an existing copy.
  #         Hint: hdfs dfs -put -f
  hdfs dfs -put -f $f $HDFS_DIR
done

echo "== verification =="
# TODO 3: list $HDFS_DIR and print how many files ended up there.
#         The count must be 12.

# There is no `wc` command
# hdfs dfs -ls | -wc -l
hdfs dfs -count $HDFS_DIR
