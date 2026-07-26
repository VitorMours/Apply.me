package com.applyme.backend.users;

import org.springframework.stereotype.Service;
import com.applyme.backend.users.internal.UserProfile;
import com.applyme.backend.users.internal.UserProfileRepository;

@Service
public class UserService {

    private final UserProfileRepository repository;

    public UserService(UserProfileRepository repository) {
        this.repository = repository;
    }

    public void createProfile(UserProfile profile) {
        repository.save(profile);
    }
}