package com.applyme.backend.auth;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.lang.reflect.Field;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.security.crypto.password.PasswordEncoder;

import com.applyme.backend.auth.internal.Credential;
import com.applyme.backend.auth.internal.CredentialRepository;
import com.applyme.backend.auth.internal.dto.AuthResponse;
import com.applyme.backend.auth.internal.jwt.JwtService;

public class AuthServiceTests {
    
    private PasswordEncoder passwordEncoder;
    private CredentialRepository repository;
    private ApplicationEventPublisher publisher;
    private AuthService service;
    private JwtService jwtService;
    
    @BeforeEach 
    void setUp() {
        repository = mock(CredentialRepository.class);
        passwordEncoder = mock(PasswordEncoder.class);
        publisher = mock(ApplicationEventPublisher.class);
        jwtService = mock(JwtService.class);

        service = new AuthService(repository, passwordEncoder, publisher, jwtService);
    }

    @Test 
    @DisplayName("Verifica Service contem os campos necessarios")
    void verificaServiceContemCamposNecessarios() throws NoSuchFieldException{
        Class<AuthService> class_ = AuthService.class;
        String[] fields = {"passwordEncoder","repository","publisher"};
        for(String field: fields) {
            assertThat(class_.getDeclaredField(field)).isNotNull();
        }
    }

    @Test
    @DisplayName("Verifica se o register funciona corretamente")
    void verificaSeORegisterFuncionaCorretamente() {
        when(repository.existsByEmail("teste.teste@gmail.com")).thenReturn(false);
        when(passwordEncoder.encode("password")).thenReturn("hash-password");
        AuthResponse userId = service.register("Vitor","Moura","teste.teste@gmail.com","password");
        assertThat(userId).isNotNull();
    }

        // void verificaSeOMetodoRegisterFuncionaCorretamente
    // void verificaSePossuiOMetodoDeLogin
    // void verificaSePossuiOMetodoDeAuthenticate
    //
    //
    //
    //
}
