package com.applyme.backend.users.internal;

import org.springframework.stereotype.Component;
import org.springframework.context.event.EventListener;
import org.springframework.modulith.events.ApplicationModuleListener;

import com.applyme.backend.auth.UserRegisteredEvent;
import com.applyme.backend.users.UserService;

@Component 
public class UserProfileEventListener {

    private final UserService profileService;

    public UserProfileEventListener(UserService service) {
        this.profileService = service;
    }

    @ApplicationModuleListener 
    public void on(UserRegisteredEvent event) {
        profileService.createProfile(new UserProfile(event.firstName(), event.lastName(), event.email()));
    }
}