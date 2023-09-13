package com.app.dto;

import java.util.ArrayList;
import java.util.List;


import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class GTPReq {

	private String model;
    private List<Message> messages;
	
    public GTPReq(String model, String prompt) {
        this.model = model;
        this.messages = new ArrayList<>();
        this.messages.add(new Message("user",prompt));
    }
    
    
}
