package com.applyme.backend.users;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.applyme.backend.users.internal.UserProfile;
import com.applyme.backend.users.internal.UserProfileRepository;

@Service
public class UserService {

    @Autowired
    private UserProfileRepository repository;

    public UserService(UserProfileRepository repository) {
        this.repository = repository;
    }

    public void createProfile(UserProfile profile) {
        repository.save(profile);
    }

    public Optional<String> getProfileByEmail(String email) {
        Optional<UserProfile> profileSearched = repository.findByEmail(email);
        if (profileSearched.isPresent()){
            return Optional.of(profileSearched.get().getId());
        }
        return Optional.empty();
    }
    
    
    // public void getProfileById(){}
}