from langchain.prompts import PromptTemplate
prompt_template = PromptTemplate(template = 
                        """
                        Summarize the research paper {paper_input} in a 
                        {style_input} style within {length_input} words.
                        -Give the breif overview of the paper
                        - Exlain all the key aspects. 
                        - Include all the mathematical formulas if any for understanding. 
                        - Cross verify if all the facts are factually correct.
                        - Use simple language for understanding.
                        - Follow all the instrcutions mentioned above.
                        """,
                        input_variables = ["paper_name", "style_input", "length_input"]
                        )

prompt_template.save("prompt_template.json")