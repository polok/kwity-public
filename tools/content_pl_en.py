# -*- coding: utf-8 -*-
"""Site texts: Polish and English. Same structure in every content_*.py; the privacy policy lives in tools/privacy/<folder>.html."""

PL = dict(
    folder="pl", html_lang="pl", label="Polski", pick="Strona główna",
    nav_privacy="Prywatność", nav_support="Wsparcie", footer_copy="© 2026 ideaapps.io", footer_langs="Języki",
    index=dict(
        title="Kwity: paragony i gwarancje",
        description="Kwity pilnują końca gwarancji, terminu zwrotu, kaucji, parkingu i numerka. Zrób zdjęcie paragonu, a przypomnimy, zanim będzie za późno.",
        h1="Wszystko, co traci wartość, pod kontrolą",
        lead="Kwity pilnują końca gwarancji, terminu zwrotu, kaucji za butelki, biletu parkingowego i numerka w kolejce. Zrób zdjęcie paragonu, a przypomnimy, zanim będzie za późno.",
        download="Pobierz w App Store", support_btn="Wsparcie", privacy_btn="Polityka prywatności",
        cards=[
            ("Skan paragonu", "Aparat dokumentów albo zdjęcie z galerii. Sklep, kwota i data odczytują się na telefonie."),
            ("Gwarancje i zwroty", "Odliczanie dni, kategorie i lista tego, co kończy się wkrótce."),
            ("Na chwilę", "Kaucje, parkingi i numerki z odliczaniem na żywo. Zostają, dopóki sam ich nie wyczyścisz."),
            ("Kody QR i kreskowe", "Pokaż kod z biletu jednym dotknięciem. Ekran sam się rozjaśnia, a kod jest narysowany ostro."),
            ("Przypomnienia", "Powiadomienie przed końcem terminu, ustawiane osobno dla każdego kwitu."),
            ("Synchronizacja iCloud (Pro)", "Opcjonalnie, jednorazowy zakup: kwity i zdjęcia na wszystkich Twoich urządzeniach, w Twoim prywatnym iCloud."),
            ("Prywatnie", "Bez konta i reklam. Kwity i zdjęcia zostają na Twoim telefonie albo w Twoim iCloud. Blokada Face ID, ciemny i jasny motyw."),
        ],
        note="Po polsku, angielsku, hiszpańsku, włosku, niemiecku, rosyjsku i chińsku. Aplikacja jest darmowa, funkcje Pro są opcjonalne.",
    ),
    support=dict(
        title="Wsparcie | Kwity", description="Pomoc i kontakt w sprawie aplikacji Kwity.",
        h1="Wsparcie", lead="Masz pytanie, pomysł albo znalazłeś błąd w Kwitach? Napisz, odpowiadam na każdą wiadomość.",
        report="Zgłoś pomysł lub błąd", mail="Napisz e-mail", privacy="Polityka prywatności",
        mail_line="E-mail: {mail}. Przy zgłoszeniu błędu podaj proszę wersję aplikacji i wersję iOS.", faq="Najczęstsze pytania",
        qa=[
            ("Jak dodać kwit?", "Na dolnym pasku dotknij „Skanuj kwit”, żeby sfotografować paragon, albo plusa, żeby dodać go ręcznie. Aplikacja odczyta sklep, kwotę i datę, a Ty sprawdzisz formularz i zapiszesz. Nazwa produktu jest zawsze oznaczona „sprawdź”, bo najłatwiej ją przeoczyć."),
            ("Nie mam aparatu albo wolę zdjęcie z galerii", "Na ekranie skanowania jest przycisk „Z galerii”. Zdjęcie możesz też wybrać z biblioteki przy ręcznym dodawaniu kwitu."),
            ("Paragon nie odczytał się dobrze", "Zrób zdjęcie na płasko, przy dobrym świetle, tak żeby tekst był ostry. Rozpoznawanie może się mylić, więc zawsze sprawdź dane przed zapisaniem. Każde pole możesz poprawić ręcznie."),
            ("Czym różni się gwarancja od okna na zwrot?", "Oba mają datę końca i trafiają do kategorii. Gwarancja to zwykle miesiące lub lata, zwrot to kilka lub kilkanaście dni. Po terminie albo po oznaczeniu jako wykorzystany kwit trafia do archiwum w menu „Więcej”."),
            ("Co to jest „Na chwilę” i dlaczego bilet nie znika sam?", "To kaucje, parkingi i numerki z odliczaniem. Po upływie czasu lądują w „Wygasłe” i zostają tam, aż je usuniesz, bo mogłeś jeszcze nie dojść do parkomatu albo butelkomatu."),
            ("Jak pokazać kod z biletu?", "Jeśli kwit ma kod QR lub kreskowy, na ekranie głównym ma przycisk z kodem, a w szczegółach „Pokaż kod do zeskanowania”. Kod jest rysowany ostro na białym tle, a ekran rozjaśnia się do maksimum. Kod możesz zeskanować aparatem w formularzu albo wpisać ręcznie."),
            ("Nie dostaję przypomnień", "W menu „Więcej” sprawdź, czy przełącznik „Przypomnienia” jest włączony. Jeśli iOS blokuje powiadomienia, włącz je w Ustawieniach telefonu. Przypomnienie nie zadziała, jeśli jego moment już minął, a aplikacja ostrzeże o tym przy zapisie."),
            ("Jak zablokować aplikację Face ID?", "W menu „Więcej” włącz „Zabezpieczenie”. Aplikacja zablokuje się po przejściu w tło i przy starcie. Jeśli Face ID zawiedzie, odblokujesz ją kodem telefonu."),
            ("Gdzie są moje dane i czy zniknęły po zmianie telefonu?", "Domyślnie kwity i zdjęcia są tylko na urządzeniu, bez konta i chmury aplikacji (anonimowe statystyki i raporty o awariach trafiają do Google Firebase). Jeśli wykupisz synchronizację iCloud, trafiają też do Twojego prywatnego iCloud i pojawiają się na Twoich innych urządzeniach. Bez niej przy przenoszeniu na nowy telefon dane przeniosą się razem z kopią zapasową iCloud lub komputera, jeśli ją masz. Usunięcie aplikacji usuwa dane z telefonu."),
            ("Czy muszę coś płacić?", "Nie. Aplikacja jest darmowa. W menu są dwa dobrowolne zakupy: „Postaw mi kawę” (napiwek dla twórcy, niczego nie odblokowuje) i „Funkcje Pro”, czyli synchronizacja iCloud (jednorazowo, na stałe, bez abonamentu)."),
            ("Jak działa synchronizacja iCloud?", "W menu „Więcej” → „Funkcje Pro” → „Synchronizacja iCloud” kup funkcję, potem zamknij Kwity i otwórz je ponownie. Kwity i zdjęcia pojawią się na innych urządzeniach z tym samym Apple ID i włączonym iCloud, czasem po kilku minutach. Na nowym telefonie wybierz „Przywróć zakupy”. Synchronizację wyłączysz przełącznikiem „Synchronizuj”."),
        ],
    ),
)

