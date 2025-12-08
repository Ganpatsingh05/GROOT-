
---

### 1.13 `tests/test_commands.md` (manual test checklist — optional)
```markdown
# Manual Test Steps

1. gsc init -> .gsc created
2. Create examples/sample.txt
3. gsc add examples/sample.txt -> shows "Staged: examples/sample.txt"
4. gsc status -> shows staged file
5. gsc commit -m "test" -> committed and index cleared
6. gsc log -> shows commit_1
7. Repeat add+commit -> commit_2 etc
