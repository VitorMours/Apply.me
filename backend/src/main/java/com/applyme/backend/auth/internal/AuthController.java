package com.applyme.backend.auth.internal;

import org.springframework.web.bind.annotation.RestController;

import com.applyme.backend.auth.AuthService;
import com.applyme.backend.auth.internal.dto.AuthResponse;
import com.applyme.backend.auth.internal.dto.RegisterRequest;

import jakarta.validation.Valid;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestBody;
// import org.springframework.web.bind.annotation.GetMapping;
// import org.springframework.web.bind.annotation.PatchMapping;
// import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

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

}