# -*- coding: utf-8 -*-
"""Copy for /ordinacije/ (dental clinics), both languages."""

BS = dict(
    lang='bs', path='/ordinacije/',
    title='Web stranica i video za stomatološke ordinacije, Sarajevo | Cosmopolit Digital',
    description='Web stranica za stomatološku ordinaciju i kratki video za Instagram. Primjer: ordinacija Dr. Ganibegović, Sarajevo. Web od 2.000 KM, video od 450 KM.',
    skip='Preskoči na sadržaj', menu='Meni', navLabel='Glavni meni',
    navHome='Početna', navFeatures='Stranica', navVideo='Video', navPrice='Cijene', navContact='Kontakt',
    cta='Pošaljite upit',

    kicker='ZA STOMATOLOŠKE ORDINACIJE',
    problemEyebrow='ŠTA PACIJENT TRAŽI', featEyebrow='WEB STRANICA', videoEyebrow='VIDEO ZA INSTAGRAM', priceEyebrow='CIJENE', stepsEyebrow='KAKO IDE', contactEyebrow='KONTAKT', footerBack='← Nazad na početnu',
    h1='Web stranica i video za vašu ordinaciju.',
    lead='Pacijenti danas prvo pogledaju stranicu i Instagram, pa tek onda zovu. Napravim vam stranicu koja jasno objašnjava šta radite i snimim kratke video priče iz vaše ordinacije.',
    heroCta2='Pogledajte primjer',
    heroNote='Primjer: ordinacija Dr. Ganibegović, Sarajevo',
    altD='Stranica ordinacije Dr. Ganibegović na računaru', altM='Stranica ordinacije Dr. Ganibegović na mobitelu',

    problemTitle='Šta pacijent želi znati prije nego nazove',
    problems=[
        ('Da li radite ono što mu treba', 'Jasan pregled usluga, od preventive i protetike do ortodoncije i izbjeljivanja.'),
        ('Ko će ga liječiti', 'Tim s imenima i slikama. Ljudi lakše dođu kad znaju kome idu.'),
        ('Da li je sad otvoreno', 'Radno vrijeme koje samo pokazuje da li je otvoreno ili kad otvarate.'),
        ('Kako da vas dobije', 'Poziv jednim dodirom, adresa na mapi i Google recenzije na jednom mjestu.'),
    ],

    featTitle='Stranica koja objašnjava, ne samo nabraja',
    featLead='Ekrani sa stranice ordinacije Dr. Ganibegović, onako kako ih pacijent vidi na mobitelu.',
    blocks=[
        dict(num='USLUGE', t='Pacijent odmah vidi šta radite',
             s='Početna jasno kaže ko ste i gdje ste, s dugmetom za poziv na vrhu. Usluge su podijeljene tako da roditelj brzo nađe dio za djecu, a odrasli protetiku ili izbjeljivanje.',
             imgs=[('home', 'Početna stranica ordinacije na mobitelu'), ('usluge', 'Pregled usluga ordinacije na mobitelu')]),
        dict(num='VODIČI', t='Interaktivni vodiči umjesto dugog teksta',
             s='Pacijent kroz modele zuba sam bira vrstu zagriza i vidi razliku. Korak po korak saznaje kako fiksni aparatić radi i koliko terapija traje. Manje ponavljanja istih pitanja u ordinaciji.',
             imgs=[('zagriz', 'Interaktivni vodič kroz probleme sa zagrizom'), ('aparatic', 'Vodič kroz fazu terapije fiksnim aparatićem')]),
    ],
    moreTitle='I još:',
    more=[
        ('Radno vrijeme uživo', 'Stranica sama pokazuje „otvoreno“ ili kad otvarate.'),
        ('Poziv jednim dodirom', 'Broj je uvijek pri ruci, na vrhu i na dnu svake stranice.'),
        ('Tim', 'Doktori i sestre sa slikom i kratkim opisom.'),
        ('Česta pitanja', 'Cijene, bol, trajanje terapije, djeca. Odgovori prije poziva.'),
        ('Google recenzije i mapa', 'Povjerenje i put do vas, bez traženja.'),
        ('Brzo učitavanje', 'Stranica radi i na slabijem mobilnom internetu.'),
    ],

    videoTitle='Video za Instagram',
    videoLead='Kratki snimci koji pokažu prostor, opremu i ljude. Snimam u ordinaciji u dogovorenom terminu, montiram i predam gotovo za objavu.',
    videoIdeas=[
        ('Upoznajte ordinaciju', 'Prostor, oprema i tim u 30 sekundi.'),
        ('Edukativni reelsi', 'Doktor objašnjava jedno pitanje: aparatić, izbjeljivanje, prvi pregled djeteta.'),
        ('Prije i poslije', 'Samo uz pisanu saglasnost pacijenta.'),
    ],

    priceTitle='Cijene',
    priceLead='Početne cijene. Tačan iznos dogovaramo nakon kratkog razgovora i obilaska ordinacije.',
    webPrices=[
        ('Web stranica za ordinaciju', 'Usluge, tim, radno vrijeme, kontakt, na jednom ili dva jezika', 'od 2.000 KM'),
        ('Interaktivni vodiči', 'Zagriz, aparatić ili druga terapija, po dogovoru', 'po ponudi'),
        ('Kasnije izmjene', 'Samo kad ih zatražite', '40 KM / sat'),
    ],
    videoPrices=[
        ('Tri reelsa', 'Jedan dolazak, do 2 sata snimanja', 'od 450 KM'),
        ('Kratka reklama', '30–60 s, s pozivom na akciju', 'od 450 KM'),
        ('Mjesečni start', '4 reelsa mjesečno, jedan svake sedmice', 'od 500 KM / mj.'),
    ],
    priceWeb='Web stranica', priceVideo='Video',
    terms=[
        ('Ključ u ruke', 'Pišem tekstove, vi ih odobrite. Stranicu predam gotovu, s pristupom za izmjene.'),
        ('Bez mjesečnih troškova', 'Plaćate samo domenu, oko 30 KM godišnje. Garancija 12 mjeseci.'),
        ('Plaćanje', '1/3 unaprijed, ostatak prije prebacivanja na vašu domenu.'),
        ('Rok', 'Stranica za 1–2 sedmice od dobijenih tekstova i slika.'),
    ],

    stepsTitle='Kako ide',
    steps=[
        dict(t='Razgovor', s='Kratak sastanak u ordinaciji ili telefonom.'),
        dict(t='Prijedlog', s='Struktura stranice i tačna ponuda.'),
        dict(t='Izrada', s='Vidite stranicu dok nastaje i tražite izmjene.'),
        dict(t='Predaja', s='Stranica ide na vašu domenu, pokažem vam kako se mijenja sadržaj.'),
    ],
    faqTitle='Česta pitanja',
    faq=[
        dict(q='Imamo staru stranicu. Možete li zadržati tekstove?', a='Mogu. Prebacim postojeće tekstove riječ po riječ, a vi odlučite šta mijenjamo.'),
        dict(q='Nemamo vremena pisati tekstove.', a='Ne morate. Ja napišem prijedlog na osnovu razgovora, vi samo pročitate i odobrite.'),
        dict(q='Da li treba forma za zakazivanje?', a='Nije obavezno. Većina pacijenata radije nazove ili pošalje poruku, pa je dugme za poziv na svakoj stranici.'),
        dict(q='Moramo li objaviti cijene?', a='Ne. Cijene mogu biti na stranici ili samo okvirno, kako vama odgovara.'),
        dict(q='Smijemo li objavljivati slike pacijenata?', a='Samo uz pisanu saglasnost pacijenta. Za video najčešće snimamo prostor, opremu i tim, bez pacijenata.'),
    ],

    contactTitle='Pogledajmo vašu ordinaciju.',
    contactText='Javite se porukom ili pozivom. Dođem, pogledam prostor i staru stranicu, pa vam pošaljem prijedlog.',
    waText='Pozdrav, zanima me web stranica / video za ordinaciju.',
)

