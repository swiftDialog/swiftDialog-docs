# swiftDialog Documentation Site

An Astro-based documentation site for swiftDialog, built with Starlight theme and optimized for Cloudflare Pages deployment.

## 🚀 Quick Start

### Development

```bash
# Install dependencies
pnpm install

# Start development server
pnpm run dev

# Build for production
pnpm run build

# Preview production build
pnpm run preview
```

## Deplyoing to Cloudflare 

### Option 1: GitHub Integration (Recommended)

1. Push this repository to GitHub
2. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/) > Pages
3. Click "Create a project" > "Connect to Git"
4. Select your repository
5. Configure build settings:
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
   - **Environment variables**: `NODE_VERSION = 20`
6. Click "Save and Deploy"

### Option 2: Direct Upload

```bash
# Build the site
npm run build

# Deploy to Cloudflare Pages (requires wrangler CLI)
npx wrangler pages deploy dist --project-name=swiftdialog-docs
```
## Configuration

### Site Configuration
Edit `astro.config.mjs` to update:
- Site title and description
- Navigation structure
- Social links
- Custom theme settings

### Theme Customization
The site uses a lightly customized version of Starlight's default theme.
Edit `src/styles/dialog-theme.css` to modify:
- Colors (light and dark mode)
- Typography
- Spacing
- Component styles

### Content
All documentation content is in `src/content/docs/`:
- Markdown files with frontmatter
- Organized by category folders
- Supports MDX for interactive components

## Base Project Structure

```
astro-dialog/
├── public/              # Static assets
├── src/
│   ├── assets/         # Images processed by Astro
│   ├── content/
│   │   └── docs/       # Documentation markdown files
│   └── styles/
│       └── dialog-theme.css  # Custom theme
├── astro.config.mjs    # Astro configuration
├── package.json        # Dependencies and scripts
├── tsconfig.json       # TypeScript configuration
└── wrangler.toml       # Cloudflare Pages configuration
```

## Resources

- [Astro Documentation](https://docs.astro.build)
- [Cloudflare Billing Information](https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/)
- [swiftDialog GitHub](https://github.com/swiftDialog/swiftDialog)

## License

MIT License

Note: This documentation conten is part of the swiftDialog project.