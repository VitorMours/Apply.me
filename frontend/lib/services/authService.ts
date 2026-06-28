import { apiFetch } from "./api";

export interface CreateUserDTO {
    firstName: string,
    lastName: string,
    email: string,
    password: string,
    role?: string
}

export interface LoginUserDTO {
    email: string,
    password: string
}

class AuthService {
    async signin(data: CreateUserDTO) { // TODO: Adicionar o retorno
        return apiFetch("v1/auth/signin",
        {
            body: JSON.stringify(data),
            method: "POST"
        });
    }
    
    async login(data: LoginUserDTO) { // TODO: Adicionar o retorno
        return apiFetch("v1/auth/login",
        {
            body: JSON.stringify(data),
            method: "POST"
        });
    }
}


export default new AuthService();