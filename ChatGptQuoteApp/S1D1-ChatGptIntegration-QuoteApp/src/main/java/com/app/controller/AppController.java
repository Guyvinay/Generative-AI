package com.app.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.client.RestTemplate;

import com.app.dto.GPTResp;
import com.app.dto.GTPReq;


public class AppController {

	@Qualifier("openaiRestTemplate")
    @Autowired
    private RestTemplate restTemplate;
    
    @Value("${openai.model}")
    private String model;
    
    @Value("${openai.api.url}")
    private String apiUrl;
    
    @GetMapping("/chat")
    public String chat(@RequestParam("prompt") String prompt) {
        // create a request
    	GTPReq request = new GTPReq(model, prompt);
        
        // call the API
        GPTResp response = restTemplate.postForObject(apiUrl, request, GPTResp.class);
        
        if (response == null || response.getChoices() == null || response.getChoices().isEmpty()) {
            return "No response";
        }
        
        // return the first response
        return response.getChoices().get(0).getMessage().getContent();
    }
	
}
