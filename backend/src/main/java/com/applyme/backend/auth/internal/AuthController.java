package com.applyme.backend.auth.internal;

import org.springframework.web.bind.annotation.RestController;

import com.applyme.backend.auth.AuthService;
import com.applyme.backend.auth.internal.dto.AuthResponse;
import com.applyme.backend.auth.internal.dto.LoginRequest;
import com.applyme.backend.auth.internal.dto.RegisterRequest;

import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;


@Tag(name="Authentication", description="Endpoints for user authentication and registration")
@RestController
@RequestMapping("/api/auth") 
public class AuthController {

    @Autowired
    private AuthService service;

    @PostMapping("register")
    public ResponseEntity<AuthResponse> register(@Valid @RequestBody RegisterRequest body) {
        AuthResponse response = service.register(body.firstName(), body.lastName(), body.email(), body.password()); 
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    @PostMapping("login")
    public ResponseEntity<AuthResponse> login(@Valid @RequestBody LoginRequest body) {
        AuthResponse response = service.login(body.email(), body.password());
        return ResponseEntity.status(HttpStatus.OK).body(response);
    }

}