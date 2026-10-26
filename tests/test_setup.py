def test_environment():
    import duckdb, pandas, pyarrow
    assert duckdb.__version__