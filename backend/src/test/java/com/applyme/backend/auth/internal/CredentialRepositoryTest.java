package com.applyme.backend.auth.internal;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.data.mongodb.test.autoconfigure.DataMongoTest;
import org.springframework.boot.testcontainers.service.connection.ServiceConnection;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;
import org.testcontainers.mongodb.MongoDBContainer;

import static org.assertj.core.api.Assertions.assertThat;

import java.util.Optional;

@DataMongoTest
@Testcontainers
class CredentialRepositoryTest {

    @Container
    @ServiceConnection
    static MongoDBContainer mongo = new MongoDBContainer("mongo:7");

    @Autowired
    CredentialRepository repository;

    @BeforeEach
    void cleanUp() {
        repository.deleteAll();
    }

    @Test
    void shouldFindCredentialByEmailWhenExists() {
        var credential = new Credential("user@aplly.dev", "hash123");
        repository.save(credential);

        Optional<Credential> found = repository.findByEmail("user@aplly.dev");

        assertThat(found).isPresent();
        assertThat(found.get().getEmail()).isEqualTo("user@aplly.dev");
    }

    @Test
    void shouldReturnEmptyWhenEmailDoesNotExist() {
        Optional<Credential> found = repository.findByEmail("noone@aplly.dev");

        assertThat(found).isEmpty();
    }

    @Test
    void shouldReturnTrueWhenEmailExists() {
        repository.save(new Credential("exists@aplly.dev","x"));

        assertThat(repository.existsByEmail("exists@aplly.dev")).isTrue();
    }

    @Test
    void shouldReturnFalseWhenEmailDoesNotExist() {
        assertThat(repository.existsByEmail("absent@aplly.dev")).isFalse();
    }
}
