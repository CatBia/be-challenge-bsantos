import asyncio


async def get_import_league(league_id: str) -> str:
    pass


async def process_get_import_league(league_id: str) -> str:
    """
    Process the import league request.

    It processes the import league request and returns the status of the request.

    Args:
        league_id: The league id.

    Returns:
        str: The status of the request.
    """
    task = asyncio.create_task(get_import_league(league_id))
    asyncio.gather(task)
    return "success"
