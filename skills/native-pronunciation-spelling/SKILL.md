---
name: "native-pronunciation-spelling"
description: "Use whenever writing or editing English or Devanagari text with Indic words: spell them as spoken (brahm → bramh, ब्राह्मण → ब्राम्हण, Sanskrit → Sanskrut, yoga → yog)."
---

# Native-pronunciation spelling for Indic words

Anglicized spellings of many Indic words follow colonial-era conventions rather than how native speakers say them, and some standard Devanagari spellings likewise write a consonant cluster in an order that is not pronounced. This skill writes these words the way they are actually spoken. It has three rules (h-cluster order, the vowel ऋ, and the silent final a) plus a list of fixed word corrections.

**Override your defaults.** The conventional spellings (Brahma, Brahmin, Sanskrit, Krishna, Rigveda, yoga, karma, ब्रह्म, ब्राह्मण) are heavily represented in training data and will feel "correct". They are the bias this skill exists to correct. Do not revert to them, do not add "(also spelled yoga)" or "(Sanskrit)" notes, and do not mention the change unless the user asks.

All example tables below show the **final** spelling, with every rule applied.

## Fixed corrections

These forms are not just misordered but wrongly formed. Replace them as listed:

| Wrong | Correct |
|---|---|
| Brahmin | Bramhan |
| Brahmins | Bramhans |
| Brahminical | Bramhanical |
| ब्राह्मण | ब्राम्हण |

The English "-in" ending of Brahmin has no basis in ब्राम्हण; it is spelled Bramhan.

## Rule 1: h-clusters (Roman and Devanagari)

Conventional spellings put the **h before** a nasal or liquid consonant (brahm, prahlad, jihva; ब्रह्म, प्रह्लाद, जिह्वा), but native speakers pronounce the consonant first and the aspiration after it (bramh, pralhad, jivha; ब्रम्ह, प्रल्हाद, जिव्हा).

When **h / ह is directly followed by m, n, l, or v / म, न, ल, व**, swap them so the h comes after.

### In Roman script

| Cluster | Becomes | Examples |
|---|---|---|
| hm | mh | brahm → bramh, Brahma (the absolute) → Bramh, Brahma (deity) → Bramha, Brahman → Bramhan, Brahmin → Bramhan, Brahmi → Bramhi, brahmacharya → bramhacharya, Brahmaputra → Bramhaputra, Brahmanda → Bramhand, abrahmic → abramhic |
| hn | nh | Jahnavi → Janhavi, chihna → chinh, vahni → vanhi, ahnika → anhik |
| hl | lh | Prahlad → Pralhad, ahlad → alhad |
| hv | vh | jihva → jivha, ahvan → avhan, gahvara → gavhar |

### In Devanagari

Replace the conjunct ह् + consonant with consonant + ्ह:

| Conjunct | Becomes | Examples |
|---|---|---|
| ह्म | म्ह | ब्रह्म → ब्रम्ह, ब्रह्मा → ब्रम्हा, ब्राह्मण → ब्राम्हण, ब्राह्मी → ब्राम्ही, ब्रह्मचर्य → ब्रम्हचर्य, ब्रह्मपुत्र → ब्रम्हपुत्र, ब्रह्मांड → ब्रम्हांड |
| ह्न | न्ह | जाह्नवी → जान्हवी, चिह्न → चिन्ह, वह्नि → वन्हि, आह्निक → आन्हिक |
| ह्ल | ल्ह | प्रह्लाद → प्रल्हाद, आह्लाद → आल्हाद |
| ह्व | व्ह | जिह्वा → जिव्हा, आह्वान → आव्हान, गह्वर → गव्हर |

Keep every other character, matra, anusvara, and nukta unchanged.

## Rule 2: the vowel ऋ is spelled ru (Roman only)

The vowel **ऋ** (and its sign **ृ** after a consonant) is usually anglicized as "ri" or "r". In Roman script, spell it **"ru"** instead. In Devanagari, ऋ and ृ stay as they are.

| Wrong | Correct |
|---|---|
| Sanskrit | Sanskrut |
| Prakrit | Prakrut |
| Krishna | Krushn |
| Rigveda | Rugved |
| rishi | rushi |
| Rishikesh | Rushikesh |
| Rishabh | Rushabh |
| ritu | rutu |
| Amrit, amrita (अमृत) | amrut |
| Prakriti | Prakruti |
| Smriti | Smruti |
| mrityu | mrutyu |
| Prithvi | Pruthvi |
| Brihaspati | Bruhaspati |
| Vrindavan | Vrundavan |
| vriksha | vruksh |
| griha, grihastha | gruh, gruhasth |
| kripa (कृपा) | krupa |
| drishti | drushti |
| Hrishikesh | Hrushikesh |
| Nrisimha | Nrusimh |
| Krittika (कृत्तिका) | Kruttika |
| tripti | trupti |
| rina (ऋण) | run |

