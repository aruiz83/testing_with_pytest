## Run pytest

```python
pytest -v
```

## Run Coverage

```python
coverage run --omit='tests/*' -m pytest
coverage report --omit='*/tests/*'
coverage html
```
