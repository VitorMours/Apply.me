package com.applyme.backend.config;

import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

import static org.assertj.core.api.Assertions.assertThat;

class ApplicationPropertiesTest {

    @Test
    void mongodbUriPropertyShouldUseSpringDataNamespace() throws IOException {
        Path propertiesPath = Path.of("src/main/resources/application.properties");

        String content = Files.readString(propertiesPath);

        assertThat(content)
                .contains("spring.mongodb.uri=");
    }
}
