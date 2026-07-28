package com.applyme.backend.users.internal;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

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
class UserProfileTests {

    @Container
    @ServiceConnection
    static MongoDBContainer mongo = new MongoDBContainer(DockerImageName.parse("mongo:7"));

    @Autowired
    private MongoTemplate mongoTemplate;

    @Test
    void deveriaPossuirCampoDeIdDoTipoString() throws NoSuchFieldException {
         Class<UserProfile> profile = UserProfile.class;
         assertThat(profile.getDeclaredField("id").getType()).isEqualTo(String.class);
    }

    @Test 
    void devePossuirOsCamposCorretosDentroDoModelo() throws NoSuchFieldException {
        Class<UserProfile> profile = UserProfile.class;
        String[] namesArray = {"id","firstName","lastName","email"};
        for(String name: namesArray) {
            assertThat(profile.getDeclaredField(name));
        }
    }

    @Test 
    void deveVerificarSeConsegueCriarComOsCamposCorretamente() {
        UserProfile profile = new UserProfile(
            "Vitor",
            "Moura",
            "vitor.moura@gmail.com"
        );
        assertThat(profile.getFirstName()).isEqualTo("Vitor");
        assertThat(profile.getLastName()).isEqualTo("Moura");
        assertThat(profile.getEmail()).isEqualTo("vitor.moura@gmail.com");
    }

    @Test 
    void deveLancarErroAoTentarSalvarComOsCamposVazios() {
        UserProfile profile = new UserProfile(
            "",
            "",
            ""
        );
        assertThatThrownBy(() -> mongoTemplate.save(profile)).isInstanceOf(ConstraintViolationException.class);
    }

    @Test 
    void deveLancarErroAoTentarSalvarComOsCamposErrados() {
        UserProfile profile1 = new UserProfile(
            "Vitor",
            "Moura",
            "123"
        );
        assertThatThrownBy(() -> mongoTemplate.save(profile1)).isInstanceOf(ConstraintViolationException.class);
 
        UserProfile profile2 = new UserProfile(
            null,
            "Moura",
            "vitor.moura@gmail.com"
        );
        assertThatThrownBy(() -> mongoTemplate.save(profile2)).isInstanceOf(ConstraintViolationException.class);
 
        UserProfile profile3 = new UserProfile(
            "Vitor",
            null,
            "vitor.moura@gmail.com"
        );
        assertThatThrownBy(() -> mongoTemplate.save(profile3)).isInstanceOf(ConstraintViolationException.class);
 
        UserProfile profile4 = new UserProfile(
            "Vitor",
            "Moura",
            null
        );
        assertThatThrownBy(() -> mongoTemplate.save(profile4)).isInstanceOf(ConstraintViolationException.class);
    }

    @Test 
    void deveLancarErroAoPossuirInformacoesDuplicados() {
        UserProfile profile1 = new UserProfile(
            "Vitor",
            "Moura",
            "teste.teste@email.com"
        );
 
        mongoTemplate.save(profile1);
        UserProfile profile2 = new UserProfile(
            "Vitor",
            "Moura",
            "teste.teste@email.com"
        );
        assertThatThrownBy(() -> mongoTemplate.save(profile2)).isInstanceOf(DuplicateKeyException.class);
    }

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
}