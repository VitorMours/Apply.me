package com.applyme.backend.auth;

import org.springframework.stereotype.Service;
import com.applyme.backend.auth.internal.Credential;
import com.applyme.backend.auth.internal.CredentialRepository;

import org.springframework.context.ApplicationEventPublisher;
import org.springframework.security.crypto.password.PasswordEncoder;

@Service
public class AuthService {


    //TODO: Adicionar o modulo de seguranca dentro do spring
    private final PasswordEncoder passwordEncoder;
    private final CredentialRepository repository;
    private final ApplicationEventPublisher publisher;

    public AuthService(CredentialRepository repository, PasswordEncoder passwordEncoder, ApplicationEventPublisher publisher){
        this.repository = repository;
        this.passwordEncoder = passwordEncoder;
        this.publisher = publisher;
    }

    public void register() {}
    public void login() {}
    public void authenticate() {}

}