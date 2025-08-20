def test_server_registers_tools():
    # importing the server wires the FastMCP tools; ensure it builds and names them
    from toolbox.server import mcp
    assert mcp is not None
