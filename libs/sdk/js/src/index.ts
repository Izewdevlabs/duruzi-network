export class DuruziError extends Error {
  statusCode: number;
  code: string;
  constructor(statusCode: number, code: string, message: string) {
    super(`${statusCode} ${code}: ${message}`);
    this.statusCode = statusCode;
    this.code = code;
  }
}

export async function infer(baseUrl: string, apiKey: string, endpointId: string, input: string, params: Record<string, any> = {}) {
  const url = `${baseUrl.replace(/\/$/, '')}/v1/infer/${endpointId}`;
  const resp = await fetch(url, {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${apiKey}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ input, params })
  });
  if (!resp.ok) {
    let payload: any = {};
    try { payload = await resp.json(); } catch {}
    throw new DuruziError(resp.status, payload.error || 'error', payload.message || '');
  }
  return await resp.json();
}
