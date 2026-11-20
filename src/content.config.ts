import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { docsLoader, i18nLoader } from '@astrojs/starlight/loaders';
import { docsSchema, i18nSchema } from '@astrojs/starlight/schema';

export const collections = {
  docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),
  // UI strings: src/content/i18n/<lang>.json. Starlight's built-in strings can be
  // overridden here too; the keys below are custom strings used by our components.
  i18n: defineCollection({
    loader: i18nLoader(),
    schema: i18nSchema({
      extend: z.object({
        'download.latest': z.string().optional(),
        'download.dmg': z.string().optional(),
        'download.pkg': z.string().optional(),
        'download.dmgGithub': z.string().optional(),
        'download.releaseNotes': z.string().optional(),
      }),
    }),
  }),
};
