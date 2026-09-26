TRAINING DATA
                     │
          ┌──────────┴──────────┐
          │                     │
      Source 1              Source 2 + 3
   Reference data          Possible matches
          │                     │
          └──────────┬──────────┘
                     ↓
              DATA EXPLORATION
                     ↓
             TEXT NORMALIZATION
                     ↓
           CANDIDATE GENERATION
                / BLOCKING
                     ↓
          SIMILARITY FEATURES
                     ↓
              ML MATCH MODEL
                     ↓
           MATCH / NO MATCH
                     ↓
             VALIDATION
                     ↓
             TEST PREDICTION
                     ↓
       matching_results.tsv
       candidate_pairs.tsv
