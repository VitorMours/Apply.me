package com.applyme.backend.users.internal;

import com.applyme.backend.users.UserService;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;

import org.springframework.beans.factory.annotation.Autowired;
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
    public ResponseEntity<UserProfile> findByEmail(@Valid @RequestBody EmailRequest request) {
        return userService.getProfileByEmail(request.email())
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/{id}")
    public ResponseEntity<UserProfile> findById(@PathVariable String id) {
        return userService.getProfileById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    private static record EmailRequest(@NotBlank String email) {
    }
}
