package com.applyme.backend.users.internal;

import com.applyme.backend.users.UserService;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/users")
public class UserProfileController {

    @Autowired
    private UserService userService;

    @PostMapping("/search")
    public ResponseEntity<Optional<UserProfile>> findByEmail(@Valid @RequestBody EmailRequest request) {
        Optional<UserProfile> user = userService.getProfileByEmail(request.email());
        return ResponseEntity.status(HttpStatus.OK).body(user);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Optional<UserProfile>> findById(@PathVariable String id) {
        Optional<UserProfile> user = userService.getProfileById(id);
        return ResponseEntity.status(HttpStatus.OK).body(user);
    }

    private static record EmailRequest(@NotBlank String email) {
    }
}
