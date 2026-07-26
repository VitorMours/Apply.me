package com.applyme.backend.users.internal;

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
class UserProfileRepositoryTest {

    @Container
    @ServiceConnection
    static MongoDBContainer mongo = new MongoDBContainer("mongo:7");

    @Autowired
    UserProfileRepository repository;

    @BeforeEach
    void cleanUp() {
        repository.deleteAll();
    }

    @Test
    void shouldFindUserByEmailWhenExists() {
        var profile = new UserProfile( "Vitor", "null", "vitor@aplly.dev", "hashed-senha");
        repository.save(profile);

        Optional<UserProfile> found = repository.findByEmail("vitor@aplly.dev");

        assertThat(found).isPresent();
        assertThat(found.get().getEmail()).isEqualTo("vitor@aplly.dev");
    }

    @Test
    void shouldReturnEmptyWhenEmailDoesNotExist() {
        Optional<UserProfile> found = repository.findByEmail("naoexiste@aplly.dev");

        assertThat(found).isEmpty();
    }

    @Test
    void shouldReturnTrueWhenEmailExists() {
        repository.save(new UserProfile( "hashed-senha", "Vitor", "vitor@aplly.dev", "null"));

        assertThat(repository.existsByEmail("vitor@aplly.dev")).isTrue();
    }

    @Test
    void shouldReturnFalseWhenEmailDoesNotExist() {
        assertThat(repository.existsByEmail("naoexiste@aplly.dev")).isFalse();
    }
}