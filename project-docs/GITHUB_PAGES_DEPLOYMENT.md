# GitHub Pages deployment

This repository supports GitHub Pages deployment from the `main` branch without GitHub Actions.

1. Run `npm run build:pages`.
2. Commit the updated `/docs` folder.
3. In GitHub **Settings → Pages**, choose **Deploy from a branch**.
4. Select branch: `main`.
5. Select folder: `/docs`.
6. Save.

The script sets the project-page base path to `/${REPOSITORY_NAME}` by default. Override with `NEXT_PUBLIC_BASE_PATH=/your-repo npm run build:pages` if needed.
