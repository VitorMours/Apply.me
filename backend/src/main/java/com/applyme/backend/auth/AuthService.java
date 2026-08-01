package com.applyme.backend.auth;

import org.springframework.stereotype.Service;
import com.applyme.backend.auth.internal.Credential;
import com.applyme.backend.auth.internal.CredentialRepository;
import com.applyme.backend.auth.internal.dto.AuthResponse;
import com.applyme.backend.auth.internal.jwt.JwtService;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.security.crypto.password.PasswordEncoder;

@Service
public class AuthService {

    private final PasswordEncoder passwordEncoder;
    private final CredentialRepository repository;
    private final ApplicationEventPublisher publisher;
    private final JwtService jwtService;

    public AuthService(CredentialRepository repository, PasswordEncoder passwordEncoder, ApplicationEventPublisher publisher, JwtService jwtService){
        this.repository = repository;
        this.passwordEncoder = passwordEncoder;
        this.publisher = publisher;
        this.jwtService = jwtService;
    }

    public AuthResponse register(String firstName, String lastName, String email, String password) {
        if(repository.existsByEmail(email)) {
            throw new IllegalArgumentException("Usuário já cadastrado");
        }
        String passwordHash = passwordEncoder.encode(password);
        Credential credential = new Credential(email, passwordHash);

        repository.save(credential);
        publisher.publishEvent(new UserRegisteredEvent(credential.getId(), firstName, lastName, email));
        
        String token = jwtService.generateToken(credential.getId(), email);
        AuthResponse.UserSummary userSummary = new AuthResponse.UserSummary(
                credential.getId(), firstName + " " + lastName, email);        
        return AuthResponse.of(token, jwtService.getExpirationSeconds(), userSummary);    }

    public void login() {}
    public void authenticate() {}

}