package com.applyme.backend.users;


import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;

import com.applyme.backend.users.internal.UserProfile;
import com.applyme.backend.users.internal.UserProfileRepository;

import static org.assertj.core.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

import java.util.Optional;



public class UserServiceTests {

    private UserProfileRepository repository;
    private UserService service;

    @BeforeEach()
    void setUp() {
        repository = mock(UserProfileRepository.class);
        service = new UserService(repository);
    }

    @Test 
    @DisplayName("Consegue Registrar usuários novos")
    void ConsegueRegistrarUsuarioNovo() {
        UserProfile profile = new UserProfile(
            "Lucas",
            "Moura",
            "lucas.moura@gmail.com"
        );
        when(repository.existsByEmail("lucas.moura@gmail.com")).thenReturn(false);
        when(repository.save(any(UserProfile.class))).thenReturn(profile);

        service.createProfile(profile);
        verify(repository).save(any(UserProfile.class));
    }

    @Test 
    @DisplayName("Consegue buscar o usuario pelo email dele e recebe o id")
    void consegueBuscarOUsuarioPeloEmailDele() {
        UserProfile profile = new UserProfile(
            "Lucas",
            "Moura",
            "lucas.moura@gmail.com"
        );
        when(repository.existsByEmail("lucas.moura@gmail.com")).thenReturn(false);
        when(repository.save(any(UserProfile.class))).thenReturn(profile);
        when(repository.findByEmail("lucas.moura@gmail.com")).thenReturn(Optional.of(profile));

        service.createProfile(profile);
        Optional<String> profileSearched = service.getProfileByEmail(profile.getEmail());
        assertThat(profileSearched).contains(profile.getId());
    }

    @Test 
    @DisplayName("Consegue buscar o usuario pelo Id dele")
    void consegueBuscarOUsuarioPeloIdDele() {
        UserProfile profile = new UserProfile(
            "Lucas",
            "Moura",
            "lucas.moura@gmail.com"
        );

        when(repository.existsById(profile.getId())).thenReturn(false);
        when(repository.save(any(UserProfile.class))).thenReturn(profile);
        when(repository.findById(profile.getId())).thenReturn(Optional.of(profile));

        service.createProfile(profile);
        Optional<String> profileSearched = service.getProfileById(profile.getId());
        assertThat(profileSearched).contains(profile.getEmail());
    }

    // TODO: 



    // void consegueAtualizarUsuarioExistente
    // void retornaErroAtualizarUsuarioInexistente
    // void retornaErroAtualizarUsuarioSenhaOuEmailErrado
    // void softDeleteNoUsuario 
    
    @Test
    @DisplayName("Faz soft delete do usuario para nao deletar registro")
    void softDeleteDoUsuario() {
        UserProfile profile = new UserProfile(
            "Lucas",
            "Moura",
            "lucas.moura@gmail.com"
        );

        when(repository.findById(profile.getId())).thenReturn(Optional.of(profile));
        when(repository.save(any(UserProfile.class))).thenReturn(profile);

        service.deleteProfile(profile.getId());

        verify(repository, never()).delete(any(UserProfile.class));
        verify(repository).save(profile);
        assertThat(profile.isActive()).isFalse();
    }

    // void levantaErroTentandoDeletarUsuarioInexistente


}
