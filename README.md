# guardian-test

Test repository for Guardian dependency update agent.

## What this repo is for

Guardian will:
1. Detect outdated packages in `requirements.txt`
2. Create a new branch `guardian/package-newversion`
3. Update the version in `requirements.txt`
4. Raise a PR
5. Post "rerun this build" comment → triggers Jenkins
6. Jenkins runs `pip install` + `pytest`
7. Pass → PR merged / Fail → RAG suggests fix

## Files

| File | Purpose |
|------|---------|
| `app.py` | Sample Flask app using the dependencies |
| `test_app.py` | pytest tests Jenkins will run |
| `requirements.txt` | Dependencies Guardian will update |
| `Jenkinsfile` | Jenkins pipeline definition |

## How to test Guardian

Send this prompt to Guardian:
```
update numpy to 1.24.0 in yourname/guardian-test
```

Guardian will:
- Find `requirements.txt`
- Change `numpy==1.21.0` to `numpy==1.24.0`
- Create branch `guardian/numpy-1.24.0`
- Raise PR
- Post "rerun this build" → Jenkins builds
