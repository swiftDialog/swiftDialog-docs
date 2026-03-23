import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  output: 'static', // Required for Cloudflare Pages
  site: 'https://dialog-docs.pages.dev', // Cloudflare Pages URL
  integrations: [
    starlight({
      title: 'swiftDialog',
      description: 'A modern macOS dialog utility for administrators',
      logo: {
        src: './src/assets/dialog_logo.png',
        replacesTitle: false,
      },
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/swiftDialog/swiftDialog',
        },
      ],
      editLink: {
        baseUrl: 'https://github.com/swiftDialog/swiftDialog/wiki/',
      },
      sidebar: [
        {
          label: 'Getting Started',
          items: [
            { label: 'Introduction', slug: 'getting-started/introduction' },
            { label: 'Installation', slug: 'getting-started/installation' },
            { label: 'Requirements', slug: 'getting-started/requirements' },
          ],
        },
        {
          label: 'Basic Use',
          collapsed: false,
          items: [
            { label: 'Title', slug: 'basic-use/title' },
            { label: 'Message', slug: 'basic-use/message' },
            { label: 'Images', slug: 'basic-use/images' },
            { label: 'Video', slug: 'basic-use/video' },
            { label: 'Web Content', slug: 'basic-use/web-content' },
            { label: 'Icon', slug: 'basic-use/icon' },
            { label: 'Buttons', slug: 'basic-use/buttons' },
            { label: 'Markdown', slug: 'basic-use/markdown' },
          ],
        },
        {
          label: 'Advanced Features',
          collapsed: true,
          items: [
            { label: 'Command Line Options', slug: 'advanced/command-line-options' },
            { label: 'JSON Configuration', slug: 'advanced/json-configuration' },
            { label: 'Command File Updates', slug: 'advanced/command-file' },
            { label: 'Checkboxes', slug: 'advanced/checkboxes' },
            { label: 'Text Fields', slug: 'advanced/textfields' },
            { label: 'Select Lists', slug: 'advanced/select-lists' },
            { label: 'Item Lists', slug: 'advanced/item-lists' },
            { label: 'Timer and Progress Bar', slug: 'advanced/timer-progress' },
            { label: 'Info Box', slug: 'advanced/info-box' },
            { label: 'Banner Images', slug: 'advanced/banner-images' },
            { label: 'Background Images', slug: 'advanced/background-images' },
            { label: 'Full Screen', slug: 'advanced/full-screen' },
            { label: 'Window Size', slug: 'advanced/window-size' },
            { label: 'Layout', slug: 'advanced/layout' },
            { label: 'Presentation Mode', slug: 'advanced/presentation' },
            { label: 'Notifications', slug: 'advanced/notifications' },
            { label: 'Cards', slug: 'advanced/cards' },
            { label: 'Inspect Mode',
              collapsed: true,
              items: [
                { label: 'Overview', slug: 'advanced/inspect-mode' },
                { label: 'Presets',
                  collapsed: true,
                  items: [
                    { label: 'Deployment', slug: 'advanced/inspect/preset1' },
                    { label: 'Cards', slug: 'advanced/inspect/preset2' },
                    { label: 'Compact List', slug: 'advanced/inspect/preset3' },
                    { label: 'Toast', slug: 'advanced/inspect/preset4' },
                    { label: 'Unified', slug: 'advanced/inspect/preset5' },
                    { label: 'Guidance', slug: 'advanced/inspect/preset6' },
                  //  { label: 'Preset 7', slug: 'advanced/inspect/preset7' },
                  //  { label: 'Preset 8', slug: 'advanced/inspect/preset8' },
                  //  { label: 'Preset 9', slug: 'advanced/inspect/preset9' }
                  ]
                }
              ]
            }
          ],
        },
        {
          label: 'Operation',
          collapsed: true,
          items: [
            { label: 'Exit Codes', slug: 'operation/exit-codes' },
            { label: 'Capturing Output', slug: 'operation/capturing-output' },
            { label: 'Login Window', slug: 'operation/login-window' },
            { label: 'Authorization', slug: 'operation/authorization' },
            { label: 'Preferences', slug: 'operation/preferences' },
            { label: 'Command-Q Behavior', slug: 'operation/command-q' },
            { label: 'Built-in Variables', slug: 'operation/builtin-variables' },
            { label: 'Help Message', slug: 'operation/help-message' },
            { label: 'Gotchas', slug: 'operation/gotchas' },
          ],
        },
        {
          label: 'Examples & Scripts',
          collapsed: true,
          items: [
            { label: 'Showcase', slug: 'examples/showcase' },
            { label: 'Demo Scripts', slug: 'examples/demo-scripts' },
            { label: 'Jamf Scripts', slug: 'examples/jamf-scripts' },
            { label: 'Nudge Style Update', slug: 'examples/nudge-update' },
            { label: 'jamfHelper Support', slug: 'examples/jamfhelper' },
            { label: 'Shell Commands', slug: 'examples/shell-commands' },
          ],
        },
        {
          label: 'Reference',
          collapsed: true,
          items: [
            { label: 'Release Notes',
              collapsed: true,
              items: [
                { label: '3.0.0', slug: 'reference/releasenotes/sd3-0-0' },
                { label: '3.0.1', slug: 'reference/releasenotes/sd3-0-1' },
                { label: '3.1.0', slug: 'reference/releasenotes/sd3-1-0' }
              ]
            },
            { label: 'Updates', slug: 'reference/updates' },
            { label: 'Builder', slug: 'builder/builder' },
          ],
        },
      ],
      customCss: [
        './src/styles/dialog-theme.css',
      ],
      head: [
        {
          tag: 'link',
          attrs: {
            rel: 'icon',
            href: '/favicon.png',
            type: 'image/png',
          },
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:image',
            content: '/dialog_logo.png',
          },
        },
      ],
      favicon: '/favicon.png',
      lastUpdated: true,
      pagination: true,
    }),
  ],
  // site: 'https://swiftdialog.github.io',
  // base: '/swiftDialog/',
});