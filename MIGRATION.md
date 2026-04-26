# Migration to Portable Bundle

This version changes Xskill from a CLI-style project into a portable skill bundle.

## Remove from the old repository

Delete these if they exist:

```text
musk_skills/
tests/
pyproject.toml
```

They belonged to the earlier Python CLI prototype and are not part of the portable bundle direction.

## Keep

```text
README.md
AGENTS.md
LICENSE
CHANGELOG.md
CONTRIBUTING.md
xskill/
docs/
examples/
.github/workflows/validate.yml
```

## Release package

Create a GitHub release and upload:

```text
xskill-v0.1.0.zip
```

The release zip should contain:

```text
xskill/
AGENTS.md
README.md
LICENSE
```
