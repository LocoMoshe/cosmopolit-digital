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
import content_dzemati
import content_ordinacije

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"

SETTINGS = dict(
    site_url="https://cosmopolitdigital.com",
    phone="062 897 216",
    phone_intl="38762897216",
    email="info@cosmopolitdigital.com",  # forwards to cosmopolit.digital@gmail.com (Cloudflare Email Routing)
    year=datetime.date.today().year,
)

ICON = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">{}</svg>'
SNIPPETS = dict(
    arrow='<svg width="18" height="18" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="#E56821" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    arrow_sm='<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    arrow_check='<svg width="18" height="18" viewBox="0 0 22 22" fill="none" aria-hidden="true"><circle cx="11" cy="11" r="11" fill="#E56821"/><path d="M6.5 11.2l3 3 6-6.4" stroke="#0A0A22" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    ig_icon=ICON.format('<rect x="3" y="3" width="18" height="18" rx="5" stroke="#E56821" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#E56821" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.2" fill="#E56821"/>'),
    viber_icon=ICON.format('<path d="M12 3c5 0 8.5 2.6 8.5 7.6S17 18 12 18c-.8 0-1.6-.1-2.3-.2L6 20.5v-3.6C4.3 15.5 3.5 13.3 3.5 10.6 3.5 5.6 7 3 12 3z" stroke="#E56821" stroke-width="2" stroke-linejoin="round"/><path d="M9.5 8.2c.3 1.9 1.9 3.6 4 4.2" stroke="#E56821" stroke-width="2" stroke-linecap="round"/>'),
    mail_icon=ICON.format('<rect x="3" y="5" width="18" height="14" rx="2" stroke="#E56821" stroke-width="2"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5" stroke="#E56821" stroke-width="2" stroke-linejoin="round"/>'),
)


def main():
    env = Environment(loader=FileSystemLoader(ROOT / "src"), autoescape=True,
                      undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)

    def out_path(path):
        return PUBLIC / path.strip("/") / "index.html" if path != "/" else PUBLIC / "index.html"

    def root_for(path):
        return "../" * path.strip("/").count("/") + ("../" if path != "/" else "")

    hl = lambda bs, en: [("bs", bs), ("en", en), ("x-default", bs)]
    jobs = []
    # homepage
    for t, alt in [(content.BS, "/en/"), (content.EN, "/")]:
        jobs.append(("page.html.j2", t, dict(
            nav=t["nav"], alt_href=alt, hreflangs=hl("/", "/en/"), og_image="/assets/img/og.jpg",
            contact_title=t["contactTitle"], contact_text=t["contactText"], wa_text="",
            footer_links=[(("/en/" if t["lang"] == "en" else "/") + "ordinacije/", "Ordinacije" if t["lang"] == "bs" else "Dental clinics"),
                          (("/en/" if t["lang"] == "en" else "/") + "dzemati/", "Džemati" if t["lang"] == "bs" else "Mosques")])))
    # džemati
    for t, alt in [(content_dzemati.BS, "/en/dzemati/"), (content_dzemati.EN, "/dzemati/")]:
        home = "/en/" if t["lang"] == "en" else "/"
        jobs.append(("dzemati.html.j2", t, dict(
            nav=[(home, t["navHome"]), ("#funkcije", t["navFeatures"]), ("#cijena", t["navPrice"]), ("#kontakt", t["navContact"])],
            alt_href=alt, hreflangs=hl("/dzemati/", "/en/dzemati/"), og_image="/assets/img/dz/og-dzemati.jpg",
            contact_title=t["contactTitle"], contact_text=t["contactText"], wa_text=t["waText"],
            footer_links=[(home, t["footerBack"].replace("← ", ""))])))
    # ordinacije
    for t, alt in [(content_ordinacije.BS, "/en/ordinacije/"), (content_ordinacije.EN, "/ordinacije/")]:
        home = "/en/" if t["lang"] == "en" else "/"
        jobs.append(("ordinacije.html.j2", t, dict(
            nav=[(home, t["navHome"]), ("#stranica", t["navFeatures"]), ("#video", t["navVideo"]), ("#cijene", t["navPrice"]), ("#kontakt", t["navContact"])],
            alt_href=alt, hreflangs=hl("/ordinacije/", "/en/ordinacije/"), og_image="/assets/img/og.jpg",
            contact_title=t["contactTitle"], contact_text=t["contactText"], wa_text=t["waText"],
            footer_links=[(home, t["navHome"])])))

    for tpl_name, t, extra in jobs:
        out = out_path(t["path"])
        root = root_for(t["path"])
        home = "/en/" if t["lang"] == "en" else "/"
        out.parent.mkdir(parents=True, exist_ok=True)
        html = env.get_template(tpl_name).render(t=t, root=root, home=home, **extra, **SETTINGS, **SNIPPETS)
        out.write_text(html, encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
