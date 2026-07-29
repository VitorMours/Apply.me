package com.applyme.backend.auth;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class UserRegisteredEventTests {

    @Test
    @DisplayName("Deve armazenar e expor userId e email corretamente")
    void deveArmazenarEExporCamposCorretamente() {
        var event = new UserRegisteredEvent("user-123", "lucas@aplly.dev");

        assertThat(event.userId()).isEqualTo("user-123");
        assertThat(event.email()).isEqualTo("lucas@aplly.dev");
    }

    @Test
    @DisplayName("Dois eventos com os mesmos valores devem ser iguais")
    void doisEventosComMesmosValoresDevemSerIguais() {
        var event1 = new UserRegisteredEvent("user-123", "lucas@aplly.dev");
        var event2 = new UserRegisteredEvent("user-123", "lucas@aplly.dev");

        assertThat(event1).isEqualTo(event2);
        assertThat(event1.hashCode()).isEqualTo(event2.hashCode());
    }

    @Test
    @DisplayName("Eventos com valores diferentes não devem ser iguais")
    void eventosComValoresDiferentesNaoDevemSerIguais() {
        var event1 = new UserRegisteredEvent("user-123", "lucas@aplly.dev");
        var event2 = new UserRegisteredEvent("user-456", "outro@aplly.dev");

        assertThat(event1).isNotEqualTo(event2);
    }

    @Test
    @DisplayName("toString deve conter os valores dos campos")
    void toStringDeveConterOsValoresDosCampos() {
        var event = new UserRegisteredEvent("user-123", "lucas@aplly.dev");

        assertThat(event.toString())
            .contains("user-123")
            .contains("lucas@aplly.dev");
    }
}