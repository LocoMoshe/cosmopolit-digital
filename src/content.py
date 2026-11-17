# -*- coding: utf-8 -*-
"""Homepage copy, both languages. Edit text here, then run: python3 src/build.py

In headings, <em>…</em> marks the words set in the italic serif accent.
"""

IMG = {
    'dzemat': 'dzemat', 'stomatolog': 'stomatolog', 'gentlebond': 'gentlebond', 'airadio': 'airadio',
}

BS = dict(
    lang='bs', path='/',
    title='Izrada web stranica i video za biznis, Sarajevo | Cosmopolit Digital',
    description='Web stranice koje poslije sami uređujete i kratki video za vaš biznis. Sarajevo, za klijente u BiH i dijaspori. Radovi, cijene i kontakt.',
    skip='Preskoči na sadržaj', menu='Meni', navLabel='Glavni meni',
    nav=[('#radovi', 'Radovi'), ('#usluge', 'Usluge'), ('#rjesenja', 'Rješenja'), ('#o-meni', 'O meni'), ('#kontakt', 'Kontakt')],
    cta='Pošaljite upit',

    h1='Web stranice i video <em>za biznise i organizacije.</em>',
    lead='Iz Sarajeva, za klijente u BiH i dijaspori. Pravim stranice koje poslije sami uređujete i kratke video priče koje pokazuju šta radite.',
    heroBtn='Pogledajte radove', heroWa='WhatsApp',
    recentLabel='Nedavno',

    workTitle='Radovi',
    workLead='Četiri projekta iz posljednjih mjeseci. Sve su prave stranice koje ljudi svaki dan koriste.',
    cases=[
        dict(img='dzemat', domain='dzematizetnanic.com', name='Džemat Izet Nanić', place='Dornbirn, Austrija',
             text='Džemat je plaćao platformu svake godine, a objavljivati je znala samo jedna osoba. Sad odbor sam objavljuje obavještenja, hutbe i vaktiju, a članstvo ide preko stranice.',
             url='https://dzematizetnanic.com', urlLabel='Otvorite stranicu', more='/dzemati/', moreLabel='Stranice za džemate',
             altD='Početna stranica Džemata Izet Nanić na računaru', altM='Stranica Džemata Izet Nanić na mobitelu'),
        dict(img='stomatolog', domain='stomatolog.ba', name='Dr. Ganibegović', place='Sarajevo',
             text='Nova stranica ortodontske ordinacije. Pacijent kroz interaktivne vodiče vidi kako aparatić radi i koji problem sa zagrizom ima, a ordinaciju zove jednim dodirom.',
             url='https://stomatolog-ganibegovic.loco-moshe.workers.dev', urlLabel='Otvorite stranicu', more='/ordinacije/', moreLabel='Stranice za ordinacije',
             altD='Stranica ordinacije Dr. Ganibegović na računaru', altM='Stranica ordinacije Dr. Ganibegović na mobitelu'),
        dict(img='gentlebond', domain='gentlebond', name='GentleBond', place='Web aplikacija',
             text='Aplikacija koja pomaže porodicama da starijim članovima pronađu društvo u blizini, za kafu, šetnju i razgovor. Na projektu radim s timom.',
             url='https://kindred-connect-elders.vercel.app', urlLabel='Otvorite aplikaciju', more='', moreLabel='',
             altD='GentleBond na računaru', altM='GentleBond na mobitelu'),
        dict(img='airadio', domain='airadio.ba', name='AI Radio Sarajevo', place='Online radio',
             text='Gradski radio s četiri stanice. Svaka ima svoj izgled, od sevdaha do rocka, uz plejer uživo i AI chat za slušaoce.',
             url='https://airadio.ba', urlLabel='Poslušajte radio', more='', moreLabel='',
             altD='AI Radio Sarajevo na računaru', altM='AI Radio Sarajevo na mobitelu'),
    ],

    servicesTitle='Usluge i <em>cijene</em>',
    servicesLead='Početne cijene. Tačan iznos dogovaramo nakon kratkog razgovora.',
    webTitle='Web stranice',
    webText='Brze stranice koje dobro izgledaju na mobitelu, na jednom ili dva jezika. Nakon predaje sadržaj mijenjate sami.',
    webPrices=[
        ('Web stranica', 'Prezentacija vašeg posla na nekoliko stranica', 'od 1.200 KM'),
        ('Proširena web stranica', 'Više podstranica i interaktivni sadržaj', 'od 2.000 KM'),
        ('Stranica s admin sistemom', 'Članstvo, prijave, obavještenja i mailovi', 'od 6.000 KM'),
        ('Kasnije izmjene', 'Samo kad ih zatražite', '40 KM / sat'),
    ],
    webTerms='1/3 unaprijed, ostatak prije predaje · gotovo za 1–2 sedmice · 12 mjeseci garancije · bez mjesečnih troškova',
    videoTitle='Video',
    videoText='Reelsi, kratke reklame i mjesečni sadržaj za Instagram i Facebook. Snimam na lokaciji u Sarajevu, montiram i isporučujem gotovo za objavu.',
    videoPrices=[
        ('Montaža vaših snimaka', '1 reel do 30 s, iz vašeg materijala', 'od 100 KM'),
        ('Jedan reel', '15–30 s, do 1 sat snimanja', 'od 200 KM'),
        ('Tri reelsa', 'Jedan dolazak, do 2 sata snimanja', 'od 450 KM'),
        ('Kratka reklama', '30–60 s, s pozivom na akciju', 'od 450 KM'),
        ('Restoran u fokusu', 'Promo video i 2 reelsa', 'od 650 KM'),
        ('Mjesečni start', '4 reelsa mjesečno, jedan svake sedmice', 'od 500 KM / mj.'),
        ('Mjesečni sadržaj', '6 reelsa mjesečno i plan objava', 'od 800 KM / mj.'),
    ],
    videoIncl='U svakom paketu: dogovor o sadržaju, montaža, boja i zvuk, natpisi i logo, licencirana muzika, jedan krug korekcija.',
    videoExtra='Dodatno: novi reel iz istog materijala 80 KM, dodatna montaža 40 KM/sat, animacije od 30 KM.',
    stepsTitle='Kako snimamo',
    steps=[('Dogovor', 'Cilj, ideja i plan kadrova.'), ('Snimanje', 'Jedan dogovoreni termin.'), ('Isporuka', 'Prva verzija za 5–7 radnih dana.')],
    gearTitle='Oprema',
    gear=[('gear-c100', 'Canon C100 II', 'Cinema kamera za snimanje na lokaciji.'), ('gear-mini5', 'DJI Mini 5 Pro', '4K snimci iz zraka, po posebnoj ponudi.')],

    solTitle='Za posebne <em>branše</em>',
    solLead='Za ove dvije branše imam gotova rješenja i primjere.',
    solutions=[
        ('/ordinacije/', 'Stomatološke ordinacije', 'Web stranica i video za Instagram, za ordinacije u Sarajevu i BiH.'),
        ('/dzemati/', 'Džemati i islamske zajednice', 'Stranica s adminom koju odbor vodi sam, bez godišnje pretplate.'),
    ],

    aboutTitle='Zašto Cosmopolit?',
    aboutParas=['Rođen sam u Africi. Poslije sam živio i radio u Aziji, na Bliskom istoku i u Evropi, pa se taj naziv nekako sam nametnuo.',
                'Kroz sve to sam shvatio da ljudi rijetko tačno znaju šta im treba. Znaju da im nešto fali ili da nešto ne radi kako treba, ali to teško opišu. Zato na početku više pitam nego što pričam.',
                'Zanima me puno toga, od historije i nauke do tipografije i toga kako se ljudi snalaze kad otvore neku stranicu. Sve mi to pomaže da napravim nešto što je lako koristiti, a da pritom lijepo izgleda.'],
    aboutSign='Haris Hadrović', aboutRole='osnivač, Cosmopolit Digital', aboutAlt='Haris Hadrović, osnivač Cosmopolit Digitala',

    contactTitle='Javite se.',
    contactText='Pošaljite mi vrstu posla, lokaciju i šta vam treba. Odgovaram isti dan.',
    instagram='Instagram',
)

