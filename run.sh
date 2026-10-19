#!/usr/bin/env bash
set -euo pipefail

cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

case "${1:-dev}" in
    build)
        exec npm run build
        ;;
    serve)
        shift
        exec uv run uvicorn main:app --app-dir app "$@"
        ;;
    dev)
        if (( $# )); then shift; fi

        # Build once before accepting requests, then keep assets up to date.
        npm run build

        processes=()
        cleanup() {
            trap '' INT TERM
            for pid in "${processes[@]}"; do
                # Each session includes npm/uv and all their child processes.
                kill -TERM -- "-$pid" 2>/dev/null || true
            done
            for pid in "${processes[@]}"; do
                wait "$pid" 2>/dev/null || true
            done
        }
        trap cleanup EXIT
        trap 'exit 130' INT
        trap 'exit 143' TERM

        setsid npm run dev &
        processes+=("$!")
        setsid uv run uvicorn main:app --app-dir app --reload "$@" &
        processes+=("$!")

        # Stop the other process if either command exits.
        status=0
        wait -n "${processes[@]}" || status=$?
        exit "$status"
        ;;
    *)
        echo "Usage: ./run.sh [dev|build|serve] [uvicorn options]" >&2
        exit 2
        ;;
esac
