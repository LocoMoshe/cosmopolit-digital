#!/usr/bin/env python3
"""Builds public/index.html (Bosnian) and public/en/index.html (English).

Usage:  python3 src/build.py
Needs:  pip install jinja2
Copy lives in src/content.py; layout in src/page.html.j2; styles in public/assets/css/site.css.
"""
import datetime
import pathlib

from jinja2 import Environment, FileSystemLoader, StrictUndefined

import content

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"

SETTINGS = dict(
    site_url="https://cosmopolitdigital.com",
    phone="062 897 216",
    phone_intl="38762897216",
    email="cosmopolit.digital@gmail.com",  # switch to info@<domain> once the domain exists
    year=datetime.date.today().year,
)

ICON = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">{}</svg>'
SNIPPETS = dict(
    arrow='<svg width="18" height="18" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="#E56821" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    arrow_sm='<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    ig_icon=ICON.format('<rect x="3" y="3" width="18" height="18" rx="5" stroke="#E56821" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#E56821" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.2" fill="#E56821"/>'),
    viber_icon=ICON.format('<path d="M12 3c5 0 8.5 2.6 8.5 7.6S17 18 12 18c-.8 0-1.6-.1-2.3-.2L6 20.5v-3.6C4.3 15.5 3.5 13.3 3.5 10.6 3.5 5.6 7 3 12 3z" stroke="#E56821" stroke-width="2" stroke-linejoin="round"/><path d="M9.5 8.2c.3 1.9 1.9 3.6 4 4.2" stroke="#E56821" stroke-width="2" stroke-linecap="round"/>'),
    mail_icon=ICON.format('<rect x="3" y="5" width="18" height="14" rx="2" stroke="#E56821" stroke-width="2"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5" stroke="#E56821" stroke-width="2" stroke-linejoin="round"/>'),
)


def main():
    env = Environment(loader=FileSystemLoader(ROOT / "src"), autoescape=True,
                      undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
    tpl = env.get_template("page.html.j2")
    pages = [(content.BS, content.BS_DATA, PUBLIC / "index.html", ""),
             (content.EN, content.EN_DATA, PUBLIC / "en" / "index.html", "../")]
    for t, d, out, root in pages:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(tpl.render(t=t, d=d, root=root, **SETTINGS, **SNIPPETS), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
