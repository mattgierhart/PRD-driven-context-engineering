#!/usr/bin/env bash
set -euo pipefail

experiment_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
runtime_dir="${experiment_dir}/.runtime"
source_dir="${runtime_dir}/kuzu-source"
venv_dir="${experiment_dir}/.venv"
expected_commit="27cba5b91423c96a0a0507c92dfe0e1654f7f184"

mkdir -p "${runtime_dir}"

if [[ ! -d "${source_dir}/.git" ]]; then
  git clone \
    --branch v0.11.3 \
    --depth 1 \
    https://github.com/kuzudb/kuzu.git \
    "${source_dir}"
fi

actual_commit="$(git -C "${source_dir}" rev-parse HEAD)"
if [[ "${actual_commit}" != "${expected_commit}" ]]; then
  echo "Kuzu checkout mismatch: expected ${expected_commit}, got ${actual_commit}" >&2
  exit 1
fi

uv venv \
  --python 3.11.13 \
  --no-python-downloads \
  --clear \
  "${venv_dir}"
uv pip install \
  --python "${venv_dir}/bin/python" \
  --only-binary :all: \
  --require-hashes \
  --requirement "${experiment_dir}/requirements.lock"

"${venv_dir}/bin/python" -c \
  'import kuzu; print(f"Kuzu Python package: {kuzu.__version__}")'
echo "Kuzu source: ${actual_commit}"
