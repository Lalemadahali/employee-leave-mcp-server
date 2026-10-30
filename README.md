# employee-leave-mcp-server
Python MCP server integrated with Claude Desktop to retrieve employee leave balances and history
# Employee Leave Management MCP Server

A hands-on Python project that connects Claude Desktop to custom tools
through the Model Context Protocol (MCP).

The server allows Claude to retrieve employee leave balances and leave
history through natural-language requests. It uses FastMCP and a small
in-memory dataset containing fictional employee records.

## Features

- Retrieve an employee's remaining leave balance.
- Retrieve an employee's previous leave dates.
- Provide a personalized greeting through an MCP resource.
- Connect to Claude Desktop using stdio transport.

## Technologies

Python, MCP Python SDK v1, FastMCP, Claude Desktop, and uv.

## Setup

Use Python 3.11 or newer and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the server:

```bash
python main.py
```

The server uses stdio, so it waits for an MCP client rather than opening
a web page.

## Connect to Claude Desktop

Open Claude Desktop's developer settings and select Edit Config.

Add the following entry to the configuration, replacing both paths with
the actual paths on your computer. If you already have an `mcpServers`
section, add the server inside that existing section.

```json
{
  "mcpServers": {
    "leave-manager": {
      "command": "C:/path/to/python.exe",
      "args": [
        "C:/path/to/my-first-mcp-server/main.py"
      ]
    }
  }
}
```

Use the Python executable from the environment where you installed the
dependencies. You can find it with:

```bash
python -c "import sys; print(sys.executable)"
```

Save the configuration, fully quit Claude Desktop, and reopen it.

## Example Request

“Use the leave-management tools to check the balance and leave history
for employee E001.”

Expected results:

- Remaining balance: 18 days
- Leave history: 2024-12-25 and 2025-01-01

## Project Scope

This is a learning prototype using fictional, in-memory data. It supports
read-only lookups; it does not submit leave requests, update balances,
authenticate employees, or connect to an HR database.

## Acknowledgment

Built while following this tutorial, with adjustments for my local
Python environment and Claude Desktop configuration:

https://www.youtube.com/watch?v=jLM6n4mdRuA
