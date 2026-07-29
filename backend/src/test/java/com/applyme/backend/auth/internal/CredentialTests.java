package com.applyme.backend.auth.internal;

import static org.assertj.core.api.Assertions.as;
import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.ArgumentMatchers.isNotNull;
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
    @DisplayName("Se o campo de Id do usuário é uma string UUID")
    void deveSerDoTipoStringOIdDoUsuario() throws NoSuchFieldException {
        Class<Credential> credential = Credential.class;
        assertThat(credential.getDeclaredField("id").getType()).isEqualTo(String.class);
    }
    
    @Test
    @DisplayName("Verifica se os campos corretos existem na entidade")
    void deveTerOsCamposCorretosDentroDoDocumento() throws NoSuchFieldException {
        Class<Credential> credential = Credential.class;
        String[] fields = {"id","email","passwordHash"};
        for(String field: fields) {
            assertThat(credential.getDeclaredField(field));
        }
    }

    @Test 
    @DisplayName("Deve ter getters e setters na entidade testada")
    void deveTerGettersAndSettersInEntity() throws NoSuchMethodException{
        Class<Credential> credential = Credential.class;
        assertThat(credential.getDeclaredMethod("getEmail")).isNotNull();
        assertThat(credential.getDeclaredMethod("getPasswordHash")).isNotNull();
        assertThat(credential.getDeclaredMethod("setEmail", String.class)).isNotNull();
        assertThat(credential.getDeclaredMethod("setPasswordHash", String.class)).isNotNull();
    }

    @Test 
    @DisplayName("Verifica se consegue criar usuario corretamente")
    void deveVerificarSeConsegueCriarOUsuarioComOsCamposCorretos() {
        Credential credential = new Credential(
            "jvrezendemoura@gmail.com",
            "sadsadsadsadasdapdmwoaidm"
        );
        assertThat(credential.getEmail()).isEqualTo("jvrezendemoura@gmail.com");
        assertThat(credential.getPasswordHash()).isEqualTo("sadsadsadsadasdapdmwoaidm");
    }

    @Test
    @DisplayName("Verifica se campos vazios geram exceção")
    void deveVerificarSeLevantaErroComCamposVazios() {
        Credential credential = new Credential(
            "",
            ""
        );
        assertThatThrownBy(() -> mongoTemplate.save(credential)).isInstanceOf(ConstraintViolationException.class);

        Credential credential2 = new Credential(
            "teste.teste@gmail.com",
            ""
        );
        assertThatThrownBy(() -> mongoTemplate.save(credential2)).isInstanceOf(ConstraintViolationException.class);

        Credential credential3 = new Credential(
            "",
            "asdisadoisadmoisadm"
        );
        assertThatThrownBy(() -> mongoTemplate.save(credential3)).isInstanceOf(ConstraintViolationException.class);
    }
    
    @Test 
    @DisplayName("Verifica se campos nulos geram exceção")
    void deveVerificarSeLevantaErroComCamposNulos() {
        Credential credential = new Credential(
            null,
            "passworda-sd1"
        );
        assertThatThrownBy(() -> mongoTemplate.save(credential)).isInstanceOf(ConstraintViolationException.class);
        Credential credential2 = new Credential(
            "teste.teste@gmail.com",
            null
        );
        assertThatThrownBy(() -> mongoTemplate.save(credential2)).isInstanceOf(ConstraintViolationException.class);
        Credential credential3 = new Credential(
            null,
            null
        );
        assertThatThrownBy(() -> mongoTemplate.save(credential3)).isInstanceOf(ConstraintViolationException.class);

    }

    @Test 
    @DisplayName("Verifica se consegue atualizar valores da entidade")
    void deveVerificarSeConsegueAtualizarValores() {
        // limpa coleção antes do teste
        mongoTemplate.dropCollection(Credential.class);

        Credential credential = new Credential("old.email@aplly.dev", "old-hash");
        mongoTemplate.save(credential);

        // recupera, atualiza e salva novamente
        Credential saved = mongoTemplate.findAll(Credential.class).stream()
            .filter(c -> c.getEmail().equals("old.email@aplly.dev"))
            .findFirst()
            .orElseThrow();

        saved.setEmail("new.email@aplly.dev");
        saved.setPasswordHash("new-hash");
        mongoTemplate.save(saved);

        // verifica se as alterações foram persistidas
        Credential updated = mongoTemplate.findAll(Credential.class).stream()
            .filter(c -> c.getEmail().equals("new.email@aplly.dev"))
            .findFirst()
            .orElseThrow();

        assertThat(updated.getPasswordHash()).isEqualTo("new-hash");
        }

}
