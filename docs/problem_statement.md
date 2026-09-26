# Problem Statement

The challenge is a **Business Entity Resolution** task.

Three independent sources contain business records. Source 1 acts as the reference set, while Source 2 and Source 3 contain noisy records that may refer to the same real-world businesses.

For every Source-1 entity, the system must determine which Source-2 and Source-3 entity IDs refer to the same business.

A Source-1 entity may have:

- no matching records
- one matching record
- multiple matching records

There is no shared identifier that directly links the records.

The main sources of noise are business-name variation, address variation, spelling errors, punctuation, abbreviations, legal suffixes, word-order changes, transliteration, and missing address components.

The solution therefore has to perform **record linkage rather than simple exact joins**.

The evaluation is precision-heavy and uses macro-averaged F0.5 at the Source-1 entity level. This makes both correct positive matches and careful handling of no-match/singleton cases important.

The challenge also requires every test Source-1 entity to appear in the final output, including entities for which the predicted match list is empty.
