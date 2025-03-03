import streamlit as st
import json
from e2e_agentic_ai.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from e2e_agentic_ai.langgraphagenticai.LLMS.groqllm import GroqLLM
from e2e_agentic_ai.langgraphagenticai.graph.graph_builder import GraphBuilder
from e2e_agentic_ai.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStramlit

#Main FUnction start
def load_langgraph_agenticai_app():
    """
    Loads and runs the Langgraph AgenticAI applicaton which Steamlit UI.
    THis function initializes the UI, handle user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while implementing
    exception handling for robutsness.
    """

    # Load UI
    ui=LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load input from the UI")
        return
    
    # Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message=st.session_state.timeframe
    else:
        user_message=st.chat_input("Enter your message:")

    if user_message:
        try:
            # Configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model cloud not be initialized")
                return
            
            # INitialize and setup the graph based on usecase
            usecase =user_input.get('selected_usecase')
            if not usecase:
                st.error("Error: No use case selected.")
                return
            
            ### Graph Builder
            graph_bulder=GraphBuilder(model)
            try:
                graph=graph_bulder.setup_graph(usecase)
                DisplayResultStramlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error("Error: Graph setup failed -{e}")
                return
            
        except Exception as e:
            raise ValueError(f"Error occured with exception : {e}")