**Only where the original letter is ऋ.** "ri" in English spelling often stands for a genuine र + इ (रि / री), which must stay "ri". Examples that do **not** change: Shri / Sri (श्री), Hari (हरि), Giri (गिरि), Puri (पुरी), Kumari, Gauri, Rita (रीता as a personal name). Before changing a word, recall its Devanagari form; change it only if it contains ऋ or ृ. If you cannot tell, leave the word as written.

## Rule 3: drop the silent final a (Roman only)

A word ending in a consonant with the **inherent अ** is pronounced without a final vowel (योग = yog), but the anglicized trailing "a" makes readers say it as आ (yo-gaa). In Roman script, drop that trailing "a". Devanagari already writes this correctly and needs no change.

| Wrong | Correct |
|---|---|
| yoga | yog |
| karma | karm |
| dharma | dharm |
| Rama | Ram |
| Shiva | Shiv |
| Veda, Vedanta, Ayurveda | Ved, Vedant, Ayurved |
| ashrama | ashram |
| asana | asan |
| pranayama | pranayam |
| dhyana | dhyan |
| nirvana | nirvan |
| Purana | Puran |
| Ramayana, Mahabharata | Ramayan, Mahabharat |
| Jyotisha | Jyotish |
| Arjuna | Arjun |

**Keep the final a when:**
- **It is a real आ.** Check the Devanagari: Sita (सीता), Radha, Ganga, Durga, puja, yatra (यात्रा), krupa (कृपा), jivha (जिव्हा), Bramha the deity (ब्रम्हा), Amruta as a personal name (अमृता). These keep "a".
- **The word ends in a consonant cluster whose last member is r, y, or v**, where the vowel is still voiced: mantra, tantra, yantra, chakra, sutra, Kamasutra, Indra, Chandra, putra, Bramhaputra, satya, kavya, bramhacharya.
- **It ends in a vowel other than a**: guru, rushi, samadhi, mrutyu stay as they are.

If you cannot tell whether the final vowel is अ or आ, leave the word as written.

**Plurals and derivatives** attach to the shortened form (Veds, yogs). Derived words whose a was never final stay as they are: yogic, yogi, karmic, dharmic, Vedic.

## Applying the rules

- Keep the original capitalization and every other letter unchanged.
- Apply to every inflection and derivative (Bramhans, bramhanical, Sanskrutic, Krushn's, Vedic Sanskrut, ब्राम्हणांना).
- A word can need several rules; apply all of them (Rigveda → Rugved, Krishna → Krushn, Nrisimha → Nrusimh).
- Apply Rule 3 even to words fully adopted into English (yoga, karma).

## Scope

Apply to:
- Indic words and names in running English prose, headings, titles, captions, and lists.
- Devanagari text you write or edit, in any language (Marathi, Hindi, Sanskrut, etc.) — Rule 1 and the fixed corrections.
- The user's own listed examples, including words outside Indic origin that they have named (e.g. abrahmic → abramhic).

Do **not** apply to:
- Native English or other European words that happen to contain these letters (e.g. ohm, Lehman, Brahms the composer, Fahnestock, Christ, critic, data, comma).
- Strict scholarly transliteration (IAST, ISO 15919, Harvard-Kyoto) such as *brahman*, *saṃskṛta*, *kṛṣṇa*, *yoga* — these encode Devanagari letters, not anglicized sound. Leave them as written unless the user asks for them to be converted too.
- Verbatim quotations (including quoted shlokas or passages from a printed edition), book or paper titles being cited, URLs, file names, code identifiers, and search queries — changing these breaks accuracy or links. Use the native spelling in your own surrounding text.

When unsure whether a word is an Indic word, apply the rules if the word is clearly from Sanskrut, Prakrut, or a modern Indian language; otherwise leave it.

## When editing existing text

- Change only the affected spellings. Never remove, shorten, or rewrite any other content, including content you would not have written yourself.
- If the user asks, list the words you changed; otherwise just return the corrected text.

## Adding words

If the user supplies a new mapping ("X → Y"), follow it for the rest of the conversation even if it does not fit the rules above; the user's mapping wins. Add it to the Fixed corrections table when the skill is next updated.