package com.applyme.backend.auth.internal;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.data.mongodb.test.autoconfigure.DataMongoTest;
import org.springframework.boot.test.context.TestConfiguration;
import org.springframework.boot.testcontainers.service.connection.ServiceConnection;
import org.springframework.context.annotation.Bean;
import org.springframework.dao.DuplicateKeyException;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.mapping.event.ValidatingEntityCallback;
import org.springframework.test.context.TestPropertySource;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;
import org.testcontainers.mongodb.MongoDBContainer;
import org.testcontainers.utility.DockerImageName;
import jakarta.validation.Validator;
import jakarta.validation.Validation;
import jakarta.validation.ConstraintViolationException;

@DataMongoTest
@Testcontainers
@TestPropertySource(properties = "spring.data.mongodb.auto-index-creation=true")

public class CredentialTests {
    @Container
    @ServiceConnection
    static MongoDBContainer mongo = new MongoDBContainer(DockerImageName.parse("mongo:7"));

    @Autowired
    private MongoTemplate mongoTemplate;

    @TestConfiguration
    static class ValidationConfig {
        @Bean
        Validator validator() {
            return Validation.buildDefaultValidatorFactory().getValidator();
        }

        @Bean
        ValidatingEntityCallback validatingEntityCallback(Validator validator) {
            return new ValidatingEntityCallback(validator);
        }
    }


    @Test 
    @DisplayName("")
    void deveSerDoTipoStringOIdDoUsuario() {

    }
    
    @Test
    @DisplayName("")
    void deveTerOsCamposCorretosDentroDoDocumento() {

    }

    @Test 
    @DisplayName("")
    void deveVerificarSeConsegueCriarOUsuarioComOsCamposCorretos() {

    }

    @Test
    @DisplayName("")
    void deveVerificarSeLevantaErroComCamposNulos() {

    }
    @Test 
    @DisplayName("")
    void deveVerificarSeLevantaErroComCamposVazios() {
        
    }

}
