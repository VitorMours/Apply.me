package com.applyme.backend.users.internal;

import java.util.Optional;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface UserProfileRepository extends MongoRepository<UserProfile, String> {

    Optional<UserProfile> findByEmail(String email);

    boolean existsByEmail(String email);
}