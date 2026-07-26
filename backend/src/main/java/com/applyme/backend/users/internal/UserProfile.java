package com.applyme.backend.users.internal;

import java.util.UUID;
import java.io.Serializable;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;

/**
 * Representa o perfil de usuário dentro do sistema,
 * possuindo informações genéricas que podem ser herdadas. 
 * Pode ser usado por outros módulos
 * @author Vitor Moura 
 * @since 0.0.1 - 25/07/2026
 */
@Document(collection="users")
public class UserProfile implements Serializable {

    @Id 
    private String id;
    
    @NotBlank(message="O Primeiro nome não pode ser vazio")
    private String firstName;
    
    @NotBlank(message="O Sobrenome não pode ser vazio")
    private String lastName; 
    
    @NotBlank(message="Email não pode ser vazio")
    @Email(message="Email não válido")
    @Indexed(unique=true)
    private String email;
    
    /**
     * Construtor exigido pelo SpringData para reidratação da entidade a partir 
     * do banco de dados via reflection
     */
    protected UserProfile() {}

    /**
     * Construtor para a entidade do banco de dados com os parâmetros
     * @param firstName
     * @param lastName
     * @param email
     */
    public UserProfile(String firstName, String lastName, String email) {
        this.id = UUID.randomUUID().toString();
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
    }

    public String getId() {
        return id;
    }
    public String getFirstName() {
        return firstName;
    }
    public String getLastName() {
        return lastName;
        }
    public String getEmail() {
        return email;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
    public void setEmail(String email) {
        this.email = email;
    }
}