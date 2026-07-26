package com.applyme.backend.auth.internal;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection="credentials")
public class Credential {
    @Id 
    private String id; 
    private String email; 
    private String passwordHash;

}


