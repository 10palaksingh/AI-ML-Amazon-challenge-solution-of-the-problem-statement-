# GitHub Upload Guide

## Recommended repository name

`business-entity-resolution-ml`

## Option A — GitHub website

1. Create a new GitHub repository.
2. Keep it public only if the competition rules allow public code.
3. Extract this project ZIP.
4. Upload the project folders/files.
5. Commit with:
   `Initial project: business entity resolution ML pipeline`

## Option B — Git commands

From the project folder:

```bash
git init
git add .
git commit -m "Initial entity resolution ML pipeline"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Then future changes:

```bash
git add .
git commit -m "Improve candidate generation and validation"
git push
```

## What should be public

Good public files:

- notebooks
- source code
- README
- methodology
- requirements
- `.gitignore`

Normally keep private:

- challenge training/test TSVs
- ground truth
- large candidate-pair files
- generated model binaries
- final competition outputs, unless the competition permits publication

## Suggested GitHub README sections

1. Project overview
2. Problem statement
3. Dataset structure
4. Approach
5. Candidate generation
6. Feature engineering
7. Model
8. Evaluation
9. Submission format
10. How to run
11. Limitations / future improvements
