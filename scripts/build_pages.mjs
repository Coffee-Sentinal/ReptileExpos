import { cpSync, existsSync, mkdirSync, rmSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';

const repoName = process.env.GITHUB_REPOSITORY?.split('/')[1] || 'ReptileExpos';
const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? process.env.PAGES_BASE_PATH ?? `/${repoName}`;

console.log(`Building ExpoWatch static export for GitHub Pages base path: ${basePath}`);
const nextBin = join(process.cwd(), 'node_modules', '.bin', process.platform === 'win32' ? 'next.cmd' : 'next');
if (!existsSync(nextBin)) {
  console.error('Next.js is not installed. Run `npm install` before `npm run build:pages`.');
  process.exit(1);
}
const build = spawnSync(
  nextBin,
  ['build'],
  {
    stdio: 'inherit',
    env: {
      ...process.env,
      NEXT_PUBLIC_BASE_PATH: basePath,
    },
  },
);

if (build.status !== 0) {
  process.exit(build.status ?? 1);
}

const outDir = join(process.cwd(), 'out');
const docsDir = join(process.cwd(), 'docs');
if (!existsSync(outDir)) {
  console.error('Expected Next.js static export directory `out/` was not found.');
  process.exit(1);
}

rmSync(docsDir, { recursive: true, force: true });
mkdirSync(docsDir, { recursive: true });
cpSync(outDir, docsDir, { recursive: true });
writeFileSync(join(docsDir, '.nojekyll'), '');

if (!existsSync(join(docsDir, 'index.html'))) {
  console.error('Static export copy failed: docs/index.html was not created.');
  process.exit(1);
}

console.log('Copied static export to docs/ and added docs/.nojekyll.');