EN = dict(
    lang='en', path='/en/',
    title='Websites and video for businesses, Sarajevo | Cosmopolit Digital',
    description='Websites you can update yourself and short video for your business. Based in Sarajevo, working with clients in Bosnia and abroad. Work, prices and contact.',
    skip='Skip to content', menu='Menu', navLabel='Main menu',
    nav=[('#radovi', 'Work'), ('#usluge', 'Services'), ('#rjesenja', 'Solutions'), ('#o-meni', 'About'), ('#kontakt', 'Contact')],
    cta='Get in touch',

    h1='Websites and video <em>for businesses and organisations.</em>',
    lead='Based in Sarajevo, working with clients in Bosnia and abroad. I build websites you can update yourself and short video stories that show what you do.',
    heroBtn='See the work', heroWa='WhatsApp',
    recentLabel='Recent',

    workTitle='Work',
    workLead='Four projects from recent months. All of them are real sites people use every day.',
    cases=[
        dict(img='dzemat', domain='dzematizetnanic.com', name='Džemat Izet Nanić', place='Dornbirn, Austria',
             text='The mosque was paying a platform every year, and only one person knew how to post. Now the committee publishes announcements, khutbahs and prayer times itself, and membership runs through the site.',
             url='https://dzematizetnanic.com', urlLabel='Open the site', more='/en/dzemati/', moreLabel='Websites for mosques',
             altD='Džemat Izet Nanić homepage on a computer', altM='Džemat Izet Nanić site on a phone'),
        dict(img='stomatolog', domain='stomatolog.ba', name='Dr. Ganibegović', place='Sarajevo',
             text='A new site for an orthodontic clinic. Interactive guides show patients how braces work and which bite problem they have, and they can call the clinic with one tap.',
             url='https://stomatolog-ganibegovic.loco-moshe.workers.dev', urlLabel='Open the site', more='/en/ordinacije/', moreLabel='Websites for clinics',
             altD='Dr. Ganibegović clinic site on a computer', altM='Dr. Ganibegović clinic site on a phone'),
        dict(img='gentlebond', domain='gentlebond', name='GentleBond', place='Web app',
             text='An app that helps families find nearby company for their older loved ones, for coffee, walks and conversation. I work on it with a team.',
             url='https://kindred-connect-elders.vercel.app', urlLabel='Open the app', more='', moreLabel='',
             altD='GentleBond on a computer', altM='GentleBond on a phone'),
        dict(img='airadio', domain='airadio.ba', name='AI Radio Sarajevo', place='Online radio',
             text='A city radio with four stations. Each has its own look, from sevdah to rock, with a live player and an AI chat for listeners.',
             url='https://airadio.ba', urlLabel='Listen live', more='', moreLabel='',
             altD='AI Radio Sarajevo on a computer', altM='AI Radio Sarajevo on a phone'),
    ],

    servicesTitle='Services and <em>prices</em>',
    servicesLead='Starting prices. We agree the exact amount after a short call.',
    webTitle='Websites',
    webText='Fast sites that look good on a phone, in one or two languages. After handover you change the content yourself.',
    webPrices=[
        ('Website', 'Your business presented across a few pages', 'from €600'),
        ('Extended website', 'More pages and interactive content', 'from €1,000'),
        ('Website with admin system', 'Membership, applications, announcements and email', 'from €3,000'),
        ('Later changes', 'Only when you ask for them', '€20 / hour'),
    ],
    webTerms='1/3 upfront, the rest before handover · ready in 1–2 weeks · 12-month guarantee · no monthly fees',
    videoTitle='Video',
    videoText='Reels, short ads and monthly content for Instagram and Facebook. I film on location in Sarajevo, edit, and deliver ready to post.',
    videoPrices=[
        ('Editing your footage', '1 reel up to 30 s, from your material', 'from 100 KM'),
        ('One reel', '15–30 s, up to 1 hour of filming', 'from 200 KM'),
        ('Three reels', 'One visit, up to 2 hours of filming', 'from 450 KM'),
        ('Short ad', '30–60 s, with a call to action', 'from 450 KM'),
        ('Restaurant spotlight', 'Promo video and 2 reels', 'from 650 KM'),
        ('Monthly starter', '4 reels a month, one a week', 'from 500 KM / mo'),
        ('Monthly content', '6 reels a month and a posting plan', 'from 800 KM / mo'),
    ],
    videoIncl='Every package includes: content planning, editing, colour and sound, captions and logo, licensed music, one round of revisions.',
    videoExtra='Extras: a new reel from the same footage 80 KM, extra editing 40 KM/hour, animation from 30 KM.',
    stepsTitle='How filming works',
    steps=[('Planning', 'Goal, idea and shot list.'), ('Filming', 'One agreed session.'), ('Delivery', 'First version in 5–7 working days.')],
    gearTitle='Equipment',
    gear=[('gear-c100', 'Canon C100 II', 'Cinema camera for on-location shoots.'), ('gear-mini5', 'DJI Mini 5 Pro', '4K aerial footage, quoted separately.')],

    solTitle='For specific <em>sectors</em>',
    solLead='For these two sectors I have ready-made solutions and examples.',
    solutions=[
        ('/en/ordinacije/', 'Dental clinics', 'A website and Instagram video for clinics in Sarajevo and Bosnia.'),
        ('/en/dzemati/', 'Mosques and Islamic communities', 'A website with an admin the committee runs itself, with no yearly subscription.'),
    ],

    aboutTitle='Why Cosmopolit?',
    aboutParas=['I was born in Africa. Later I lived and worked in Asia, the Middle East and Europe, so the name more or less chose itself.',
                'Along the way I noticed that people rarely know exactly what they need. They know something is missing or not working, but it is hard to put into words. So at the start I ask more than I talk.',
                'I am interested in a lot of things, from history and science to typography and how people find their way around a web page. All of it helps me make something that is easy to use and looks good too.'],
    aboutSign='Haris Hadrović', aboutRole='founder, Cosmopolit Digital', aboutAlt='Haris Hadrović, founder of Cosmopolit Digital',

    contactTitle='Get in touch.',
    contactText='Send me what you do, where you are and what you need. I reply the same day.',
    instagram='Instagram',
)
