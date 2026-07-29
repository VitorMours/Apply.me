package com.applyme.backend.users;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.applyme.backend.users.internal.UserProfile;
import com.applyme.backend.users.internal.UserProfileRepository;

import jakarta.persistence.EntityNotFoundException;

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
    
    public Optional<String> getProfileById(String id){
        Optional<UserProfile> profileSearched = repository.findById(id);
        if (profileSearched.isPresent()) {
            return Optional.of(profileSearched.get().getEmail());
        }
        return Optional.empty();
    }

    public boolean deleteProfile(String id) {
        Optional<UserProfile> profileSearched = repository.findById(id);
        if (profileSearched.isEmpty()) {
            throw new EntityNotFoundException("Não foi encontrada uma entidade com o id: " + id);
        }

        UserProfile profile = profileSearched.get();
        profile.setActive(false);
        repository.save(profile);
        return true;
    }
}