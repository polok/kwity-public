# kwity-public

The public site of Kwity (served at https://haker.dev/kwity-public/): a landing page, the privacy policy and the support page in Polish, English, German, French, Spanish, Italian, Ukrainian, Russian, Japanese and Chinese: `pl/`, `en/`, `de/`, `fr/`, `es/`, `it/`, `uk/`, `ru/`, `ja/`, `zh/`. The pages at the root only send the browser to its language (and list all of them).

Everything is generated; do not edit the HTML by hand.

```bash
python3 tools/build.py                                          # pages and stylesheet
python3 tools/build.py --policies ../kwity-ios/Kwity/Resources  # first re-read the privacy policies the app ships (all ten languages)
```

- Texts: `tools/content_*.py` (one dict per language, the same structure in all of them; edit every language when the meaning changes) and `tools/privacy/<lang>.html` (the privacy policy, a copy of the one the app ships).
- Layout and styles: `tools/build.py`.
- The privacy policy must stay in step with the app (`Kwity/Resources/<lang>.lproj/PrivacyPolicy.html`) and with the App Privacy answers in App Store Connect; bump its "updated" date when it changes.
- The App Store listing links to `<lang>/privacy.html` and `<lang>/support.html` (`fastlane/metadata` in kwity-ios).
