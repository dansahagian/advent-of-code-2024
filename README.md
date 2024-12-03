# Advent of Code, 2024

## To quickly bootstrap an environment using uv
If you already using uv, ruff, and pre-commit, you can skip to the last step.

Install uv:
https://docs.astral.sh/uv/

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install `ruff` and `pre-commit`:
```shell
uv tool install ruff
uv tool install pre-commit
```

Make sure these are on your PATH:
```shell
export PATH=$PATH:~/.cargo/bin
export PATH=$PATH:~/.local/bin
```

Run the `initialize-env` dev script
```shell
./dev/initialize-env
```