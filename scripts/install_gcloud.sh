#!/usr/bin/env bash

set -euo pipefail

export PATH="$HOME/google-cloud-sdk/bin:$PATH"

if command -v gcloud >/dev/null 2>&1; then
    echo "gcloud CLI is already installed."
else
    echo "Installing gcloud CLI..."
    curl -fsSL https://sdk.cloud.google.com | bash -s -- --disable-prompts --install-dir="$HOME"
fi

path_entry='export PATH="$HOME/google-cloud-sdk/bin:$PATH"'
if [ -d "$HOME/google-cloud-sdk/bin" ] && ! grep -Fxq "$path_entry" "$HOME/.bashrc" 2>/dev/null; then
    printf '\n%s\n' "$path_entry" >> "$HOME/.bashrc"
fi

gcloud --version
