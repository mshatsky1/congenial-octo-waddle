#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH=${PYTHONPATH:-src} pytest "$@"
