import httpx
from typing import Any, Dict

# in libs/sdk/python/src/duruzi/client.py
def main():
    print("Duruzi SDK installed. Import DuruziClient from duruzi.client.")

class DuruziError(Exception):
    def __init__(self, status_code: int, error: str, message: str):
        super().__init__(f"{status_code} {error}: {message}")
        self.status_code = status_code
        self.error = error
        self.message = message

class DuruziClient:
    def __init__(self, base_url: str, api_key: str, timeout: float = 30.0):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def infer(self, endpoint_id: str, input_text: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
        url = f"{self.base_url}/v1/infer/{endpoint_id}"
        with httpx.Client(timeout=self.timeout) as client:
            r = client.post(url, headers=self._headers(), json={"input": input_text, "params": params or {}})
        if r.status_code >= 400:
            try:
                payload = r.json()
                raise DuruziError(r.status_code, payload.get("error","error"), payload.get("message",""))
            except ValueError:
                r.raise_for_status()
        return r.json()
