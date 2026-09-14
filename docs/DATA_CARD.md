# READI data card

## Summary

READI (Read the Room, Read the Image) is a bilingual Visual Pragmatic Question
Answering benchmark for indirect directive speech-act understanding. A model must
combine an utterance with sociopragmatic information depicted in an image and
select the intended directive function from four choices.

| Subset | Paper count | Language | Construction |
|---|---:|---|---|
| KRISA | 57 | Korean | Korean scenarios drafted by native speakers and reviewed by linguists |
| ENGISA | 45 | English | Adapted from English pragmatics studies and validated by native speakers and expert linguists |

The subsets are independent, not translations.

## Indirectness ontology

- `1 / CID`: conventionally indirect directive;
- `2 / NCID_STRONG`: non-conventionally indirect directive with a lexical hint;
- `3 / NCID_MILD_NONE`: non-conventionally indirect directive with a mild or no explicit hint.

Direct directives are part of the theoretical scale but are not included in the
final benchmark items reported in the paper.

## Sociopragmatic design

Scenario design controls interlocutor relations, power asymmetry and hierarchy,
social distance, interactional situation and physical setting, and the target and
content of the directive act. Images provide pragmatic context rather than serving
as object-recognition targets; the paper states that images exclude textual
elements and speech bubbles.

## Public schema

- `item_id`: `readi_ko_###` or `readi_en_###`;
- `language`: `ko` or `en`;
- `image`: relative image path;
- `question` and `utterance`;
- `choices`: mapping from `1` through `4` to answer text;
- `answer`: integer from 1 through 4;
- `isa_intensity`: integer from 1 through 3;
- `source_reference`: optional English source provenance.

## Evaluation

The primary metric is exact four-choice accuracy. Explanations may be collected
for qualitative visual-grounding analysis but are not part of the primary score.

## Limitations

- READI covers indirect directives only.
- Scenarios are theory-driven rather than naturally occurring.
- Only Korean and English are represented.
- The task evaluates understanding, not generation.
- Current source files have unresolved count and intensity discrepancies documented
  in `SOURCE_AUDIT.md`.

## Privacy and consent

The paper states that contributors were recruited through academic and professional
networks, informed consent was obtained, the data is for research use, and personal
identifiers were anonymized. A release-level human review is still required.

