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

    public Optional<UserProfile> getProfileByEmail(String email) {
        return repository.findByEmail(email);
    }
    
    public Optional<UserProfile> getProfileById(String id){
        return repository.findById(id);
    }

    public boolean deleteProfile(String id) {
        Optional<UserProfile> profileSearched = repository.findById(id);
        if (profileSearched.isEmpty()) {
            System.out.println("Problema ao encontrar o usuario");
        }

        UserProfile profile = profileSearched.get();
        profile.setActive(false);
        repository.save(profile);
        return true;
    }
}