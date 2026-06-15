# GitHub Pages deployment

1. Enable GitHub Pages with source set to GitHub Actions.
2. Push to `main`.
3. `.github/workflows/deploy-pages.yml` installs dependencies and runs `npm run build`.
4. Next.js writes static files to `out/`.
5. The workflow uploads and deploys `out/`.

For project pages, the workflow sets `NEXT_PUBLIC_BASE_PATH` to the repository name. Locally, leave it empty.
