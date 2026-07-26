package com.applyme.backend.users;

import java.util.Optional;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import com.applyme.backend.users.internal.UserProfileRepository;
import static org.assertj.core.api.Assertions.*;
import static org.mockito.Mockito.*;

public class UserServiceTests {
    
    private UserProfileRepository repository;
    private UserService service;


    @BeforeEach()
    void setUp() {
        repository = mock(UserProfileRepository.class);
        service = new UserService(repository);
    }
}
