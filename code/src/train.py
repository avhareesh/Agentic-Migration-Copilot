# -*- coding: utf-8 -*-
"""Agentic Migration Copilot.

Run:
    python -m code.src.train --config code/configs/config.yaml --data_dir data/sample
"""
import argparse
from pathlib import Path
import yaml

def load_config(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description="Train a simple model (skeleton).")
    parser.add_argument("--config", type=str, required=True, help="Path to YAML config.")
    parser.add_argument("--data_dir", type=str, required=True, help="Path to data directory.")
    args = parser.parse_args()

    cfg = load_config(Path(args.config))
    data_dir = Path(args.data_dir)

    # TODO: replace with real dataset/model/training loop
    print("[INFO] Loaded config:", cfg)
    print("[INFO] Using data_dir:", data_dir.resolve())
    print("[OK] Training skeleton complete. Implement your ML/DL pipeline here.")

if __name__ == "__main__":
    main()
