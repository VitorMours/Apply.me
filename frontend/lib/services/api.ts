import { ApiError } from "../errors";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api";

export async function apiFetch<T>(
  endpoint: string,
  options?: RequestInit
): Promise<T> {
  const { headers, ...restOptions } = options ?? {};  // separa os headers do resto

  const response = await fetch(`${API_URL}/${endpoint}`, {
    ...restOptions,  // espalha o resto SEM headers
    headers: {
      'Content-Type': 'application/json',
      ...headers,    // merge dos headers customizados por cima
    },
  });
  if (!response.ok) {
    const error = await response.json();
    throw new ApiError(response.status, error.detail)
  }

  return response.json() as Promise<T>;

}