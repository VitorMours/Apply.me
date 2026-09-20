package com.applyme.backend.auth.internal;

import java.util.Optional;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface CredentialRepository extends MongoRepository<Credential, String> {
	Optional<Credential> findByEmail(String email);
	boolean existsByEmail(String email);
}
