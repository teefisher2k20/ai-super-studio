import os


class AgentService:
    """Service for Conversational AI Agents"""


    def __init__(self):
        self.agents = {}
        
    def create_agent(self, name, system_prompt, voice_id):
        agent_id = f"agent_{os.urandom(4).hex()}"
        self.agents[agent_id] = {
            'id': agent_id,
            'name': name,
            'system_prompt': system_prompt,
            'voice_id': voice_id,
            'history': []
        }
        return self.agents[agent_id]
        
    def chat(self, agent_id, user_message):
        """Process a chat message"""
        if agent_id not in self.agents:
            raise Exception("Agent not found")
            
        agent = self.agents[agent_id]
        
        # Add user message to history
        agent['history'].append({'role': 'user', 'content': user_message})
        
        # 1. Simple Echo Logic (Fallback)
        # response_text = f"You said: {user_message}. (I am a basic echo bot for now.)"
        
        # 2. OpenAI / Local LLM Logic
        # If we had 'openai' installed and a key:
        # response = openai.ChatCompletion.create(...)
        
        # For this demo, let's simulate a "Helpful AI" response
        response_text = self._simulate_llm_response(
            user_message, agent['system_prompt']
        )
        
        agent['history'].append(
            {'role': 'assistant', 'content': response_text}
        )
        
        return {
            'response': response_text,
            'agent': agent['name']
        }
        
    def _simulate_llm_response(self, message, system_prompt):
        """Simple keyword-based response simulator for testing without GPU/API"""
        msg = message.lower()
        if "hello" in msg or "hi" in msg:
            return "Hello! How can I help you today?"
        elif "weather" in msg:
            return "I cannot check the real weather yet, but I hope it's sunny!"
        elif "name" in msg:
            return "I am your custom AI agent."
        else:
            return f"That's interesting! Tell me more about '{message}'."
            

agent_service = AgentService()
