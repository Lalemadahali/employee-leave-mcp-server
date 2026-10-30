from mcp.server.fastmcp import FastMCP

employee_leaves = {
    "E001": {
        "balance": 18,
        "history": ["2024-12-25", "2025-01-01"],
    },
    "E002": {
        "balance": 20,
        "history": [],
    },
}

mcp = FastMCP("LeaveManager")


@mcp.tool()
def get_leave_balance(employee_id: str) -> str:
    """Return the remaining leave balance for an employee."""
    data = employee_leaves.get(employee_id)

    if data is not None:
        return f"{employee_id} has {data['balance']} leave days remaining."

    return "Employee ID not found."


@mcp.tool()
def get_leave_history(employee_id: str) -> str:
    """Return the dates of an employee's previous leave."""
    data = employee_leaves.get(employee_id)

    if data is not None:
        history = (
            ", ".join(data["history"])
            if data["history"]
            else "No leaves taken."
        )
        return f"Leave history for {employee_id}: {history}"

    return "Employee ID not found."


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Return a personalized leave-management greeting."""
    return f"Hello, {name}! How can I assist you with leave management today?"


if __name__ == "__main__":
    mcp.run(transport="stdio")