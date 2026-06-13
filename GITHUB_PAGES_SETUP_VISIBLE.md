# GitHub Pages Setup — Visible Upload Version

This package contains no hidden files. The live website works from the visible root `index.html`.

## Upload

1. Extract the ZIP.
2. Open the extracted folder.
3. Drag all visible files and folders into the GitHub repo upload page.
4. Commit.

## Enable Pages

Go to:

```text
Settings → Pages
```

Use:

```text
Source: Deploy from a branch
Branch: main
Folder: / root
```

Save. Your site should appear at:

```text
https://shawncalvinsnelling.github.io/axz-defect-homology-theory/
```

## Optional Actions

GitHub Actions requires a hidden path. If you want Actions later, create:

```text
.github/workflows/verify.yml
```

Then paste the contents of:

```text
GITHUB_ACTIONS_WORKFLOW_VERIFY_YML_VISIBLE_COPY.txt
```
