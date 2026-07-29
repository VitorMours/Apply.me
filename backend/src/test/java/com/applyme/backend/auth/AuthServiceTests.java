package com.applyme.backend.auth;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;

import java.lang.reflect.Field;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.security.crypto.password.PasswordEncoder;
import com.applyme.backend.auth.internal.CredentialRepository;

public class AuthServiceTests {
    
    private PasswordEncoder passwordEncoder;
    private CredentialRepository repository;
    private ApplicationEventPublisher publisher;

    @BeforeEach 
    void setUp() {
        repository = mock(CredentialRepository.class);
        passwordEncoder = mock(PasswordEncoder.class);
        publisher = mock(ApplicationEventPublisher.class);
        AuthService service = new AuthService(repository, passwordEncoder, publisher);
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


    // TODO:
    // void verificaSeOEventoEstaSendoPublicado
    // void verificaSeOEventoEstaSendoConstruidoCorretamente
    // void verificaSePossuiOMetodoDeLogin
    // void verificaSePossuiOMetodoDeAuthenticate
    // void verificaSePossuiOMetodoDeRegister
    //
    //
    //
    //
}
