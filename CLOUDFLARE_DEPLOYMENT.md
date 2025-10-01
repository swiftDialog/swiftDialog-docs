# Cloudflare Pages Deployment Settings

## Base Setup for Cloudflare

## Build configuration
- Build command: `npm run build``
- Build output: `dist`
- Root directory: `/`
- Build comments: `Enabled`

## Branch control
- Production branch: `main`
- Automatic deployments: `Enabled`

## Production System Version

- Version 3
[ Go: 1.24.3 | Node.js: 22.16.0 | Bun: 1.2.15 | Python: 3.13.3 | Ruby: 3.4.4 ] 

## Required API Token Permissions

Your Cloudflare API token needs:
- Cloudflare Pages: Edit
- Account: Cloudflare Pages:Read

- Containers: Edit, Secrets Store:Edit, Browser Rendering:Edit, AI Gateway:Run, Workers Pipelines:Edit, AI Gateway:Edit, AI Gateway:Read, Workers AI:Edit, Queues:Edit, Vectorize:Edit, Hyperdrive:Edit, Cloudchamber:Edit, D1:Edit, Cloudflare 

- Pages:Edit, Workers R2 Storage:Edit, Workers KV Storage:Edit, Workers 

- Scripts: Edit, 
- Account Settings:Read
- All zones - Workers Routes:Edit
- All users - Memberships:Read, User Details:Read

