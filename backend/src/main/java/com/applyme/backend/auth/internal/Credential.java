package com.applyme.backend.auth.internal;

import java.util.UUID;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import jakarta.validation.constraints.NotBlank;


/**
 * Representa as credenciais de acesso do usuario dentro do banco de dados
 * de forma que a senha fica descentralizada do usuario, gerando maior 
 * segurança separando os fluxos de autorização e autenticação
 * 
 * @author Joao Vitor R. Moura 
 * @since 29/07/2026
 */
@Document(collection="credentials")
public class Credential {
    @Id 
    private String id; 
    @NotBlank(message="O valor presente dentro do email nao pode ser nulo")
    private String email; 
    @NotBlank(message="O valor presente dentro da senha nao pode ser nulo")
    private String passwordHash;

    public Credential(String email, String passwordHash) {
        this.id = UUID.randomUUID().toString();
        this.email = email;
        this.passwordHash = passwordHash;
    }
    public String getId() {
        return id;
    }

    public String getEmail() {
        return email;
    }
    
    public String getPasswordHash() {
        return passwordHash;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setPasswordHash(String passwordHash) {
        this.passwordHash = passwordHash;
    }
    public void setId(String string) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'setId'");
    }

}


