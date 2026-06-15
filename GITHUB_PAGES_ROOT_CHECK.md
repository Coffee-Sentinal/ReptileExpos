# GitHub Pages root deployment check

This repository is intended to publish the ExpoWatch static dashboard directly from the repository root.

Use this exact GitHub Pages configuration:

1. Go to **Settings → Pages**.
2. Set **Source** to **Deploy from a branch**.
3. Set **Branch** to `main`.
4. Set **Folder** to `/ (root)`.
5. Save and wait for GitHub Pages to republish.

The repository root must contain these files in the GitHub web UI before Pages is refreshed:

- `index.html`
- `style.css`
- `app.js`
- `.nojekyll`
- `data/events.json`

If the Pages site renders README text instead of the dashboard, GitHub Pages is serving an older commit or the wrong folder. Open `/index.html` directly to check whether the dashboard file is published, then hard-refresh after Pages finishes rebuilding.

No npm, Node build, Next.js export, `/docs` folder, GitHub Actions deployment, backend, or database is required.
