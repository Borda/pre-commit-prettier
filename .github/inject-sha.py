import yaml

THIS_REPO = "https://github.com/JoC0de/pre-commit-prettier"
PRE_COMMIT_CONFIG = ".pre-commit-config.yaml"

def main(sha: str) -> None:
    """Inject the SHA into the YAML file."""
    # Load the YAML file
    with open(PRE_COMMIT_CONFIG, "r", encoding="utf-8") as fo:
        config = yaml.safe_load(fo)

    # Inject the SHA into the config
    for i, repo in enumerate(config.get("repos", [])):
        if repo.get("repo") != THIS_REPO:
            continue
        print(f"Injecting SHA `{sha}` into repo {repo}")
        config["repos"][i]["rev"] = sha

    # Save the updated config back to the file
    with open(PRE_COMMIT_CONFIG, "w", encoding="utf-8") as fo:
        yaml.safe_dump(config, fo, default_flow_style=False)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python inject-sha.py <sha>")
        sys.exit(1)

    sha = sys.argv[1]
    main(sha)
    print(f"SHA `{sha}` injected into .pre-commit-config.yaml")