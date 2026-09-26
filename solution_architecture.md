# Solution Architecture

## 1. Normalization

Business names and addresses are normalized before matching.

Operations:

1. convert to lowercase
2. transliterate Unicode text where possible
3. convert `&` to `and`
4. remove punctuation/symbol noise
5. collapse repeated whitespace
6. preserve empty strings for missing fields

This makes superficial formatting differences less important.

## 2. Candidate generation

Comparing every Source-1 record with every Source-2/Source-3 record would be computationally expensive and would create an enormous number of irrelevant pairs.

The solution therefore uses blocking.

### Block A — normalized name + country

Records with the same normalized business name and country are candidate pairs.

### Block B — address prefix + country

Whitespace-free normalized address prefixes are used as another blocking key.

### Candidate union

Candidates from both blocks are unioned and deduplicated.

The candidate-generation stage is intentionally separated from feature engineering so that candidate recall can be measured independently.

## 3. Feature engineering

For every candidate pair:

- name WRatio
- name token-set ratio
- address WRatio
- address token-set ratio
- exact normalized-name indicator
- country-match indicator
- name missingness
- address missingness
- name-length difference
- address-length difference

These features combine fuzzy similarity with simple structural evidence.

## 4. Supervised matching model

Training labels are constructed from `train_ground_truth.tsv`.

A Random Forest classifier predicts whether each candidate pair is a true match.

A Source-1-level split is preferred for validation so records from the same Source-1 entity do not leak between training and validation.

## 5. Threshold selection

The model produces a probability for each candidate pair.

Instead of blindly using 0.5, several thresholds are evaluated.

Because the challenge metric is entity-level macro F0.5, the validation notebook calculates the challenge-style metric by:

1. grouping predictions by Source-1 entity
2. converting each predicted list to a set
3. comparing it with the ground-truth set
4. calculating F0.5 per Source-1 entity
5. averaging across Source-1 entities

## 6. Test prediction

For test data:

1. normalize all three sources
2. generate candidates
3. calculate the same features
4. load the trained model
5. apply the selected threshold
6. group predicted S2/S3 IDs by S1
7. create a row for every test S1 entity
8. write `matching_results.tsv`
9. write `candidate_pairs.tsv`

## 7. Submission validation

The supplied validator checks:

- exact required headers
- TAB-separated format
- duplicate Source-1 rows
- duplicate IDs inside a list
- illegal S1 matches
- invalid ID prefixes
- missing required S1 rows
- extra S1 rows
- optional existence of S2/S3 IDs
- whether final matches come from candidate lists

This validation should be run before packaging the submission.