EN = dict(
    folder="en", html_lang="en", label="English", pick="Home",
    nav_privacy="Privacy", nav_support="Support", footer_copy="© 2026 ideaapps.io", footer_langs="Languages",
    index=dict(
        title="Kwity: receipts and warranties",
        description="Kwity keeps track of warranties, return windows, deposits, parking and queue numbers. Snap a receipt and get a reminder before it is too late.",
        h1="Everything that loses value, under control",
        lead="Kwity keeps track of the end of a warranty, a return window, a bottle deposit, a parking ticket and a queue number. Snap a receipt and we remind you before it is too late.",
        download="Download on the App Store", support_btn="Support", privacy_btn="Privacy policy",
        cards=[
            ("Receipt scanning", "The document camera or a photo from your library. Store, amount and date are read on your phone."),
            ("Warranties and returns", "Day countdowns, categories and a list of what ends soon."),
            ("For a moment", "Deposits, parking and queue tickets with a live countdown. They stay until you clear them."),
            ("QR codes and barcodes", "Show a ticket's code with one tap. The screen brightens by itself and the code is drawn sharply."),
            ("Reminders", "A notification before a deadline, set separately for every receipt."),
            ("iCloud sync (Pro)", "Optional, a one-time purchase: your receipts and photos on all your devices, in your own private iCloud."),
            ("Private", "No account, no ads. Your receipts and photos stay on your phone or in your own iCloud. Face ID lock, dark and light looks."),
        ],
        note="Available in English, Polish, Spanish, Italian, German, Russian and Chinese. The app is free; the Pro features are optional.",
    ),
    support=dict(
        title="Support | Kwity", description="Help and contact for the Kwity app.",
        h1="Support", lead="A question, an idea, or did you find a bug in Kwity? Write to me, I answer every message.",
        report="Report an idea or a bug", mail="Send an e-mail", privacy="Privacy policy",
        mail_line="E-mail: {mail}. When reporting a bug, please include the app version and the iOS version.", faq="Frequently asked questions",
        qa=[
            ("How do I add a receipt?", "On the bottom bar tap “Scan receipt” to photograph a receipt, or the plus to add one by hand. The app reads the store, amount and date, and you check the form and save. The product name is always marked “check”, because it is the easiest thing to miss."),
            ("I have no camera, or I prefer a photo from the library", "The scanning screen has a “From library” button. You can also pick a photo from your library when adding a receipt by hand."),
            ("The receipt was not read well", "Take the photo flat, in good light, with the text in focus. Recognition can make mistakes, so always check the data before saving. Every field can be corrected by hand."),
            ("What is the difference between a warranty and a return window?", "Both have an end date and go into a category. A warranty is usually months or years, a return a few or a dozen days. After the date, or once marked as used, the receipt goes to the archive in the “More” menu."),
            ("What is “For a moment” and why does a ticket not disappear on its own?", "These are deposits, parking and queue tickets with a countdown. When time runs out they land in “Expired” and stay there until you remove them, because you may not have reached the meter or the bottle machine yet."),
            ("How do I show a ticket's code?", "If a receipt has a QR code or barcode, it has a code button on the home screen and “Show code to scan” in the details. The code is drawn sharply on white and the screen brightens to the maximum. You can scan the code with the camera in the form or type it in."),
            ("I am not getting reminders", "In the “More” menu check that the “Reminders” switch is on. If iOS blocks notifications, turn them on in your phone's Settings. A reminder will not fire if its moment has already passed, and the app warns you about that when you save."),
            ("How do I lock the app with Face ID?", "In the “More” menu turn on “Security”. The app locks when it goes to the background and at launch. If Face ID fails, you can unlock it with your device passcode."),
            ("Where is my data, and does it survive a new phone?", "By default your receipts and photos are only on the device, with no account and no app cloud (anonymous statistics and crash reports go to Google Firebase). If you buy iCloud sync, they are also copied to your own private iCloud and appear on your other devices. Without it, moving to a new phone brings your data along with an iCloud or computer backup, if you have one. Deleting the app deletes the data from the phone."),
            ("Do I have to pay anything?", "No. The app is free. The menu has two voluntary purchases: “Buy me a coffee” (a tip for the developer, it unlocks nothing) and “Pro features”, which is iCloud sync (one time, for good, no subscription)."),
            ("How does iCloud sync work?", "In the “More” menu go to “Pro features” → “iCloud sync”, buy the feature, then close Kwity and open it again. Your receipts and photos appear on your other devices with the same Apple ID and iCloud turned on, sometimes after a few minutes. On a new phone choose “Restore purchases”. You can switch sync off with the “Sync” switch."),
        ],
    ),
)
