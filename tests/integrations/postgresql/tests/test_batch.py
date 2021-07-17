import pytest
from prisma import Client


@pytest.mark.asyncio
async def test_create_many(client: Client) -> None:
    async with client.batch_() as batcher:
        batcher.user.create({'name': 'Robert'})
        batcher.user.create({'name': 'Tegan'})

    assert await client.user.count() == 2
