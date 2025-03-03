import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage, HumanMessage
from e2e_agentic_ai.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Con