EN = dict(
    lang='en', path='/en/ordinacije/',
    title='Websites and video for dental clinics, Sarajevo | Cosmopolit Digital',
    description='A website for your dental clinic and short Instagram video. Example: Dr. Ganibegović clinic, Sarajevo. Website from €1,000, video from 450 KM.',
    skip='Skip to content', menu='Menu', navLabel='Main menu',
    navHome='Home', navFeatures='Website', navVideo='Video', navPrice='Prices', navContact='Contact',
    cta='Get in touch',

    kicker='FOR DENTAL CLINICS',
    problemEyebrow='WHAT PATIENTS LOOK FOR', featEyebrow='WEBSITE', videoEyebrow='INSTAGRAM VIDEO', priceEyebrow='PRICES', stepsEyebrow='HOW IT WORKS', contactEyebrow='CONTACT', footerBack='← Back to homepage',
    h1='A website and video for your clinic.',
    lead='Patients look at the website and Instagram first, and only then call. I build a site that clearly explains what you do and film short video stories in your clinic.',
    heroCta2='See the example',
    heroNote='Example: Dr. Ganibegović clinic, Sarajevo',
    altD='Dr. Ganibegović clinic site on a computer', altM='Dr. Ganibegović clinic site on a phone',

    problemTitle='What a patient wants to know before calling',
    problems=[
        ('Do you do what they need', 'A clear overview of services, from prevention and prosthetics to orthodontics and whitening.'),
        ('Who will treat them', 'The team with names and photos. People come more easily when they know who they are seeing.'),
        ('Are you open right now', 'Opening hours that show by themselves whether you are open or when you open.'),
        ('How to reach you', 'One-tap calling, the address on a map and Google reviews in one place.'),
    ],

    featTitle='A site that explains, not just lists',
    featLead='Screens from the Dr. Ganibegović clinic site, the way a patient sees them on a phone.',
    blocks=[
        dict(num='SERVICES', t='Patients see straight away what you do',
             s='The homepage says who you are and where, with a call button at the top. Services are grouped so a parent quickly finds the children’s section, and adults find prosthetics or whitening.',
             imgs=[('home', 'Clinic homepage on a phone'), ('usluge', 'Clinic services overview on a phone')]),
        dict(num='GUIDES', t='Interactive guides instead of long text',
             s='Using tooth models, patients pick a bite type and see the difference. Step by step they learn how fixed braces work and how long treatment takes. Fewer repeated questions in the chair.',
             imgs=[('zagriz', 'Interactive guide to bite problems'), ('aparatic', 'Guide to the stages of fixed braces treatment')]),
    ],
    moreTitle='And also:',
    more=[
        ('Live opening hours', 'The site shows “open” or when you open next.'),
        ('One-tap calling', 'The number is always at hand, top and bottom of every page.'),
        ('Team', 'Doctors and nurses with a photo and a short bio.'),
        ('FAQ', 'Prices, pain, treatment length, children. Answers before the call.'),
        ('Google reviews and map', 'Trust and directions, without searching.'),
        ('Fast loading', 'Works on weaker mobile connections too.'),
    ],

    videoTitle='Video for Instagram',
    videoLead='Short clips that show the space, the equipment and the people. I film in the clinic at an agreed time, edit, and deliver ready to post.',
    videoIdeas=[
        ('Meet the clinic', 'Space, equipment and team in 30 seconds.'),
        ('Educational reels', 'The doctor explains one question: braces, whitening, a child’s first visit.'),
        ('Before and after', 'Only with the patient’s written consent.'),
    ],

    priceTitle='Prices',
    priceLead='Starting prices. We agree the exact amount after a short call and a visit to the clinic.',
    webPrices=[
        ('Clinic website', 'Services, team, hours, contact, in one or two languages', 'from €1,000'),
        ('Interactive guides', 'Bite, braces or another treatment, as agreed', 'quoted'),
        ('Later changes', 'Only when you ask for them', '€20 / hour'),
    ],
    videoPrices=[
        ('Three reels', 'One visit, up to 2 hours of filming', 'from 450 KM'),
        ('Short ad', '30–60 s, with a call to action', 'from 450 KM'),
        ('Monthly starter', '4 reels a month, one a week', 'from 500 KM / mo'),
    ],
    priceWeb='Website', priceVideo='Video',
    terms=[
        ('Turnkey', 'I write the copy, you approve it. You get a finished site with access to make changes.'),
        ('No monthly fees', 'You only pay for the domain, about €15 a year. 12-month guarantee.'),
        ('Payment', '1/3 upfront, the rest before the switch to your domain.'),
        ('Timeline', 'The site in 1–2 weeks after receiving copy and photos.'),
    ],

    stepsTitle='How it works',
    steps=[
        dict(t='Conversation', s='A short meeting at the clinic or by phone.'),
        dict(t='Proposal', s='Site structure and an exact quote.'),
        dict(t='Build', s='You see the site as it takes shape and ask for changes.'),
        dict(t='Handover', s='The site goes live on your domain and I show you how to edit it.'),
    ],
    faqTitle='FAQ',
    faq=[
        dict(q='We have an old site. Can you keep the text?', a='Yes. I move the existing text over word for word, and you decide what changes.'),
        dict(q='We have no time to write copy.', a='You don’t need to. I draft it after our conversation; you just read and approve.'),
        dict(q='Do we need a booking form?', a='Not necessarily. Most patients prefer to call or send a message, so there is a call button on every page.'),
        dict(q='Do we have to publish prices?', a='No. Prices can be on the site, approximate, or left out, as you prefer.'),
        dict(q='Can we post photos of patients?', a='Only with the patient’s written consent. For video we usually film the space, equipment and team, without patients.'),
    ],

    contactTitle='Let’s look at your clinic.',
    contactText='Send a message or call. I come by, look at the space and your current site, and send you a proposal.',
    waText='Hello, I am interested in a website / video for a clinic.',
)
