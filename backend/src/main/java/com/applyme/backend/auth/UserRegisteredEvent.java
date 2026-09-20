package com.applyme.backend.auth;

public record UserRegisteredEvent(String userId, String firstName, String lastName, String email){}