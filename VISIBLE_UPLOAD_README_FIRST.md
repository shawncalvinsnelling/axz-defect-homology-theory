# AXZ Defect Homology Theory — Ultimate Visible Upload Package

This package intentionally contains **no hidden files or hidden folders**.
It is designed for GitHub web upload when hidden files such as `.github/` or `.gitignore` are hard to drag into the browser.

## Upload method

1. Extract the ZIP.
2. Open this folder.
3. Drag everything visible inside this folder into GitHub.
4. Commit with:

```text
Release AXZ Defect Homology Theory Ultimate Visible Upload
```

## Important note about GitHub Actions

GitHub Actions requires a hidden path:

```text
.github/workflows/verify.yml
```

This visible package includes the workflow as:

```text
GITHUB_ACTIONS_WORKFLOW_VERIFY_YML_VISIBLE_COPY.txt
```

So the repository will upload cleanly without hidden files, but Actions will not run automatically until that workflow template is copied into the required hidden GitHub path.

The core verifier still runs locally with:

```bash
bash RUN_ALL.sh
pytest -q
```
