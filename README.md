# Cosmopolit Digital

Website for Cosmopolit Digital: websites and short video for businesses. Bosnian (`/`) and English (`/en/`).

## Structure

```
public/            ← the live site (this is what gets deployed)
  index.html       ← Bosnian, generated
  en/index.html    ← English, generated
  assets/css/site.css
  assets/fonts/    ← Poppins, self-hosted (no Google Fonts, GDPR-friendly)
  assets/img/      ← logo, project screenshots, share image
src/
  content.py       ← ALL page text, both languages. Edit copy here.
  page.html.j2     ← the page layout (shared by both languages)
  build.py         ← generates public/index.html and public/en/index.html
```

## Editing

1. Change text in `src/content.py` (or layout in `src/page.html.j2`, styles in `public/assets/css/site.css`).
2. Run `pip install jinja2` (once), then `python3 src/build.py`.
3. Commit and push. Both language versions update together.

Phone, email and the site's domain are set at the top of `src/build.py`.

## Still to fill in

- Website prices: `[CIJENA]` / `[PRICE]` in `src/content.py`
- Email: `email=None` in `src/build.py` (the button appears once it's set)
- Domain: `site_url` in `src/build.py` (used for share previews and search engines)

## Deploy (Cloudflare Pages)

Connect this repo in Cloudflare → Workers & Pages → Create → Pages → Connect to Git.

- Build command: *(leave empty)*
- Build output directory: `public`
