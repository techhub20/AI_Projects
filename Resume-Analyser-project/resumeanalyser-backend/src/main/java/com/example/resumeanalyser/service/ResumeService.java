package com.example.resumeanalyser.service;

import java.io.IOException;
import java.util.Map;

import org.apache.tika.Tika;
import org.apache.tika.exception.TikaException;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.beans.factory.annotation.Value;

@Service
public class ResumeService {

    private final Tika tika = new Tika();
    private final RestTemplate restTemplate = new RestTemplate();

    @Value("${ai.service.url}")
    private String aiServiceUrl;


    public String extractText(MultipartFile file) throws IOException, TikaException {
        return tika.parseToString(file.getInputStream());
    }
    

    public Map<String, Object> callAIService(String resumeText, String jobDesc) {
        String aiUrl = aiServiceUrl;

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        Map<String, String> request = Map.of(
            "resumeText", resumeText,
            "jobDescription", jobDesc
        );

        HttpEntity<Map<String, String>> entity = new HttpEntity<>(request, headers);

        ResponseEntity<Map> response = restTemplate.postForEntity(aiUrl, entity, Map.class);
        return response.getBody();
    }
}
