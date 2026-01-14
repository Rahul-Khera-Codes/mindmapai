from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from langchain import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

router = APIRouter()

class MindMapRequest(BaseModel):
    topic: str
    subtopics: list

class MindMapResponse(BaseModel):
    mind_map: dict

@router.post("/generate_mindmap", response_model=MindMapResponse)
async def generate_mindmap(request: MindMapRequest):
    try:
        # Initialize OpenAI model
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise HTTPException(status_code=500, detail="OpenAI API key not configured.")
        
        llm = OpenAI(api_key=openai_api_key)
        
        # Create a prompt for mind map generation
        prompt_template = PromptTemplate(
            input_variables=["topic", "subtopics"],
            template="Generate a structured mind map for the topic '{topic}' with the following subtopics: {subtopics}."
        )
        
        chain = LLMChain(llm=llm, prompt=prompt_template)
        
        # Generate mind map
        mind_map = chain.run(topic=request.topic, subtopics=request.subtopics)
        
        return MindMapResponse(mind_map=mind_map)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))