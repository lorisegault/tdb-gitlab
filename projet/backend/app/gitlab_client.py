import httpx


class GitLabClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.headers = {"PRIVATE-TOKEN": token}

    async def _get(self, path: str) -> dict | list:
        async with httpx.AsyncClient(
            base_url=self.base_url, headers=self.headers, timeout=10.0
        ) as client:
            resp = await client.get(path)
            resp.raise_for_status()
            return resp.json()

    async def get_project(self, project_id: int) -> dict:
        return await self._get(f"/api/v4/projects/{project_id}")

    async def get_merge_requests(self, project_id: int) -> list:
        return await self._get(
            f"/api/v4/projects/{project_id}/merge_requests?state=opened"
        )

    async def get_issues(self, project_id: int) -> list:
        return await self._get(
            f"/api/v4/projects/{project_id}/issues?state=opened"
        )

    async def get_pipelines(self, project_id: int) -> list:
        return await self._get(f"/api/v4/projects/{project_id}/pipelines")
